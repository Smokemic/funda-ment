# Funda-Ment (Bausatz)

Ein lokaler, privater KI-Begleiter für Menschen, die mit einer Krebsdiagnose konfrontiert sind, sowie für deren Angehörige. 

Dieses Repository enthält den **Code (Bausatz)**, um Funda-Ment auf dem eigenen Rechner nachzubauen. Es ist als Open-Source-Bildungsprojekt gedacht.

> ⚠️ **WICHTIGER HINWEIS:** Funda-Ment ist ein rein informatives Recherche-Tool. Es stellt **keine Diagnosen**, gibt **keine Therapieempfehlungen** und ersetzt **keinen Arztbesuch**. Die Nutzung erfolgt auf eigene Verantwortung. Bitte kläre alle medizinischen Fragen mit deinem Ärzteteam oder dem Krebsinformationsdienst.

---

## 🚨 WICHTIG: Die Datenbank ist anfangs LEER!

Dieses Repository enthält **keine** medizinischen Texte oder PDFs. Aus rechtlichen Gründen (Urheberrecht) werden keine Inhalte Dritter geteilt. 

Das System funktioniert erst, wenn du ihm Wissen beibringst!
- Die Datei `urls.txt` ist **leer** (enthält nur einen Platzhalter-Kommentar).
- Die RAG-Datenbank (der Ordner `01_Quellen`) existiert bei dir noch nicht.

**Du musst also selbst entscheiden, welche Quellen (z.B. Webseiten oder PDFs) du einlesen willst, bevor das System Antworten geben kann.**

---

## 💻 Systemanforderungen (Hardware)

Da alles lokal läuft, brauchst du genug VRAM (Grafikkartenspeicher). 

*   **Empfohlen (für das große Modell `qwen3:14b`):** Eine GPU mit **mindestens 12–16 GB VRAM** (z.B. NVIDIA RTX 3060/4060 Ti 16GB, AMD RX 7800 XT / 9070 XT). Das Modell belegt ca. 13,5 GB VRAM (bei Q4-Quantisierung), läuft auf einer 16-GB-Karte aber flüssig (ca. 45–50 Tokens/Sekunde) [citation:8].
*   **RAM:** Mindestens 16 GB System-RAM.
*   **Lightweight-Alternative (für schwächere PCs):** Wenn du weniger VRAM hast (z.B. 8 GB), kannst du ein kleineres Modell nutzen. **Tipp:** Probiere `qwen3:4b` oder ein deutsches Modell wie **ELMOD-2.7B** (vom Fraunhofer IIS), das speziell für ressourcenbeschränkte Umgebungen entwickelt wurde [citation:9]. Du musst dann in den Skripten den Modellnamen von `qwen3:14b` auf das kleinere Modell ändern.

## Voraussetzungen
- Windows (getestet)
- Python 3.12 oder 3.13 (in einer virtuellen Umgebung)
- Ollama (mit den Modellen `qwen3:14b` **oder** einem kleineren Modell wie `qwen3:4b` und `nomic-embed-text`)
- [Optional] Hermes (für die Chat- und Sprachintegration)

## Installation (Schritt für Schritt)

1. **Repository klonen**
   ```bash
   git clone https://github.com/DEIN-NAME/funda-ment.git
   cd funda-ment