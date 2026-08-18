from fastapi import FastAPI

app = FastAPI(
    title="PropFlow AI",
    description="Real Estate AI Automation API"
)

@app.get("/")
def home():
    return {"status": "success", "message": "PropFlow AI Server is Live!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
