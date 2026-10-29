from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

# Definiere, wie die Anfrage aussieht
class Query(BaseModel):
    prompt: str

@app.post("/ask")
async def ask(query: Query):
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    # Führe den Befehl aus (ohne /no_think, falls das Modell es nicht mag)
    result = subprocess.run(
        ["rag", "ask", query.prompt, "--chat-model", "qwen3:14b"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env
    )
    
    raw_output = result.stdout
    lines = raw_output.split("\n")
    clean_lines = []
    
    # Bereinige die ASCII-Box von local-rag
    for line in lines:
        if "│" in line:
            parts = line.split("│")
            if len(parts) > 1:
                text = parts[1].strip()
                clean_lines.append(text)
                
    answer = "\n".join(clean_lines)
    if not answer.strip():
        answer = "Ich habe keine Antwort gefunden."
        
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)