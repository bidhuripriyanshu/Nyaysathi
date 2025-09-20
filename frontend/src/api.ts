export const API = (typeof import.meta !== "undefined" && (import.meta as any).env?.VITE_API_URL)
  || (typeof window !== "undefined" ? window.localStorage.getItem("API_BASE") || "" : "")
  || "http://localhost:8000";

async function handleResponse(r: Response){
  if(r.ok){
    return r.json();
  }
  const contentType = r.headers.get("content-type") || "";
  let details = "";
  try{
    if(contentType.includes("application/json")){
      const j = await r.json();
      details = typeof j === "string" ? j : JSON.stringify(j);
    }else{
      details = await r.text();
    }
  }catch{}
  const snippet = (details || "").slice(0, 300);
  throw new Error(`HTTP ${r.status} ${r.statusText}${snippet ? `: ${snippet}` : ""}`);
}

export async function ping(){
  try{
    const r = await fetch(`${API}/health`, { method: "GET" });
    return await handleResponse(r);
  }catch(ex:any){
    throw new Error(`Cannot reach API at ${API}. ${ex?.message || ""}`);
  }
}

export async function uploadFile(file: File){
  const fd = new FormData();
  fd.append("file", file);
  try{
    const r = await fetch(`${API}/upload`, { method:"POST", body: fd });
    return await handleResponse(r);
  }catch(ex:any){
    const hint = `Failed to reach API at ${API}. Make sure backend is running (uvicorn on :8000), CORS allows origin, and no firewall is blocking.`;
    throw new Error(`${ex?.message || "Upload failed"}. ${hint}`);
  }
}

export async function analyze(mode: "summarize"|"simplify"|"qa", text: string, question?: string){
  try{
    const r = await fetch(`${API}/analyze`, {
      method:"POST",
      headers: { "Content-Type":"application/json" },
      body: JSON.stringify({ mode, text, question })
    });
    return await handleResponse(r);
  }catch(ex:any){
    throw new Error(`${ex?.message || "Analyze failed"}`);
  }
}

export async function enhanceSummary(text: string) {
  try {
    const r = await fetch(`${API}/enhance-summary`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });
    return await handleResponse(r);
  } catch (ex: any) {
    throw new Error(`${ex?.message || "Enhance summary failed"}`);
  }
}

export async function riskAnalysis(text: string) {
  try {
    const r = await fetch(`${API}/risk-analysis`, {
      method: "POST", 
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });
    return await handleResponse(r);
  } catch (ex: any) {
    throw new Error(`${ex?.message || "Risk analysis failed"}`);
  }
}

export async function translateHindi(text: string) {
  try {
    const r = await fetch(`${API}/translate-hindi`, {
      method: "POST",
      headers: { "Content-Type": "application/json" }, 
      body: JSON.stringify({ text })
    });
    return await handleResponse(r);
  } catch (ex: any) {
    throw new Error(`${ex?.message || "Hindi translation failed"}`);
  }
}

export async function googleAIStatus() {
  try {
    const r = await fetch(`${API}/google-ai-status`, { method: "GET" });
    return await handleResponse(r);
  } catch (ex: any) {
    throw new Error(`${ex?.message || "Status check failed"}`);
  }
}
