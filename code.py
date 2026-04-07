import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dataset
data = {
    "CGPA": [7.8, 8.0, 9.8, 4.9, 9.7],
    "DSA": [50, 20, 80, 60, 40],
    "Aptitude": [20, 80, 70, 60, 50],
    "Certifications": [1, 3, 5, 0, 4],
    "Internships": [0, 1, 2, 0, 2],
    "Projects": [1, 2, 4, 0, 3],
    "Placed": [0, 1, 1, 0, 1],
}

df = pd.DataFrame(data)
X = df[["CGPA", "DSA", "Aptitude", "Certifications", "Internships", "Projects"]]
y = df["Placed"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
