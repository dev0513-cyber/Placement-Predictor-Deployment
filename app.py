from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model once
model = joblib.load("model.pkl")

def predict_result(cgpa, dsa, aptitude, certifications, internships, projects):
    data = np.array([[cgpa, dsa, aptitude, certifications, internships, projects]])
    pred = model.predict(data)[0]

    if pred == 1:
        text = "High chance of placement\n\nNext Focus:\n"
        text += "• Start mock interviews\n• Improve resume\n• Practice HR questions\n• Focus on company-specific coding rounds\n"
        if certifications < 5:
            text += "• Add relevant certifications\n"
        if internships < 2:
            text += "• Gain more internship experience\n"
        if projects < 3:
            text += "• Complete impactful projects\n"
    else:
        text = "Low chance of placement\n\nSuggestions:\n"
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
            text += "• Work on more projects\n"
    return text

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            cgpa = float(request.form["cgpa"])
            dsa = int(request.form["dsa"])
            aptitude = int(request.form["aptitude"])
            certifications = int(request.form["certifications"])
            internships = int(request.form["internships"])
            projects = int(request.form["projects"])
            result = predict_result(cgpa, dsa, aptitude, certifications, internships, projects)
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
