import streamlit as st
import subprocess
import os

# 1. Seiten-Konfiguration (Dunkles Design)
st.set_page_config(page_title="Funda-Ment", page_icon="💙", layout="centered")

# 2. Eigenes CSS für den "Hermes/ChatGPT"-Look
st.markdown("""
<style>
    /* Dunkler Hintergrund für die ganze App */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    /* Chat-Eingabe unten schöner machen */
    .stChatInput {
        padding-bottom: 2rem;
    }
    /* Warnbox in der Sidebar */
    .sidebar-warning {
        background-color: #1e1e24;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #ff4b4b;
        font-size: 0.85rem;
        color: #d1d5db;
    }
    /* Entfernt das "Made with Streamlit" Menü oben rechts */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. Sidebar (Wichtige Infos)
with st.sidebar:
    st.title("💙 Funda-Ment")
    st.markdown("""
    <div class="sidebar-warning">
    <b>Wichtiger Hinweis:</b><br><br>
    Dies ist eine geschlossene Beta.<br><br>
    Funda-Ment ist ein rein informatives Recherche-Tool. Es stellt <b>keine Diagnosen</b>, gibt <b>keine Therapieempfehlungen</b> und ersetzt <b>keinen Arztbesuch</b>.<br><br>
    Bitte kläre medizinische Fragen immer mit deinem Ärzteteam.
    </div>
    """, unsafe_allow_html=True)

# Haupttitel
st.title("Wie kann ich dir helfen?")

# Chat-Verlauf initialisieren
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bisherige Nachrichten anzeigen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Eingabefeld
if prompt := st.chat_input("Stelle deine Frage..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Suche in den Quellen..."):
            try:
                env = os.environ.copy()
                env["PYTHONIOENCODING"] = "utf-8"
                
                result = subprocess.run(
                    ["rag", "ask", prompt, "--chat-model", "qwen3:14b"],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    env=env
                )
                
                raw_output = result.stdout
                lines = raw_output.split("\n")
                clean_lines = []
                for line in lines:
                    if "│" in line:
                        parts = line.split("│")
                        if len(parts) > 1:
                            text = parts[1].strip()
                            clean_lines.append(text)
                
                answer = "\n".join(clean_lines)
                
                if not answer.strip():
                    answer = "Ich habe keine Antwort gefunden."
                
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
            except Exception as e:
                st.error(f"Fehler: {e}")