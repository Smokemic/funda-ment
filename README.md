# Funda-Ment

Ein lokaler, privater KI-Begleiter für Krebsbetroffene und Angehörige.

**Funda-Ment** hilft dabei, den Informationsfluss nach einer Krebsdiagnose zu ordnen, medizinische Fachbegriffe zu verstehen und Antworten auf offizielle, geprüfte Quellen zu stützen.

> **Wichtig:** Funda-Ment stellt keine Diagnosen, gibt keine Therapieempfehlungen und ersetzt keinen Arztbesuch. Bitte kläre alle medizinischen Fragen mit deinem Ärzteteam.

## Wie es funktioniert
- **100 % lokal:** Die Verarbeitung erfolgt komplett auf deinem Rechner. Es werden keine Daten an Cloud-Anbieter gesendet.
- **RAG (Retrieval-Augmented Generation):** Funda-Ment antwortet ausschließlich auf Basis der von dir bereitgestellten PDFs (z. B. vom Krebsinformationsdienst oder der Deutschen Krebshilfe) und zitiert die Quelle.
- **Ethische Leitplanken:** Das System ist angewiesen, keine Diagnosen zu stellen und bei fehlenden Informationen ehrlich zu sein.

## Voraussetzungen
- Python 3.12 oder 3.13
- Ollama (mit den Modellen `qwen3:14b` und `nomic-embed-text`)
- Hermes (für die Chat- und Sprachintegration)

## Installation
1. Klone dieses Repository.
2. Erstelle eine virtuelle Umgebung: `python -m venv venv`
3. Aktiviere sie: `venv\Scripts\activate` (Windows)
4. Installiere die Abhängigkeiten: `pip install ollama-local-rag`
5. Lade die PDFs von den offiziellen Seiten (z. B. krebsinformationsdienst.de) herunter und lege sie in den Ordner `01_Quellen`.
6. Indiziere die PDFs: `rag add "C:\Pfad\zu\deinen\PDFs"`

## Lizenz
MIT License