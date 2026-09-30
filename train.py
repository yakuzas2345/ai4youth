"""Anti-SCAM Flooz Lite - pipeline conforme PDF AI4Youth 2026.
Charge UCI + exemples Togo, EDA, TF-IDF, LogReg vs XGBoost, métriques, sauvegarde modèle.
Reproductible: python train.py
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, f1_score
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "data"

# 1. Collecte
uci = pd.read_csv(DATA / "SMSSpamCollection", sep="\t", header=None, names=["label", "text"])
uci["label"] = uci["label"].map({"ham": 0, "spam": 1})
togo = pd.read_csv(DATA / "togo_examples.csv")
togo["label"] = togo["label"].map({"ham": 0, "spam": 1})
# Oversampling x10 des exemples Togo (30 -> 300) pour forcer l'apprentissage des tokens FR locaux
# Flooz/TMoney/FCFA sinon noyés dans 5574 SMS anglais. Documenté comme gestion du déséquilibre.
togo_aug = pd.concat([togo] * 10, ignore_index=True)
df = pd.concat([uci[["label", "text"]], togo_aug[["label", "text"]]], ignore_index=True)
print(f"Dataset total: {len(df)} | spam={df.label.sum()} ({df.label.mean()*100:.1f}%) | ham={(df.label==0).sum()}")
print(f"Dont Togo: {len(togo)}")

# 2. EDA rapide (chiffres pour notebook + jury)
df["longueur"] = df["text"].str.len()
print(df.groupby("label")["longueur"].describe())
print("Doublons:", df.duplicated().sum())
print("Manquants:", df.isnull().sum().sum())
# Dedup UCI seule, puis ré-ajout Togo x10 (sinon l'oversampling est annulé par drop_duplicates)
uci_dedup = uci.drop_duplicates().reset_index(drop=True)
print(f"UCI apres dedup: {len(uci_dedup)}")
df_clean = pd.concat([uci_dedup[["label", "text"]], togo_aug[["label", "text"]]], ignore_index=True)
df_clean["longueur"] = df_clean["text"].str.len()
print(f"Apres dedup UCI + Togo x10: {len(df_clean)}")

# Graphiques EDA
plt.figure()
sns.histplot(data=df_clean, x="longueur", hue="label", bins=50)
plt.title("Longueur SMS ham(0) vs spam(1)")
plt.savefig(BASE / "eda_longueur.png")
plt.close()

cm_data = df_clean[["label", "longueur"]].corr()
plt.figure()
sns.heatmap(cm_data, annot=True)
plt.title("Correlation label-longueur")
plt.savefig(BASE / "eda_correlation.png")
plt.close()

# 3. Split train/val/test 70/15/15 stratifié
X_temp, X_test, y_temp, y_test = train_test_split(
    df_clean["text"], df_clean["label"], test_size=0.15, random_state=42, stratify=df_clean["label"])
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.1765, random_state=42, stratify=y_temp)  # ~15% total
print(f"Train {len(X_train)} / Val {len(X_val)} / Test {len(X_test)}")

# 4. Preprocessing TF-IDF
vec = TfidfVectorizer(lowercase=True, ngram_range=(1, 2), max_features=8000)
Xtr = vec.fit_transform(X_train)
Xv = vec.transform(X_val)
Xte = vec.transform(X_test)

# 5. Modèle A: Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(Xtr, y_train)
pv_lr = lr.predict(Xv)
print("=== LogisticRegression VAL ===")
print(classification_report(y_val, pv_lr, target_names=["ham", "spam"]))

# 6. Modèle B: XGBoost
xgb = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1,
                    subsample=0.9, colsample_bytree=0.9, eval_metric="logloss", random_state=42)
xgb.fit(Xtr, y_train)
pv_xgb = xgb.predict(Xv)
print("=== XGBoost VAL ===")
print(classification_report(y_val, pv_xgb, target_names=["ham", "spam"]))

# 7. Choix meilleur (F1 spam) + eval TEST
f1_lr = f1_score(y_val, pv_lr, pos_label=1)
f1_xgb = f1_score(y_val, pv_xgb, pos_label=1)
best_name, best_model = ("XGBoost", xgb) if f1_xgb >= f1_lr else ("LogReg", lr)
print(f"Meilleur VAL F1-spam: {best_name} ({max(f1_lr, f1_xgb):.3f})")

pt = best_model.predict(Xte)
print(f"=== {best_name} TEST ===")
print(classification_report(y_test, pt, target_names=["ham", "spam"]))
print("ROC-AUC TEST:", roc_auc_score(y_test, best_model.predict_proba(Xte)[:, 1]))

cm = confusion_matrix(y_test, pt)
plt.figure()
sns.heatmap(cm, annot=True, fmt="d", xticklabels=["ham", "spam"], yticklabels=["ham", "spam"])
plt.title(f"Matrice confusion TEST - {best_name}")
plt.savefig(BASE / "confusion_test.png")
plt.close()

# 8. Exemples succès / échecs (exigé PDF)
test_df = pd.DataFrame({"text": X_test.values, "y": y_test.values, "pred": pt}).reset_index(drop=True)
print("--- 3 succès SCAM détectés ---")
print(test_df[(test_df.y == 1) & (test_df.pred == 1)].head(3)["text"].tolist())
print("--- 3 échecs (faux négatifs) ---")
print(test_df[(test_df.y == 1) & (test_df.pred == 0)].head(3)["text"].tolist())

# 9. Sauvegarde reproductible
joblib.dump(vec, BASE / "tfidf.joblib")
joblib.dump(best_model, BASE / "model.joblib")
print("Modèles sauvegardés: tfidf.joblib + model.joblib")

# 10. Test live Togo
demos = [
    "Vous avez recu 50000 FCFA via Flooz. Envoyez votre code PIN pour debloquer",
    "Salut, on se voit au marche Hedzranawoe demain?",
]
Xd = vec.transform(demos)
probas = best_model.predict_proba(Xd)[:, 1]
for txt, p in zip(demos, probas):
    print(f"[{'SCAM' if p > 0.5 else 'HAM'} {p:.2f}] {txt}")
