"""Démo Streamlit Anti-SCAM (bonus Application). streamlit run app.py"""
import streamlit as st
import joblib
from pathlib import Path

BASE = Path(__file__).parent

st.set_page_config(page_title="Anti-SCAM Flooz", page_icon="🛡️")
st.title("🛡️ Anti-SCAM Flooz Lite — Togo")
st.write("Colle un SMS suspect → SCAM / HAM + score. Modèle XGBoost F1 0.94.")

@st.cache_resource
def load():
    vec = joblib.load(BASE / "tfidf.joblib")
    model = joblib.load(BASE / "model.joblib")
    return vec, model

try:
    vec, model = load()
    txt = st.text_area("SMS à analyser", "Vous avez recu 50000 FCFA via Flooz. Envoyez votre code PIN pour debloquer")
    if st.button("Analyser"):
        p = float(model.predict_proba(vec.transform([txt]))[0, 1])
        label = "🚨 SCAM" if p > 0.5 else "✅ HAM"
        st.subheader(f"{label} — {p:.2f}")
        st.progress(p)
        if p > 0.5:
            st.warning("Ne cliquez pas, ne renvoyez pas de code. Signalez au 8000.")
        else:
            st.success("SMS a priori légitime. Restez vigilant.")
except Exception as e:
    st.error(f"Modèle non trouvé. Lancez `python train.py` d'abord. ({e})")
