import sys
import subprocess
import os

def ask_rag(query):
    # Befehl für local-rag zusammenbauen
    command = [
        "rag", "ask", query, 
        "--chat-model", "qwen3:14b"
    ]
    
    # Windows-Umgebung zwingen, UTF-8 zu nutzen
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    try:
        # Führe den Befehl aus und fange die Ausgabe ab
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            encoding='utf-8', 
            errors='replace', # Verhindert Absturz bei kaputten Zeichen
            env=env,
            check=True
        )
        # Die Antwort ausgeben (stdout)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Datenbankabfrage:\n{e.stderr}")
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bitte eine Frage als Argument übergeben.")
        sys.exit(1)
    
    question = " ".join(sys.argv[1:])
    ask_rag(question)