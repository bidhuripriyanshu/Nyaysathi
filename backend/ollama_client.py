import os
import requests
from typing import Optional

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models"
GEMINI_MODEL = "gemini-1.5-flash-latest"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set or empty in environment variables")

def generate(prompt: str, options: Optional[dict] = None) -> str:
    url = f"{GEMINI_URL}/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    if options:
        generation_config = {}
        if "temperature" in options:
            generation_config["temperature"] = options["temperature"]
        if "num_predict" in options:
            generation_config["maxOutputTokens"] = options["num_predict"]
        if generation_config:
            payload["generationConfig"] = generation_config

    headers = {"Content-Type": "application/json"}

    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    return (
        data.get("candidates", [{}])[0]
        .get("content", {})
        .get("parts", [{}])[0]
        .get("text", "")
        .strip()
    )
