import os
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from groq import Groq
from google import genai

app = FastAPI(title="EstateMind AI")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Initialize Dual AI Clients
groq_key = os.getenv("GROQ_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

groq_client = Groq(api_key=groq_key) if groq_key else None
gemini_client = genai.Client(api_key=gemini_key) if gemini_key else None

# Memory store for active document context
document_context = ""

class ChatMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# ROUTE 1: Fast Chat powered by Groq (Llama 3.3)
@app.post("/api/chat")
async def chat_response(data: ChatMessage):
    global document_context
    if not groq_client:
        return {"reply": "EstateMind AI Error: GROQ_API_KEY missing on server."}

    system_prompt = (
        "You are EstateMind AI, a high-converting real estate agent assistant. "
        "Answer questions concisely and professionally."
    )
    
    if document_context:
        system_prompt += f"\nUse this property document knowledge when answering:\n{document_context}"

    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": data.message}
            ],
            temperature=0.6,
            max_tokens=200
        )
        return {"reply": completion.choices[0].message.content}
    except Exception as e:
        return {"reply": f"EstateMind AI Chat Error: {str(e)}"}

# ROUTE 2: Document Processing powered by Google Gemini
@app.post("/api/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    global document_context
    if not gemini_client:
        return JSONResponse({"error": "GEMINI_API_KEY missing on server."}, status_code=400)

    try:
        contents = await file.read()
        
        # Pass document bytes directly to Gemini Flash for extraction & indexing
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                {"mime_type": file.content_type or "application/pdf", "data": contents},
                "Summarize all property specs, prices, terms, and features from this document into key factual bullets for a sales chatbot."
            ]
        )
        
        # Save processed specs into memory context for Groq
        document_context = response.text
        return {"status": "success", "message": "Document processed and linked to EstateMind AI!", "summary": response.text[:200] + "..."}
    except Exception as e:
        return JSONResponse({"error": f"Document Processing Error: {str(e)}"}, status_code=500)












