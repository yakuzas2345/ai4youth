# app_ready — NOSCAM finalisée (standalone)

Démo Streamlit autonome : `app.py` + dépendances minimales.

## Préparer les modèles (une fois)
```bash
# depuis la racine du projet :
make install && make train
# puis copier les artefacts générés ici :
cp tfidf.joblib model.joblib app_ready/
```
(`*.joblib` sont gitignorés : régénérez-les plutôt que de les commiter.)

## Lancer
```bash
cd app_ready
pip install -r requirements.txt
streamlit run app.py
```
Sans les 2 fichiers `.joblib` dans ce dossier, l'app affiche la procédure au lieu de crasher.
