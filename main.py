import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="PropFlow AI")

# Force explicit path to the templates directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(BASE_DIR, "templates")

templates = Jinja2Templates(directory=templates_path)

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/health")
def health_check():
    return {"status": "healthy"}





