import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class PlacementBackend:
    def __init__(self):
        # Updated dataset with additional features: Certifications, Internships, Projects
        data = {
            "CGPA": [7.8, 8.0, 9.8, 4.9, 9.7],
            "DSA": [50, 20, 80, 60, 40],
            "Aptitude": [20, 80, 70, 60, 50],
            "Certifications": [1, 3, 5, 0, 4],
            "Internships": [0, 1, 2, 0, 2],
            "Projects": [1, 2, 4, 0, 3],
            "Placed": [0, 1, 1, 0, 1],
        }

        self.df = pd.DataFrame(data)

        # Features and target
        X = self.df[
            ["CGPA", "DSA", "Aptitude", "Certifications", "Internships", "Projects"]
        ]
        y = self.df["Placed"]

        # Train the model
        self.model = RandomForestClassifier()
        self.model.fit(X, y)

    def predict_result(
        self, cgpa, dsa, aptitude, certifications, internships, projects
    ):
        # Make prediction
        result = self.model.predict(
            [[cgpa, dsa, aptitude, certifications, internships, projects]]
        )

        text = ""

        if result[0] == 0:
            text += " Low chance of placement\n\nSuggestions:\n"
            if cgpa < 7.5:
                text += "• Improve CGPA\n"
            if dsa < 50:
                text += "• Solve more DSA problems\n"
            if aptitude < 70:
                text += "• Practice aptitude questions\n"
            if certifications < 3:
                text += "• Complete more certifications\n"
            if internships < 1:
                text += "• Apply for internships\n"
            if projects < 2:
                text += "•  should Work on more projects\n"

        else:
            text = " High chance of placement\n\nNext Focus:\n"
            text += "• Start mock interviews\n"
            text += "• Improve resume\n"
            text += "• Practice HR questions\n"
            text += "• Focus on company-specific coding rounds\n"
            if certifications < 5:
                text += "• Add relevant certifications\n"
            if internships < 2:
                text += "• Gain more internship experience\n"
            if projects < 3:
                text += "• Complete impactful projects\n"

        return text
