# NOSCAM — Détecteur d'arnaques Mobile Money (Togo)

**Thématique :** Cybersécurité | **Solution :** classifieur ARNAQUE / NORMAL (français + argot local : Flooz, TMoney, FCFA, PIN).
Projet initialement préparé pour AI4Youth 2026, réorienté vers les hackathons IA en ligne (ex. ForgeHacks, track AI + Cybersecurity).

## Résultats (reproductibles)
- Dataset : 5469 SMS (UCI 5169 + 30 exemples Togo x10) | 15,3 % spam
- Split 70/15/15 stratifié, TF-IDF 1-2grams 8000
- **XGBoost TEST : acc 0,98, F1-spam 0,94, ROC-AUC 0,985**
- LogReg TEST : F1-spam 0,87 → XGBoost retenu
- Démo : `[ARNAQUE 1.00] Vous avez recu 50000... Flooz... PIN` / `[NORMAL 0.01] marché Hedzranawoe`

## Prérequis
- Python 3.10+ (`make install` crée un `venv/` et installe tout)
- Données déjà incluses dans `data/` : `SMSSpamCollection` (UCI), `togo_examples.csv` (30 SMS FR/Ewe), `corpus_complet.csv`

## Générer les modèles (`make train`)
```bash
make install   # une seule fois : venv + pip install -r requirements.txt
make train     # ./venv/bin/python train.py
```
`train.py` enchaîne : chargement UCI + Togo (oversampling Togo x10) → dédup → EDA → split stratifié →
TF-IDF → LogReg vs XGBoost (choix au meilleur F1-spam en validation) → éval TEST → sauvegarde.
Artefacts régénérés (gitignorés, ne pas commiter) :
- `tfidf.joblib`, `model.joblib` (vectorizer + meilleur modèle)
- `eda_longueur.png`, `eda_correlation.png`, `confusion_test.png`
- Métriques attendues en console : XGBoost TEST acc ≈ 0,98 / F1-spam ≈ 0,94 / ROC-AUC ≈ 0,985,
  plus 3 succès ARNAQUE, 3 échecs (faux négatifs) et 2 tests live Togo.
Durée indicative : 1 à 3 min sur CPU portable.

## Lancer la démo
```bash
make train            # obligatoire d'abord : crée tfidf.joblib + model.joblib
make app              # ./venv/bin/streamlit run app.py
# ou version finalisée standalone : voir app_ready/README.md
```
L'app charge `tfidf.joblib` + `model.joblib` situés dans son propre dossier.

## Fichiers
- `data/` (datasets), `train.py` (pipeline complet), `notebook.ipynb` (EDA + modèles + métriques)
- `app.py` (démo Streamlit de travail), `app_ready/` (version finalisée standalone)
- `Makefile`, `requirements.txt`
- Les documents de candidature (pitch, script vidéo) sont volontairement **hors git** : usage local uniquement.

## Limites
Dataset EN biaisé, 30 exemples Togo insuffisants → collecter ~500 SMS terrain.
Pistes : BERT multilingue, vocal Whisper, RAG base d'arnaques.
Sources : UCI SMS Spam, exemples propres. Licence : recherche.
