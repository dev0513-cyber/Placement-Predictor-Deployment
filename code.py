import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


class PlacementBackend:
    def __init__(self):
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

        X = df[
            ["CGPA", "DSA", "Aptitude", "Certifications", "Internships", "Projects"]
        ]
        y = df["Placed"]

        self.model = RandomForestClassifier(n_estimators=10)

        try:
            self.model.fit(X, y)
        except Exception as e:
            print(e)

    def predict_result(
        self, cgpa, dsa, aptitude, certifications, internships, projects
    ):
        try:
            data = np.array(
                [[cgpa, dsa, aptitude, certifications, internships, projects]]
            )
            result = self.model.predict(data)
        except Exception as e:
            return str(e)

        if result[0] == 0:
            return "Low chance of placement"
        else:
            return "High chance of placement"
