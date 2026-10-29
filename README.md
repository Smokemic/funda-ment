<h1 align="center">Funda-Ment</h1><p align="center"> <strong>In liebevoller Erinnerung an Funda 🤍</strong> </p><p align="center"> Ein lokales, datenschutzfreundliches RAG-System (Retrieval-Augmented Generation) für krebsbezogene Informationen. </p>

---

### 💡 Warum dieses Projekt?

Dieses Projekt ist aus einer persönlichen Geschichte entstanden. Die Idee zu Funda-Ment hatte ich, als meine Schwester Funda die Diagnose Krebs im Endstadium bekam und wir alle sehr viele Fragen hatten aber umso mehr Antworten gebraucht haben. Der ursprüngliche Gedanke war, einen Ort zu schaffen, an dem Betroffene, Angehörige und Freunde schnell und unkompliziert verlässliche Antworten auf ihre Fragen finden können ohne all ihre Daten preiszugeben oder sich anmelden zu müssen, schnell und unkompliziert, ein digitales Fundament für Menschen in einer schwierigen Lebenssituation.

Ursprünglich war geplant, dieses System als öffentlich zugängliches Webangebot bereitzustellen. Aus rechtlichen Gründen ist das jedoch nicht möglich (siehe unten). Das Projekt ist dennoch fertiggestellt worden, weil der Weg das Ziel war: Es geht darum, zu zeigen, dass man mit den richtigen Werkzeugen Wissen aufbereiten und sinnvoll nutzbar machen kann und weil es für mich ein wichtiger Teil der Verarbeitung war, diese Idee zu Ende zu bringen.

---

### ⚖️ Warum läuft das nur lokal?

---


Ein öffentlicher Betrieb wäre aus mehreren Gründen problematisch gewesen:

- **Urheberrecht:** Die medizinischen Inhalte (z. B. PDFs der Deutschen Krebshilfe) sind urheberrechtlich geschützt. Eine öffentliche Bereitstellung dieser Texte in einer Datenbank ist ohne explizite Genehmigung nicht erlaubt.
- **Medizinische Verantwortung:** Ein KI-System, das medizinische Fragen beantwortet, muss extrem hohe Anforderungen an Korrektheit und Sicherheit erfüllen, um niemanden zu gefährden. Das ist ohne ärztliche Supervision nicht verantwortbar.
- **Datenschutz:** Gesundheitsdaten sind besonders sensibel. Eine lokale, private Installation stellt sicher, dass keine Daten das eigene Gerät verlassen.

Das System ist deshalb als **lokales Werkzeug** konzipiert: Du entscheidest, welche Quellen du einliest, du behältst die Kontrolle über die Daten, und nichts wird irgendwohin hochgeladen. Es ist ein Fundament, das du selbst mit Wissen füllen kannst.

---

## 📂 Projektstruktur

Das Repository ist wie folgt aufgebaut:

funda-ment/

├── 01_Quellen/ (Deine PDFs und Quelldateien, anfangs leer)

├── 02_Datenbank/ (Die lokale Vektordatenbank, wird automatisch befüllt)

├── 03_Logs/ (Log-Dateien für Fehlersuche und Monitoring)

├── venv/ (Python Virtual Environment, nicht versioniert)

├── app.py (Hauptanwendung / Einstiegspunkt)

├── crawl_krebshilfe.py (Crawler-Skript zum Einlesen spezifischer Webseiten)

├── funda_rag.py (Kernlogik für das RAG: Retrieval, Embeddings, Chat)

├── server.py (Lokaler Server, z.B. für die Chat-Oberfläche)

├── requirements.txt (Python-Abhängigkeiten)

├── .gitignore (Git-Ignore-Datei)

└── README.md (Diese Datei)

**Hinweis:** Die Ordner 01_Quellen, 02_Datenbank und 03_Logs sind anfangs leer. Das System befüllt sie erst, wenn du eigene Quellen (PDFs oder Webseiten) einliest.

---

### 🚨 WICHTIG: Die Datenbank ist anfangs LEER!

---


Dieses Repository enthält keine medizinischen Texte oder PDFs. Aus rechtlichen Gründen (Urheberrecht) werden keine Inhalte Dritter geteilt.

Das System funktioniert erst, wenn du ihm Wissen beibringst!

- Die Datei urls.txt ist leer (enthält nur einen Platzhalter-Kommentar).
- Die RAG-Datenbank (der Ordner 01_Quellen) existiert bei dir noch nicht.

**Du musst also selbst entscheiden, welche Quellen (z.B. Webseiten oder PDFs) du einlesen willst, bevor das System Antworten geben kann.**

---

### 💻 Systemanforderungen (Hardware)

---


Da alles lokal läuft, brauchst du genug VRAM (Grafikkartenspeicher).

- **Empfohlen (für das große Modell qwen3:14b):** Eine GPU mit mindestens 12–16 GB VRAM (z.B. NVIDIA RTX 3060/4060 Ti 16GB, AMD RX 7800 XT / 9070 XT). Das Modell belegt ca. 13,5 GB VRAM (bei Q4-Quantisierung), läuft auf einer 16-GB-Karte aber flüssig (ca. 45–50 Tokens/Sekunde).
- **RAM:** Mindestens 16 GB System-RAM.
- **Lightweight-Alternative (für schwächere PCs):** Wenn du weniger VRAM hast (z.B. 8 GB), kannst du ein kleineres Modell nutzen. **Tipp:** Probiere qwen3:4b oder ein deutsches Modell wie **ELMOD-2.7B** (vom Fraunhofer IIS), das speziell für ressourcenbeschränkte Umgebungen entwickelt wurde. Du musst dann in den Skripten den Modellnamen von qwen3:14b auf das kleinere Modell ändern.

