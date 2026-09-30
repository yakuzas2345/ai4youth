# NOSCAM — AI4Youth 2026

**Catégorie:** Data Science | **Thématique:** Cybersécurité
**Problème Togo:** faux SMS Flooz/TMoney. **Solution:** classifieur ARNAQUE/NORMAL FR + argot local.

## Résultats (reproductibles)
- Dataset: 5469 SMS (UCI 5169 + 30 Togo x10) | 15.3% spam
- Split 70/15/15 stratifié, TF-IDF 1-2grams 8000
- **XGBoost TEST: acc 0.98, F1-spam 0.94, ROC-AUC 0.985**
- LogReg TEST: F1-spam 0.87 → XGBoost retenu
- Démo: `[ARNAQUE 1.00] Vous avez recu 50000... Flooz... PIN` / `[NORMAL 0.01] marché Hedzranawoe`

## Reproduire
```bash
pip install -r requirements.txt
python train.py
# notebook: jupyter notebook notebook.ipynb
# démo: streamlit run app.py
```

## Fichiers
- `data/SMSSpamCollection` (UCI) + `data/togo_examples.csv` (30 FR/Ewe)
- `train.py` (pipeline complet), `notebook.ipynb` (EDA + modèles + métriques)
- `tfidf.joblib`, `model.joblib`, `eda_longueur.png`, `confusion_test.png`
- `app.py` (démo Streamlit), `dossier_candidature.md` (pitch + vidéo 2min)

## Limites (jury)
Dataset EN biaisé, 30 Togo insuffisants → collecter 500 SMS terrain pendant sprint 4 semaines.
Pistes: BERT multilingue, vocal Whisper, RAG base arnaques.

## Équipe
Dev Python. Contact via AI4Youth candidature avant 30/09/2026.
Sources: UCI SMS Spam, exemples propres. Licence: recherche.
