import React, { useState } from 'react';
import { Sparkles, Shield, Languages, Loader2 } from 'lucide-react';

interface GoogleAIProps {
  text: string;
  summary: string;
}

export default function GoogleAI({ text, summary }: GoogleAIProps) {
  const [enhanced, setEnhanced] = useState("");
  const [risks, setRisks] = useState("");
  const [hindi, setHindi] = useState("");
  const [loading, setLoading] = useState<string>("");

  const callGoogleAPI = async (endpoint: string, setter: (val: string) => void, loadingKey: string) => {
    setLoading(loadingKey);
    try {
      console.log(`🔍 Calling: ${endpoint}`);
      
      const response = await fetch(`http://localhost:8000/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: endpoint === 'enhance-summary' ? summary : text })
      });
      
      const data = await response.json();
      console.log(`📥 Response:`, data);
      
      // Fix: Use correct response keys
      let resultKey;
      if (endpoint === 'enhance-summary') {
        resultKey = 'enhanced_summary';
      } else if (endpoint === 'risk-analysis') {
        resultKey = 'risk_analysis';
      } else if (endpoint === 'translate-hindi') {
        resultKey = 'hindi_translation';  // This was the missing piece!
      }
      
      console.log(`🔑 Looking for key: ${resultKey}`);
      
      if (data[resultKey]) {
        console.log(`✅ Found result: ${data[resultKey].substring(0, 100)}...`);
        setter(data[resultKey]);
      } else {
        console.log(`❌ No data found for key: ${resultKey}`, data);
      }
    } catch (error) {
      console.error('❌ Error:', error);
    } finally {
      setLoading("");
    }
  };

  return (
    <div className="card fade-in" style={{
      background: 'linear-gradient(135deg, rgba(168, 85, 247, 0.1) 0%, rgba(139, 69, 19, 0.05) 100%)',
      border: '1px solid rgba(168, 85, 247, 0.2)'
    }}>
      <div className="card-header">
        <Sparkles className="card-icon" />
        <h3 className="card-title">Google AI Studio Enhancement</h3>
        <span style={{ 
          fontSize: '0.75rem', 
          background: 'rgba(34, 197, 94, 0.2)', 
          padding: '0.25rem 0.5rem', 
          borderRadius: '0.25rem',
          color: '#22c55e'
        }}>
          FREE - No Billing Required
        </span>
      </div>
      
      <div className="grid grid-3" style={{ gap: '1rem' }}>
        <button
          className="btn btn-primary btn-sm"
          onClick={() => callGoogleAPI('enhance-summary', setEnhanced, 'enhance')}
          disabled={loading === 'enhance' || !summary}
        >
          {loading === 'enhance' ? (
            <><Loader2 className="spinner" size={16} />Enhancing...</>
          ) : (
            <><Sparkles size={16} />Enhance Summary</>
          )}
        </button>
        
        <button
          className="btn btn-primary btn-sm"
          onClick={() => callGoogleAPI('risk-analysis', setRisks, 'risk')}
          disabled={loading === 'risk' || !text}
        >
          {loading === 'risk' ? (
            <><Loader2 className="spinner" size={16} />Analyzing...</>
          ) : (
            <><Shield size={16} />Risk Analysis</>
          )}
        </button>
        
        <button
          className="btn btn-primary btn-sm"
          onClick={() => callGoogleAPI('translate-hindi', setHindi, 'hindi')}
          disabled={loading === 'hindi' || !text}
        >
          {loading === 'hindi' ? (
            <><Loader2 className="spinner" size={16} />Translating...</>
          ) : (
            <><Languages size={16} />Hindi Translation</>
          )}
        </button>
      </div>

      {enhanced && (
        <div style={{ marginTop: '1rem' }}>
          <label className="input-label">🚀 Google Gemini Enhanced Summary</label>
          <div className="result-content slide-up">{enhanced}</div>
        </div>
      )}

      {risks && (
        <div style={{ marginTop: '1rem' }}>
          <label className="input-label">🛡️ Google Gemini Risk Analysis</label>
          <div className="result-content slide-up">{risks}</div>
        </div>
      )}

      {hindi && (
        <div style={{ marginTop: '1rem' }}>
          <label className="input-label">🇮🇳 Google Gemini Hindi Translation</label>
          <div className="result-content slide-up">{hindi}</div>
        </div>
      )}
    </div>
  );
}
