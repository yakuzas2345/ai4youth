# Dossier candidature AI4Youth 2026 — NOSCAM

## 1. Concept (pour formulaire https://ai4youth.neuractif.org/candidature)
**Titre:** NOSCAM
**Thématique:** Cybersécurité
**Pitch 300 caractères:** Chaque jour des Togolais perdent leur argent via faux SMS Flooz/TMoney. Notre IA détecte les ARNAQUES en français + argot local avec 98% accuracy (XGBoost, F1 0.94). Notebook reproductible + démo live. Objectif sprint: 500 vrais SMS collectés, app SMS gratuite.
**Équipe 2-3:** dev Python + 1 biz/terrain Lomé (à compléter).

## 2. PPT 5 slides (reprendre KALAN design vert)
1. Cover: NOSCAM + Flooz/TMoney + 98% accuracy
2. Problème: screenshots faux SMS, pertes, 0 filtre FR local
3. Solution: colle SMS → ARNAQUE/NORMAL + score + mots suspects. Schema TF-IDF → XGBoost
4. Preuve: matrice confusion, F1 0.94, ROC 0.985, démo live ARNAQUE 1.00 vs NORMAL 0.01
5. Roadmap sprint: collecte 500 SMS, BERT, app Streamlit/SMS, impact 3M users

## 3. Script vidéo pitch 2 min (120s)
0-20s: "Vous avez reçu 50.000 FCFA, envoyez PIN..." — qui n'a pas reçu ça? Au Togo c'est quotidien.
20-50s: Pas de filtre français/Ewe. On a combiné 5500 SMS + 30 exemples Lomé.
50-90s: Démo live: SMS test → ARNAQUE 100%, marché Hédzranawoé → NORMAL. XGBoost 98%, F1 0.94.
90-110s: Pendant hackathon: 500 SMS terrain, modèle vocal, app gratuite.
110-120s: Protégeons Mobile Money. Merci Neuractif. Équipe dispo sprint 16/11-12/12.

## 4. Checklist éligibilité PDF
- [x] Thème Cybersécurité, problème africain
- [x] EDA + 2 modèles comparés + métriques + succès/échecs + limites
- [x] Notebook exécutable + requirements + README + repo
- [x] Reproductible (seed 42)
- [x] Éthique: pas de données perso, exemples synthétiques
- [ ] À faire sprint: collecte terrain consentie, fairness, RAG arnaques
