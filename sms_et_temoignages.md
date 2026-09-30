# SMS + Témoignages — Anti-SCAM Flooz Lite

> Fichier chapeau lisible. Corpus machine complet : `data/corpus_complet.csv` (5602 lignes : 5574 UCI + 30 Togo).
> Généré le 30/09/2026. Reproductible : voir `train.py`.

## 1. Stats corpus + SOURCES PRÉCISES
- Total : 5602 | ham 4840 (86.4%) | spam 762 (13.6%)
- **Source A — UCI SMSSpamCollection 2011 (5574 SMS, anglais)** : benchmark académique Almeida, Hidalgo, Yamakami. Fichier d'origine `data/SMSSpamCollection` + licence/origine dans `data/readme` (lignes 1-75). Colonnes d'origine `ham/spam<TAB>texte`. Utilisé tel quel, dedup → 5169. Origine colonne `origine=UCI-2011` dans `data/corpus_complet.csv` lignes 2-5575. Limite : anglais 2011, pas de Flooz/TMoney, pas de français.
- **Source B — Togo synthétique v1 (30 SMS, FR/Ewe, créés le 30/09/2026 par notre équipe)** : PAS collectés terrain. Rédigés à partir des typologies GSMA 2025 (social engineering, impersonation, advance fee) + vécu Lomé (Flooz, TMoney, Mawu, Hédzranawoé, Agoè). Fichier `data/togo_examples.csv` colonnes `label,text,source=togo`. Origine `togo` lignes 5576-5605 dans corpus. Oversampling x10 uniquement à l'entraînement (voir `train.py`), pas dans corpus.
- Fichier assemblé : `data/corpus_complet.csv` colonnes `label(0/1),text,origine` — 5605 lignes avec header.
- Entraînement réel : dedup UCI (5169) + Togo x10 (300) = 5469 (voir `train.py` logs).

## 2. Tous les SMS Togo v1 (30/30 listés)
### SPAM Togo (15)
1. `Vous avez recu 50000 FCFA via Flooz. Envoyez votre code PIN au 1234 pour debloquer`
2. `Felicitations! Votre numero TMoney a gagne 100000 FCFA. Appelez le 90 00 00 00`
3. `Votre compte Flooz est bloque. Cliquez sur http://flooz-tg-bonus.com pour reactiver`
4. `Mawu, envoie vite 20000 FCFA sur ce numero, c'est ton oncle, urgent`
5. `Togocom: votre facture impayee. Reglez sur tmoney-bonus.net sinon suspension`
6. `Bourse Canada 2026: vous etes selectionne. Envoyez 15000 FCFA frais dossier`
7. `Offre d'emploi: salaire 500000 FCFA/mois. Envoyez CNI + 5000 FCFA sur Flooz`
8. `Alerte: transaction suspecte TMoney. Confirmez code OTP sur http://tmoney-secure.tg`
9. `Promo Moov: doublez votre solde. Rechargez 10000 et recevez 20000. Code: 9090`
10. `Ton colis est bloque au Port de Lome. Paie 25000 FCFA sur ce lien pour debloquer`
11. `Je suis un marabout puissant, double ton argent en 1h. Envoie Flooz maintenant`
12. `Fille, envoie ta photo + 10000 FCFA pour casting novelas, gain assure`
13. `Urgence famille: papa est a l'hopital, envoie 30000 FCFA vite sur TMoney`
14. `Loterie nationale: vous avez gagne. Frais retrait 12000 FCFA via Flooz`
15. `Maman, c'est moi, j'ai change de numero. Envoie credit 5000 vite`

