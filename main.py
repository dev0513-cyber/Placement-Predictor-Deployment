from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the trained model
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


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})


@app.post("/", response_class=HTMLResponse)
def predict(
    request: Request,
    cgpa: float = Form(...),
    dsa: int = Form(...),
    aptitude: int = Form(...),
    certifications: int = Form(...),
    internships: int = Form(...),
    projects: int = Form(...),
):
    try:
        result = predict_result(
            cgpa, dsa, aptitude, certifications, internships, projects
        )
    except Exception as e:
        result = f"Error: {e}"

    return templates.TemplateResponse(
        "index.html", {"request": request, "result": result}
    )
