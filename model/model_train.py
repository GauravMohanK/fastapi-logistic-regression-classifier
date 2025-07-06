from ucimlrepo import fetch_ucirepo
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib, os

iris = fetch_ucirepo(id=53)
X = iris.data.features
y = iris.data.targets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = LogisticRegression()

clf.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
joblib.dump(clf, "model/logreg_model.pkl")
print("Model saved")

