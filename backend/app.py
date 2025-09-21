from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Literal
from dotenv import load_dotenv
from fastapi.exception_handlers import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# local imports (with backend prefix)
from backend.extract import extract_text, split_sections, highlight_risks
from backend.prompts import SUMMARIZE_PROMPT, SIMPLIFY_PROMPT, QA_PROMPT
from backend.ollama_client import generate
from backend.gemini_client import gemini_client

import os

# load environment variables
load_dotenv(override=False)
app = FastAPI(title="Local Legal Assistant API")

# ✅ CORS setup (for all origins during testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Custom error handlers to always return CORS headers
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": str(exc.detail)},
        headers={"Access-Control-Allow-Origin": "*"}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
        headers={"Access-Control-Allow-Origin": "*"}
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
        headers={"Access-Control-Allow-Origin": "*"}
    )


# Health check
@app.get("/health")
async def health():
    return {"ok": True}


# Request models
class AnalyzeBody(BaseModel):
    mode: Literal["summarize", "simplify", "qa"]
    text: Optional[str] = None
    question: Optional[str] = None
    model: Optional[str] = "llama3.2"


class SimpleBody(BaseModel):
    text: str


# Upload file API
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    raw = await file.read()
    text = extract_text(raw, file.filename)
    sections = split_sections(text)
    risks = highlight_risks(text)
    return {"text": text, "sections": sections, "risks": risks}


# Analyze text API
@app.post("/analyze")
async def analyze(body: AnalyzeBody):
    if not body.text:
        raise HTTPException(status_code=400, detail="text required")

    if body.mode == "summarize":
        prompt = SUMMARIZE_PROMPT.format(content=body.text[:120000])
        out = generate(prompt, model=body.model, options={"temperature": 0.3, "num_predict": 512})
        return {"result": out}

    if body.mode == "simplify":
        prompt = SIMPLIFY_PROMPT.format(content=body.text[:16000])
        out = generate(prompt, model=body.model, options={"temperature": 0.3, "num_predict": 400})
        return {"result": out}

    if body.mode == "qa":
        q = body.question or ""
        prompt = QA_PROMPT.format(content=body.text[:120000], question=q)
        out = generate(prompt, model=body.model, options={"temperature": 0.2, "num_predict": 384})
        return {"result": out}

    raise HTTPException(status_code=400, detail="unsupported mode")


@app.post("/enhance-summary")
async def enhance_summary(body: SimpleBody):
    if not body.text:
        raise HTTPException(status_code=400, detail="Text required")

    enhanced = gemini_client.enhance_summary(body.text[:2000])
    if enhanced:
        return {"enhanced_summary": enhanced, "powered_by": "Google Gemini AI"}
    else:
        raise HTTPException(status_code=503, detail="Google AI Studio not available")


# Risk analysis
@app.post("/risk-analysis")
async def risk_analysis(body: SimpleBody):
    if not body.text:
        raise HTTPException(status_code=400, detail="Text required")

    result = gemini_client.risk_analysis(body.text)
    if result:
        return {"risk_analysis": result, "powered_by": "Google Gemini AI"}
    else:
        raise HTTPException(status_code=503, detail="Risk analysis unavailable")


# Translate to Hindi
@app.post("/translate-hindi")
async def translate_hindi(body: SimpleBody):
    if not body.text:
        raise HTTPException(status_code=400, detail="Text required")

    result = gemini_client.translate_hindi(body.text[:1000])
    if result:
        return {"hindi_translation": result, "powered_by": "Google Gemini AI"}
    else:
        raise HTTPException(status_code=503, detail="Translation unavailable")


# Google AI status
@app.get("/google-ai-status")
async def google_ai_status():
    return {
        "google_ai_available": getattr(gemini_client, "available", False),
        "service": "Google AI Studio (Free Tier)",
        "model": "Gemini 1.5 Flash",
        "billing_required": False,
    }
