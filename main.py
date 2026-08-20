import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="PropFlow AI")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

class ChatMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/chat")
async def chat_response(data: ChatMessage):
    user_text = data.message.lower()
    
    # Intelligent response handling
    if "buy" in user_text or "price" in user_text:
        reply = "We have verified residential and commercial listings available. What budget range are you targeting?"
    elif "rent" in user_text or "list" in user_text:
        reply = "I can help you list your property or connect with verified buyers. Could you share your location?"
    else:
        reply = f"Thank you for reaching out! PropFlow AI has logged your request regarding: '{data.message}'. An agent will connect shortly."
        
    return {"reply": reply}












