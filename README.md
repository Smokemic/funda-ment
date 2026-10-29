<h1 align="center" style="font-size: 4em; margin-bottom: 0;">Funda-Ment</h1>

<p align="center">
  <strong>In liebevoller Erinnerung an Funda 🤍</strong>
</p>

<p align="center">
  Ein lokales, datenschutzfreundliches RAG-System (Retrieval-Augmented Generation) für krebsbezogene Informationen.
</p>

---

---

## 💡 Warum dieses Projekt?

Dieses Projekt ist aus einer persönlichen Geschichte entstanden: Ich habe es in Erinnerung an meine Schwester Funda gebaut, die an Krebs verstorben ist. Der ursprüngliche Gedanke war, einen Ort zu schaffen, an dem Betroffene, Angehörige und Freunde schnell und unkompliziert verlässliche Antworten auf ihre Fragen finden können – ein digitales Fundament für Menschen in einer schwierigen Lebenssituation.

Ursprünglich war geplant, dieses System als öffentlich zugängliches Webangebot bereitzustellen. Aus rechtlichen Gründen ist das jedoch nicht möglich (siehe unten). Das Projekt ist dennoch fertiggestellt worden, weil der Weg das Ziel war: Es geht darum, zu zeigen, dass man mit den richtigen Werkzeugen Wissen aufbereiten und sinnvoll nutzbar machen kann – und weil es für mich ein wichtiger Teil der Verarbeitung war, diese Idee zu Ende zu bringen.

## ⚖️ Warum läuft das nur lokal?

Ein öffentlicher Betrieb wäre aus mehreren Gründen problematisch gewesen:
- **Urheberrecht:** Die medizinischen Inhalte (z. B. PDFs der Deutschen Krebshilfe) sind urheberrechtlich geschützt. Eine öffentliche Bereitstellung dieser Texte in einer Datenbank ist ohne explizite Genehmigung nicht erlaubt.
- **Medizinische Verantwortung:** Ein KI-System, das medizinische Fragen beantwortet, muss extrem hohe Anforderungen an Korrektheit und Sicherheit erfüllen, um niemanden zu gefährden. Das ist ohne ärztliche Supervision nicht verantwortbar.
- **Datenschutz:** Gesundheitsdaten sind besonders sensibel. Eine lokale, private Installation stellt sicher, dass keine Daten das eigene Gerät verlassen.

Das System ist deshalb als **lokales Werkzeug** konzipiert: Du entscheidest, welche Quellen du einliest, du behältst die Kontrolle über die Daten, und nichts wird irgendwohin hochgeladen. Es ist ein Fundament, das du selbst mit Wissen füllen kannst.

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

*   **Empfohlen (für das große Modell `qwen3:14b`):** Eine GPU mit **mindestens 12–16 GB VRAM** (z.B. NVIDIA RTX 3060/4060 Ti 16GB, AMD RX 7800 XT / 9070 XT). Das Modell belegt ca. 13,5 GB VRAM (bei Q4-Quantisierung), läuft auf einer 16-GB-Karte aber flüssig (ca. 45–50 Tokens/Sekunde).
*   **RAM:** Mindestens 16 GB System-RAM.
*   **Lightweight-Alternative (für schwächere PCs):** Wenn du weniger VRAM hast (z.B. 8 GB), kannst du ein kleineres Modell nutzen. **Tipp:** Probiere `qwen3:4b` oder ein deutsches Modell wie **ELMOD-2.7B** (vom Fraunhofer IIS), das speziell für ressourcenbeschränkte Umgebungen entwickelt wurde. Du musst dann in den Skripten den Modellnamen von `qwen3:14b` auf das kleinere Modell ändern.

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
