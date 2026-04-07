from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from code import PlacementBackend
from fastapi.staticfiles import StaticFiles
app = FastAPI()
backend = PlacementBackend()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


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
        result = backend.predict_result(
            cgpa, dsa, aptitude, certifications, internships, projects
        )
    except:
        result = "Enter valid values"

    return templates.TemplateResponse(
        "index.html", {"request": request, "result": result}
    )
