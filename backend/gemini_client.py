import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

class GeminiClient:
    def __init__(self):  # Fixed: double underscores
        # Try both environment variable names
        self.api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        
        print(f"🔍 Loading Google AI API key: {self.api_key[:10] if self.api_key else 'None'}...")
        
        if self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-1.5-flash')  # Free model
                self.available = True
                print("✅ Google AI initialized successfully")
            except Exception as e:
                print(f"❌ Google AI initialization failed: {e}")
                self.available = False
        else:
            print("❌ No Google AI API key found in environment variables")
            self.available = False
    
    def enhance_summary(self, text: str) -> Optional[str]:
        """Use Google Gemini to enhance/validate Ollama summary"""
        if not self.available:
            print("❌ Google AI not available for enhance_summary")
            return None
        
        try:
            prompt = f"""Review this contract summary and add any important legal points that might be missing. Keep it concise:

Original Summary:
{text}

Enhanced Summary (add missing key legal points):"""
            
            response = self.model.generate_content(prompt)
            print("✅ Summary enhanced successfully")
            return response.text.strip()
        except Exception as e:
            print(f"❌ Gemini enhancement failed: {e}")
            return None
    
    def risk_analysis(self, text: str) -> Optional[str]:
        """Analyze legal risks using Gemini"""
        if not self.available:
            print("❌ Google AI not available for risk_analysis")
            return None
        
        try:
            prompt = f"""Analyze this legal text and identify TOP 3 RISKS in bullet points:

Legal Text:
{text[:3000]}

Risk Analysis (3 bullet points max):"""
            
            response = self.model.generate_content(prompt)
            print("✅ Risk analysis completed successfully")
            return response.text.strip()
        except Exception as e:
            print(f"❌ Risk analysis failed: {e}")
            return None
    
    def translate_hindi(self, text: str) -> Optional[str]:
        """Translate legal text to Hindi using Gemini"""
        if not self.available:
            print("❌ Google AI not available for translate_hindi")
            return None
        
        try:
            prompt = f"""Translate this legal text to Hindi, keeping legal terms accurate:

English Text:
{text}

Hindi Translation:"""
            
            response = self.model.generate_content(prompt)
            print("✅ Hindi translation completed successfully")
            return response.text.strip()
        except Exception as e:
            print(f"❌ Translation failed: {e}")
            return None

# Global instance
gemini_client = GeminiClient()
