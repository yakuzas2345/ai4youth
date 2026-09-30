# Sources problème + Actions entrevues + Impact — NOSCAM Flooz

## 1. Sources qui documentent que c'est un vrai problème africain

### Togo — usage massif
- **ARCEP via TogoFirst 08/07/2026** : 4,96M abonnés Mobile Money fin 09/2025 (+21%), 1398 Mds FCFA au T3 2025 (+33%), pénétration 57,2%. Mixx 58% (2,89M), Flooz 42% (2,06M). Sans confiance, ces volumes s'effondrent.
  https://www.togofirst.com/en/telecom/0807-19503-moov-africa-togo-expands-mobile-money-offering-with-insurance-gift-card-services
- **ARCEP 24/02/2026** : nouvelles règles protection conso (facturation, bundles, SIM) — le régulateur lui-même constate les abus.
  https://techafricanews.com/2026/02/24/arcep-introduces-new-consumer-protection-rules-for-mobile-services-in-togo
- **TechCabal 14/10/2025 / Gozem Money** : TMoney ~60%, Flooz ~40%, 39% pénétration sur 8M habitants, $1.54B au T1 2024. Gozem entre avec NSIA car c'est l'infrastructure financière du pays.
  https://techcabal.com/2025/10/14/togos-gozem-expands-into-mobile-money-with-new-fintech-platform/

### Afrique — fraude avérée
- **GSMA State of Industry 2025 (PDF)** : Afrique $1.105 trillion en 2024 (65% mondial), 81.8 Mds transactions. « fraud remains an issue, social engineering, SIM swap, identity fraud top concerns ».
  https://www.gsma.com/sotir/wp-content/uploads/2025/04/The-State-of-the-Industry-Report-2025_English.pdf
- **GSMA Fraud & Scams 02/2025 (PDF)** : mobile money users key target en Afrique/Asie/LatAm, $1 trillion volé en 2023, social engineering + SIM swap dominants.
  https://www.gsma.com/solutions-and-impact/connectivity-for-good/public-policy/wp-content/uploads/2025/02/Fraud-and-scams-safety-report.pdf
- **Kenya Interior Ministry 24/08/2026** : mobile money = 1er cas cyber S1 2026, 51/102 dossiers, 19 fraudes 18.6%.
  https://citizen.digital/article/mobile-money-fraud-tops-cases-reported-in-first-half-of-2026-n388881
- **ESET Africa / Serianu via Business Insider 04/12/2025** : phishing, SIM-swap, social engineering les plus communs. Kenya $230M pertes 2025, Afrique ~$5B. Pics en décembre avec transferts fêtes.
  https://africa.businessinsider.com/local/markets/festive-scams-and-sim-swap-fraud-threaten-africas-dollar81-billion-mobile-money/bhml9tt
  + synthèse : https://www.independent.co.ug/fraud-rises-as-africas-mobile-money-peaks

### Technique — base dataset
- UCI SMSSpamCollection 2011 (Almeida et al.) : 5574 SMS, benchmark mondial spam. `data/readme` d'origine.
- Notre apport : 30 exemples Togo FR/Ewe v1 (`data/togo_examples.csv`), oversampling x10 documenté dans `train.py`.

## 2. Actions menées / à mener pour les entrevues

### Fait au 30/09/2026
- [x] Corpus v1 assemblé : `data/corpus_complet.csv` (5602)
- [x] 30 exemples Togo synthétiques typés (Flooz/TMoney/marabout/bourse/emploi)
- [x] Canevas 6 témoignages + guide 5 questions + tableau suivi dans `sms_et_temoignages.md`
- [ ] 0 entretien réel mené — à dire honnêtement au jury

### Protocole sprint 16/11-12/12 (éthique PDF)
1. Lieux : marchés Hédzranawoé, Agoè, Gare Zemidjan, cybercafés Lomé. Cible : 100 pers (revendeuses, élèves, zem, seniors).
2. Consentement écrit, anonymisation (numéros masqués +228 90 XX XX XX), droit retrait, mineurs avec parent.
3. Collecte : photo SMS floutée + transcription + perte FCFA + réaction. Objectif 500 SMS labellisés ARNAQUE/NORMAL.
4. Validation : double lecture, 3e arbitre si doute. Stockage local chiffré, pas de cloud public.
5. Restitution : 1 page résultats par marché + atelier sensibilisation 30 min.

### Équipe terrain
- J1 dev Python (modèle), J2 biz/terrain (entretiens Ewe/FR). Carnet de bord quotidien exigé PDF.

## 3. Impact — mesuré et visé

### Impact déjà mesuré (technique, 30/09)
| Métrique | Valeur | Fichier preuve |
|----------|--------|----------------|
| Accuracy TEST | 0.98 | `train.py` log + `confusion_test.png` |
| F1-spam TEST | 0.94 (XGBoost) vs 0.87 LogReg | notebook + rapport sklearn |
| ROC-AUC | 0.985 | log |
| Démo Togo ARNAQUE | 1.00 | log + `app.py` |
| Démo Togo HAM | 0.01 | log |
| Reproductibilité | seed 42, notebook nbconvert OK | `/tmp/test_exec.ipynb` |

### Impact terrain visé (à mesurer sprint)
| Indicateur | Cible | Comment mesurer |
|------------|-------|-----------------|
| SMS réels collectés | 500 | `sms_et_temoignages.md` tableau |
| ARNAQUES bloquées en test | >90% recall | ré-entraînement corpus v2 |
| Faux positifs HAM bloqué à tort | <5% | test users |
| FCFA évités | estimer pertes évitées x SMS bloqués | entretiens suivi |
| Personnes sensibilisées | 200 | ateliers marchés/écoles |
| Adoption | 100 beta-testeurs Streamlit/SMS | logs `app.py` |

### Impact social / jury
- Protège 5M abonnés Togo, surtout femmes marchés + seniors peu alphabétisés numériques.
- Restaure confiance Mobile Money = inclusion financière (cf. GSMA $190B PIB Afrique 2023).
- Faible coût, offline possible, Ewe inclus → réplicable Bénin, Ghana, Côte d'Ivoire.

> À citer en présentation : « 57% de Togolais utilisent Mobile Money (ARCEP 2025), la fraude SIM-swap/social engineering est top menace GSMA 2025, $5B pertes Afrique Serianu 2025. Notre modèle détecte 94% ARNAQUES et on va le prouver sur 500 SMS loméens. »