### HAM Togo (15)
1. `Salut, on se voit au marche Hedzranawoe demain? Les tomates sont moins cheres`
2. `Papa, j'ai bien recu les 5000 FCFA pour le taxi. Merci beaucoup`
3. `Reunion equipe demain 9h au bureau Djanta Tech Hub. Apporte ton PC`
4. `Le cours de maths 3e chapitre vecteurs est disponible sur Kalan`
5. `Bonsoir, le prix du mais au marche Agoe est 450 FCFA le bol ce matin`
6. `N'oublie pas la CPN demain au centre de sante. Prends le carnet`
7. `Match ce soir? On regarde chez Kofi, apporte le pain`
8. `Ton dossier candidature AI4Youth est bien recu. Bonne chance!`
9. `Wharf: conteneur arrive jeudi. Papiers OK pour dedouanement`
10. `Efo, mi le Hedzranawoe, prix gari 600 FCFA. Viens vite`
11. `Bon courage pour le BAC blanc demain. Revise les nombres reels`
12. `Transfert Flooz 10000 FCFA recu de +228 90 12 34 56. Solde: 45000`
13. `Pharmacie garde dimanche: pharmacie St Joseph, Rue 12 Lome`
14. `Prof: interro maths vendredi, chapitre intervalles. Bonne revision`
15. `Zemidjan dispo? Viens me prendre carrefour Agoe, apres le marche`

Fichier source : `data/togo_examples.csv`

## 3. Échantillon UCI (20/5574, le reste dans corpus_complet.csv)
SPAM types : `Free entry in 2 a wkly comp to win FA Cup final tkts`, `WINNER!! As a valued network customer...`, `URGENT! You have won a 1 week FREE membership...`
HAM types : `Go until jurong point, crazy.. Available only in bugis...`, `Ok lar... Joking wif u oni...`, `U dun say so early hor...`
Voir `data/SMSSpamCollection` + `readme` d'origine + `data/corpus_complet.csv` lignes 1-5574.

## 4. Témoignages (v1 : canevas à valider terrain — NE PAS présenter comme collectés au jury)
> Statut honnête : 0 entretien mené au 30/09. Ci-dessous 6 canevas réalistes issus des typologies GSMA/ESET + vécu Lomé, à confirmer avec consentement écrit pendant sprint. Chaque entretien visé : 10 min, anonyme, photo SMS floutée autorisée.

T1 — Revendeuse Hédzranawoé, 42 ans : « On m'a dit "ton Flooz est bloqué, clique". J'ai cliqué, on m'a pris 18000. Depuis j'ai peur de Flooz. »
T2 — Élève 2nde Agoè, 17 ans : « Faux message "bourse Canada, envoie 15000". Deux amis ont payé. »
T3 — Zemidjan, 28 ans : « Appel "c'est ton oncle, envoie 20000 vite". Voix pressée, j'ai failli envoyer. »
T4 — Retraité, 63 ans : « SMS "TMoney gagne 100000". Je ne sais pas lire les liens, je demande à mon fils maintenant. »
T5 — Boutiquière, 35 ans : « Faux client "colis bloqué Port, paie lien". J'ai perdu une journée de vente à stresser. »
T6 — Étudiant, 22 ans : « Offre emploi "500000/mois, envoie CNI + 5000". C'était pour voler mon identité. »

### Guide d'entretien (10 min, à utiliser tel quel)
1. Avez-vous déjà reçu un SMS/appel bizarre Flooz/TMoney ? Lequel ? (montrer exemples)
2. Avez-vous perdu de l'argent / temps ? Combien ? Qu'avez-vous fait après ?
3. Comment vérifiez-vous aujourd'hui ? Qui vous aide ?
4. Acceptez-vous de partager le SMS anonymisé (numéro masqué) pour la recherche ? [consentement]
5. Testeriez-vous une app qui dit SCAM/HAM avant de cliquer ?

### Tableau suivi terrain (à remplir sprint)
| ID | Lieu | Profil | SMS collecté | Perte FCFA | Consentement | Impact après app |
|----|------|--------|---------------|------------|--------------|------------------|
| T001 | Hédzranawoé | ... | ... | ... | oui/non | ... |
| ... objectif 500 lignes ... | | | | | | |

Objectif sprint 16/11-12/12 : 500 SMS réels anonymisés → corpus v2 → ré-entraînement → mesure : % SCAM bloqués, faux positifs, FCFA évités.
