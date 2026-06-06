from sklearn.metrics import classification_report, confusion_matrix
import joblib
import pandas as pd

model = joblib.load("best_model.pkl")
data = pd.read_csv("student_data.csv")

X = data.drop("Performance", axis=1)
y = data["Performance"]

predictions = model.predict(X)

print("\nClassification Report\n")
print(classification_report(y, predictions))

print("\nConfusion Matrix\n")
print(confusion_matrix(y, predictions))