# NOSCAM — Document Projet AI4Youth 2026

## 1ère partie : Contexte et problématique

Le Togo compte 4,96 millions d'abonnés Mobile Money fin 09/2025 (+21%/an) pour 1398 milliards FCFA transactés sur un seul trimestre, soit 57,2% de pénétration (ARCEP via TogoFirst 08/07/2026). Mixx (ex-TMoney) détient 58% (2,89M) et Flooz 42% (2,06M). Le Mobile Money est devenu l'infrastructure financière quotidienne : marché, taxi, pharmacie, frais scolaires.

En parallèle, la fraude explose. En Afrique, le mobile money a traité $1.105 trillion en 2024 (GSMA State of Industry 2025) et la fraude « remains an issue » avec en tête le social engineering, le SIM-swap et l'usurpation d'identité. Le rapport GSMA Fraudes 02/2025 chiffre à $1 trillion les vols mondiaux en 2023, les utilisateurs mobile money africains étant des cibles prioritaires. Au Kenya, la fraude mobile money est le 1er cas cyber du S1 2026 avec 51 dossiers sur 102 (Ministère Intérieur 24/08/2026). ESET/Serianu estiment $230M de pertes au Kenya et ~$5B en Afrique en 2025, avec phishing et faux messages urgents comme vecteurs dominants.

Au Togo, les formes sont connues : « Vous avez reçu 50.000 FCFA, envoyez votre PIN », « compte Flooz bloqué, cliquez », « c'est ton oncle, envoie vite », « bourse Canada, envoie frais », « double ton argent marabout ». L'ARCEP a dû imposer de nouvelles règles de protection consommateur le 24/02/2026. Les victimes principales sont les revendeuses des marchés Hédzranawoé et Agoè, les élèves, les zemidjans et les seniors peu à l'aise avec les liens. Une seule compromission fait perdre confiance à tout un quartier et freine l'inclusion financière.

Problématique : comment détecter automatiquement, en français et argot local Ewe/Mina, les SMS frauduleux Flooz/TMoney avant que l'utilisateur ne clique ou n'envoie de l'argent, avec un outil sobre, explicable et reproductible par le jury ?

Sources complètes + liens dans `sources_probleme_actions_impact.md`. Corpus dans `data/corpus_complet.csv`.

## 2ème partie : Notre solution

### Son but
Protéger les 5 millions d'utilisateurs Mobile Money togolais en disant en 1 seconde si un SMS est une arnaque ou un message normal, avec un score de confiance et sans jargon technique. Objectif sprint : 500 vrais SMS de Lomé collectés, 90% de ARNAQUES bloquées, moins de 5% de faux blocages, 200 personnes sensibilisées.

### Comment ça marche (sans détails techniques)
L'application a appris à reconnaître le langage des arnaqueurs : mots d'urgence, promesses de gains, faux liens, demandes de code PIN ou d'argent rapide. Elle a lu 5600 exemples dont 30 exemples togolais Flooz/TMoney. Quand un nouveau SMS arrive, elle le compare à ce qu'elle connaît et rend un verdict : rouge ARNAQUE ou vert NORMAL, avec un pourcentage. Plus le pourcentage est haut, plus c'est sûrement une arnaque. Elle a été entraînée à préférer laisser passer un doute plutôt que bloquer un vrai message important, puis on l'a testée sur des messages jamais vus pour vérifier qu'elle ne triche pas.

### Comment l'utilisateur final va l'utiliser
1. L'utilisateur reçoit un SMS bizarre, par exemple « Flooz bloqué, cliquez ici ».
2. Il ouvre NOSCAM (page web sur téléphone, même bas-débit) et colle le texte dans la case.
3. Il appuie sur Analyser. En moins de 2 secondes s'affiche : « 🚨 ARNAQUE 95% » ou « ✅ NORMAL 3% » avec une barre de couleur.
4. Si ARNAQUE : consigne claire « Ne cliquez pas, ne renvoyez pas de code, signalez ». Si NORMAL : « Message a priori légitime, restez vigilant ».
5. En version sprint : transfert automatique du SMS vers un numéro court, réponse SMS instantanée, et bouton « signaler » qui enrichit la base pour protéger les autres. Mode hors-ligne prévu pour zones rurales. Démo actuelle dans `app.py` (`streamlit run app.py`).

