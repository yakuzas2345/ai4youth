"""Démo Streamlit NOSCAM (version finalisée). streamlit run app.py"""
import streamlit as st
import joblib
from pathlib import Path

BASE = Path(__file__).parent

st.set_page_config(page_title="NOSCAM", page_icon="🛡️", layout="centered")
st.title("🛡️ NOSCAM")
st.write("Collez un SMS suspect → **Arnaque** ou **Normal** + score de confiance. Modèle XGBoost F1 0,94.")
st.caption("Exemple : faux SMS Flooz / TMoney. Aucune donnée envoyée, tout tourne en local.")

@st.cache_resource
def load():
    vec = joblib.load(BASE / "tfidf.joblib")
    model = joblib.load(BASE / "model.joblib")
    return vec, model

try:
    vec, model = load()
    txt = st.text_area("SMS à analyser", "Salut, on se voit au marche Hedzranawoe demain?", height=120)
    col1, col2 = st.columns(2)
    with col1:
        analyser = st.button("Analyser", type="primary")
    with col2:
        exemple_normal = st.button("Voir un exemple normal")
    if exemple_normal:
        txt = "Salut, on se voit au marche Hedzranawoe demain?"
        st.info(f"Exemple normal chargé : {txt}")
    if analyser:
        if not txt.strip():
            st.warning("Veuillez d'abord coller un SMS.")
        else:
            p = float(model.predict_proba(vec.transform([txt]))[0, 1])
            label = "🚨 ARNAQUE" if p > 0.5 else "✅ MESSAGE NORMAL"
            st.subheader(f"{label} — confiance : {p:.0%}")
            st.progress(p)
            if p > 0.5:
                st.error("Danger : ne cliquez sur aucun lien, ne renvoyez aucun code PIN ou OTP. Signalez le message au 8000.")
            else:
                st.success("SMS a priori normal. Restez quand même vigilant : ne partagez jamais votre code PIN.")
            with st.expander("Pourquoi ce résultat ?"):
                st.write("Le modèle a appris les mots typiques des arnaques (urgence, gain, Flooz, PIN, lien). Un score proche de 100% = très suspect, proche de 0% = normal.")
    st.divider()
    st.caption("Projet AI4Youth 2026 — Cybersécurité. Modèle local XGBoost, précision test 98%.")
except Exception as e:
    st.error(f"Modèle introuvable. Copiez `tfidf.joblib` et `model.joblib` (générés via `make train` à la racine) dans ce dossier, puis relancez. Détail : ({e})")
