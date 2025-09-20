import React from "react";
import { motion } from "framer-motion";
import Header from "./components/Header";
import Hero from "./components/Hero";
import UploadZone from "./components/UploadZone";
import SummarySection from "./components/SummarySection";
import QASection from "./components/QASection";
import ClauseAnalysis from "./components/ClauseAnalysis";
import GoogleAI from "./components/GoogleAI";
import { ping, API, enhanceSummary, riskAnalysis, translateHindi } from "./api";

export default function App() {
  const [text, setText] = React.useState("");
  const [sections, setSections] = React.useState<[string, string][]>([]);
  const [risks, setRisks] = React.useState<[string, number][]>([]);
  const [summary, setSummary] = React.useState("");
  const [status, setStatus] = React.useState("");
  const [isConnected, setIsConnected] = React.useState(false);

  React.useEffect(() => {
    (async () => {
      try {
        await ping();
        setStatus(`Connected to API: ${API}`);
        setIsConnected(true);
      } catch (ex: any) {
        setStatus(ex?.message || "API unreachable");
        setIsConnected(false);
      }
    })();
  }, []);

  const onLoaded = (payload: any) => {
    setText(payload.text || "");
    setSections(payload.sections || []);
    setRisks(payload.risks || []);
  };

  return (
    <div className="app">
      <Header status={status} isConnected={isConnected} />
      
      <main className="main-content">
        <Hero />
        
        <UploadZone onLoaded={onLoaded} />

        {text && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
          >
            <div className="results-grid">
              <SummarySection text={text} risks={risks} onSummaryChange={setSummary} />
              <QASection docText={text} />
            </div>
            
            <div style={{ marginTop: '2rem' }}>
              <ClauseAnalysis sections={sections} />
            </div>

            <div style={{ marginTop: '2rem' }}>
              <GoogleAI 
                text={text} 
                summary={summary}
                enhanceSummary={enhanceSummary}
                riskAnalysis={riskAnalysis}
                translateHindi={translateHindi}
              />
            </div>
          </motion.div>
        )}
      </main>
    </div>
  );
}