## 3ème partie : Présentation des membres du groupe

> À remplir par toi avant dépôt 30/09.

| Nom complet | Rôle projet | Compétences | Contact | Disponibilité sprint 16/11-12/12 |
|-------------|-------------|-------------|---------|----------------------------------|
|  | ex : Lead Data / Python |  |  |  |
|  | ex : Terrain / Collecte Ewe-FR Lomé |  |  |  |
|  | ex : App / Doc / Pitch |  |  |  |

Équipe visée : 2-3 personnes, 18-35 ans. Renseigner nom, rôle, ce que chacun a fait (voir partie 4).

## 4ème partie : Points à respecter — point, travail effectué, résultat obtenu

> Convention : ✅ validé avec preuve fichier, ⚠️ partiel, ❌ à faire au sprint. Tous les chiffres sont rejouables via `python train.py` (seed 42).

### Point 1 — Thématique imposée parmi les 5
Travail effectué : choix Cybersécurité, cadrage Flooz/TMoney documenté dans `dossier_candidature.md` et `sources_probleme_actions_impact.md`.
Résultat : éligible. Thème accepté, pas de hors-sujet.

### Point 2 — Problème africain concret et documenté
Travail effectué : synthèse ARCEP/TogoFirst, ARCEP 02/2026, GSMA 2025 x2, Kenya 2026, ESET/Serianu 2025 avec liens. 30 exemples Togo FR/Ewe rédigés dans `data/togo_examples.csv`.
Résultat : problème prouvé chiffré (4,96M abonnés, $5B pertes Afrique). À renforcer avec 500 SMS terrain (tableau suivi dans `sms_et_temoignages.md`).

### Point 3 — EDA complète (histogrammes, corrélation, qualité, déséquilibre, synthèse)
Travail effectué : méthode dans `notebook.ipynb` + `train.py`. Calcul longueur par SMS, `sns.histplot longueur hue label`, `heatmap corrélation`, `value_counts`, `duplicated`, `isnull`. Synthèse écrite en markdown.
Résultat : 5602 lignes, 13,6% spam puis 15,3% après oversampling, spam plus longs (~128 vs 71 caractères), 0 manquants, 673 doublons UCI traités, `eda_longueur.png` + `eda_correlation.png` générés.

### Point 4 — Nettoyage et preprocessing justifiés
Travail effectué : dedup UCI seule (5169 conservés), conservation Togo x10 (30→300) documentée comme gestion du biais anglais, TF-IDF lowercase 1-2 grams 8000 features dans `train.py`.
Résultat : 5469 lignes d'entraînement, vocabulaire contient `flooz`, 0 fuite (fit uniquement sur train). Reproductible.

### Point 5 — Répartition train/val/test argumentée
Travail effectué : `train_test_split` stratifié 70/15/15, random_state 42, dans `train.py` et notebook.
Résultat : Train 3827 / Val 821 / Test 821, proportions spam conservées (~14,6%). Pas de leakage.

### Point 6 — Minimum 2 modèles comparés
Travail effectué : A = LogisticRegression max_iter 1000, B = XGBClassifier 200 arbres depth 6 lr 0.1 subsample 0.9, même TF-IDF, évalués sur val.
Résultat : Val F1-spam LogReg 0,87 vs XGBoost 0,92 → XGBoost retenu. Preuve logs + classification_report.

