from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Literal

# absolute imports to avoid "no known parent package"
from backend.extract import extract_text, split_sections, highlight_risks
from backend.prompts import SUMMARIZE_PROMPT, SIMPLIFY_PROMPT, QA_PROMPT
from backend.ollama_client import generate
from backend.gemini_client import gemini_client  # adjust if module is elsewhere

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Local Legal Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"ok": True}

class AnalyzeBody(BaseModel):
    mode: Literal["summarize", "simplify", "qa"]
    text: Optional[str] = None
    question: Optional[str] = None
    model: Optional[str] = "llama3.2"

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    raw = await file.read()
    text = extract_text(raw, file.filename)
    sections = split_sections(text)
    risks = highlight_risks(text)
    return {"text": text, "sections": sections, "risks": risks}

@app.post("/analyze")
async def analyze(body: AnalyzeBody):
    if not body.text:
        return {"error": "text required"}

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

    return {"error": "unsupported mode"}

@app.post("/enhance-summary")
async def enhance_summary(body: AnalyzeBody):
    if not body.text:
        return {"error": "text required"}
    enhanced = gemini_client.enhance_summary(body.text[:2000])
    if enhanced:
        return {"enhanced_summary": enhanced, "powered_by": "Google Gemini AI"}
    else:
        return {"error": "Google AI Studio not available"}

@app.post("/risk-analysis")
async def risk_analysis(body: AnalyzeBody):
    result = gemini_client.risk_analysis(body.text)
    if result:
        return {"risk_analysis": result, "powered_by": "Google Gemini AI"}
    else:
        return {"error": "Risk analysis unavailable"}

@app.post("/translate-hindi")
async def translate_hindi(body: AnalyzeBody):
    result = gemini_client.translate_hindi(body.text[:1000])
    if result:
        return {"hindi_translation": result, "powered_by": "Google Gemini AI"}
    else:
        return {"error": "Translation unavailable"}

@app.get("/google-ai-status")
async def google_ai_status():
    return {
        "google_ai_available": gemini_client.available,
        "service": "Google AI Studio (Free Tier)",
        "model": "Gemini 1.5 Flash",
        "billing_required": False
    }
