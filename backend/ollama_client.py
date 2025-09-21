import os
import requests
from typing import Optional

# Gemini API base URL
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models"
GEMINI_MODEL = "gemini-1.5-flash-latest"  # tu change kar sakta hai agar aur model use karna ho
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # env me set karna zaroori hai

def generate(prompt: str, model: str = GEMINI_MODEL, options: Optional[dict] = None) -> str:
    if not GEMINI_API_KEY:
        raise ValueError("❌ GEMINI_API_KEY not set in environment variables")

    url = f"{GEMINI_URL}/{model}:generateContent?key={GEMINI_API_KEY}"

    # Gemini payload format
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    # options ke liye support (temperature, maxOutputTokens etc.)
    if options:
        generation_config = {}
        if "temperature" in options:
            generation_config["temperature"] = options["temperature"]
        if "num_predict" in options:  # map to Gemini's maxOutputTokens
            generation_config["maxOutputTokens"] = options["num_predict"]
        if generation_config:
            payload["generationConfig"] = generation_config

    headers = {"Content-Type": "application/json"}

    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()

    data = resp.json()
    # Extract response text
    return (
        data.get("candidates", [{}])[0]
        .get("content", {})
        .get("parts", [{}])[0]
        .get("text", "")
        .strip()
    )