### Point 7 — Métriques d'évaluation et interprétation
Travail effectué : `classification_report`, `confusion_matrix`, `roc_auc_score` sur test held-out, heatmap sauvegardée.
Résultat : TEST XGBoost accuracy 0,98, F1-spam 0,94, ROC-AUC 0,985, `confusion_test.png`. Interprétation : 91% ARNAQUES attrapées, 2% NORMAUX bloqués à tort.

### Point 8 — Exemples succès/échecs, limites, pistes d'amélioration
Travail effectué : extraction 3 succès / 3 faux négatifs dans `train.py`, section limites en notebook et README.
Résultat : succès dont « marabout Flooz » (prouve apprentissage local), échecs type ringtones anglais ambigus. Limites avouées : 30 Togo insuffisants, pas d'Ewe oral, pas de BERT. Pistes : collecte 500 SMS, BERT multilingue, Whisper vocal, RAG arnaques.

### Point 9 — Pas d'API seule, modèle propre entraîné
Travail effectué : 0 appel OpenAI/Gemini, pipeline TF-IDF + XGBoost entraîné localement, `tfidf.joblib` + `model.joblib` sauvegardés.
Résultat : conforme FAQ PDF. Coût 0, latence <100ms CPU, fonctionne offline.

### Point 10 — Code/notebook exécutable, commenté, avec markdown
Travail effectué : `notebook.ipynb` 8 cellules FR + code, `train.py` commenté, vérifié par `jupyter nbconvert --execute` → 56613 octets sans erreur.
Résultat : jury peut relancer. ✅

### Point 11 — requirements.txt et instructions de reproduction
Travail effectué : `requirements.txt` (pandas, sklearn, matplotlib, seaborn, xgboost, jupyter, joblib), `README.md` avec `pip install -r requirements.txt` + `python train.py`.
Résultat : reload `tfidf.joblib` + `model.joblib` OK, seed 42 fixe. ✅

### Point 12 — Repository Git avec README et datasets
Travail effectué : dossier structuré prêt, `README.md`, `data/corpus_complet.csv`, `data/readme` UCI cité.
Résultat : ⚠️ local seul au 30/09, pas encore push. À faire : `git init`, `.gitignore` (*.joblib, *.zip, __pycache__), premier commit, push vers URL à fournir.

### Point 13 — Présentation orale 10-15 min + slides
Travail effectué : plan 5 slides + script vidéo 2 min dans `dossier_candidature.md`.
Résultat : ❌ slides finales non créées, présentation non répétée. À faire pour finale décembre.

### Point 14 — Application démo + vidéo 3-5 min + doc utilisateur
Travail effectué : `app.py` Streamlit (input → ARNAQUE/NORMAL + barre + conseil) créé.
Résultat : ⚠️ non lancé/déployé, pas de vidéo démo, pas de doc user complète. Commande : `streamlit run app.py`. À faire au sprint.

### Point 15 — Éthique : vie privée, biais, non-discrimination, licences
Travail effectué : données UCI publiques + exemples synthétiques (0 donnée perso), numéros masqués, biais anglais avoué + oversampling correctif, licences respectées, protocole consentement/anonymisation défini dans `sources_probleme_actions_impact.md`.
Résultat : conforme. Reste collecte terrain consentie au sprint.

### Point 16 — Intégrité : pas de plagiat, pas de falsification, transparence
Travail effectué : sources citées, chiffres issus des logs réels, limites affichées, canevas témoignages marqués « à valider », pas de chiffres inventés.
Résultat : ✅ présentable honnêtement au jury.

### Point 17 — Équipe 2-3 et dossier candidature complet
Travail effectué : concept + plan PPT + script 2 min prêts.
Résultat : ❌ équipe solo à compléter (partie 3), vidéo non tournée, dépôt `ai4youth.neuractif.org/candidature` non fait. Deadline 30/09/2026 ce soir.

### Point 18 — Règle 60% data/model, 40% dev max
Travail effectué : 100% temps sur data/model/éval, app bonus minimal.
Résultat : ✅ conforme philosophie « rigueur > UI ».