---

### ⚙️ Voraussetzungen

---


- Windows (getestet)
- Python 3.12 oder 3.13 (in einer virtuellen Umgebung)
- Ollama (mit den Modellen qwen3:14b oder einem kleineren Modell wie qwen3:4b und nomic-embed-text)
- \[Optional] Hermes (für die Chat- und Sprachintegration)

---

### 🛠️ Installation (Schritt für Schritt)

---


1. **Repository klonen**\
   Führe diese Befehle in deinem Terminal aus:

   git clone https://github.com/DEIN-NAME/funda-ment.git
   cd funda-ment


---

Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die Datei LICENSE für Details.

<p> Mit Hilfe von DeepSeek gebaut 🤍 </p>




---

<h1 align="center">Funda-Ment (English)</h1><p align="center"> <strong>In loving memory of Funda 🤍</strong> </p><p align="center"> A local, privacy-focused RAG system (Retrieval-Augmented Generation) for cancer-related information. </p>

---



### 💡 Why this project?

---


This project grew out of a personal story. The idea for Funda-Ment came to me when my sister Funda was diagnosed with terminal cancer and we all had so many questions – but needed even more answers. The original thought was to create a place where those affected, their families, and friends could quickly and easily find reliable answers to their questions – without having to give away all their data or sign up. Quick and uncomplicated – a digital foundation for people in a difficult life situation.

Originally, the plan was to make this system publicly available as a web service. However, for legal reasons, this is not possible especially in Germany (see below). Nevertheless, the project was completed because the journey was the goal: it demonstrates that with the right tools, knowledge can be processed and made useful – and because finishing this idea was an important part of my own healing process.

---

### ⚖️ Why does it run only locally?

---


A public deployment would have been problematic for several reasons:

- **Copyright:** The medical content (e.g., PDFs from the German Cancer Aid) is protected by copyright. Publicly providing these texts in a database without explicit permission is not allowed.
- **Medical responsibility:** An AI system that answers medical questions must meet extremely high standards of accuracy and safety to avoid harming anyone. This is not justifiable without medical supervision.
- **Data privacy:** Health data is particularly sensitive. A local, private installation ensures that no data leaves your device.

Therefore, the system is designed as a **local tool**: you decide which sources to ingest, you retain control over the data, and nothing is uploaded anywhere. It is a foundation that you can fill with knowledge yourself.

---

### 📂 Project Structure

---


The repository is structured as follows:

funda-ment/

├── 01_Quellen/ (Your PDFs and source files, initially empty)

├── 02_Datenbank/ (The local vector database, populated automatically)

├── 03_Logs/ (Log files for troubleshooting and monitoring)

├── venv/ (Python Virtual Environment, not versioned)

├── app.py (Main application / entry point)

├── crawl_krebshilfe.py (Crawler script for ingesting specific websites)

├── funda_rag.py (Core logic for the RAG: retrieval, embeddings, chat)

├── server.py (Local server, e.g., for the chat interface)

├── requirements.txt (Python dependencies)

├── .gitignore (Git ignore file)

└── README.md (This file)

**Note:** The folders 01_Quellen, 02_Datenbank, and 03_Logs are initially empty. The system fills them only when you ingest your own sources (PDFs or websites).

---

### 🚨 IMPORTANT: The Database is EMPTY by default!

---


This repository contains no medical texts or PDFs. For legal reasons (copyright), no third-party content is shared.

The system only works once you teach it knowledge!

- The file urls.txt is empty (contains only a placeholder comment).
- The RAG database (the 01_Quellen folder) does not exist yet on your system.

**You must decide for yourself which sources (e.g., websites or PDFs) you want to ingest before the system can provide answers.**

---

### 💻 System Requirements (Hardware)

---


Since everything runs locally, you need enough VRAM (graphics card memory).

- **Recommended (for the large model qwen3:14b):** A GPU with at least 12–16 GB VRAM (e.g., NVIDIA RTX 3060/4060 Ti 16GB, AMD RX 7800 XT / 9070 XT). The model uses approx. 13.5 GB VRAM (with Q4 quantization) but runs smoothly on a 16 GB card (approx. 45–50 tokens/second).
- **RAM:** At least 16 GB system RAM.
- **Lightweight alternative (for weaker PCs):** If you have less VRAM (e.g., 8 GB), you can use a smaller model. **Tip:** Try qwen3:4b or a German model like **ELMOD-2.7B** (from Fraunhofer IIS), which was specifically developed for resource-constrained environments. You will need to change the model name in the scripts from qwen3:14b to the smaller model.

---

### ⚙️ Prerequisites

---


- Windows (tested)
- Python 3.12 or 3.13 (in a virtual environment)
- Ollama (with the models qwen3:14b or a smaller model like qwen3:4b and nomic-embed-text)
- \[Optional] Hermes (for chat and voice integration)

---

### 🛠️ Installation (Step by Step)

---


1. **Clone the repository**\
   Führe diese Befehle in deinem Terminal aus:


   git clone https://github.com/DEIN-NAME/funda-ment.git
   cd funda-ment


---
   

This project is licensed under the MIT License – see the [LICENSE](https://license/) file for details.

<p> Built with the help of DeepSeek 🤍 </p>
