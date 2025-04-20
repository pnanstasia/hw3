from fastapi import FastAPI, HTTPException
import os
import requests

app = FastAPI()

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your api key")

@app.get("/")
def root():
    return {"message": "Business logic for music library"}

@app.get("/health")
def health():
    return {"status": "ok"}

def get_recommend(your_song: str):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-4o",
        "messages": [{"role": "user", "content": f"Recommend songs similar to {your_song}"}],
        "max_tokens": 50
    }
    response = requests.post(OPENROUTER_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No recommendations found")
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to get recommendations")

@app.post("/recommendations")
def recommend_song(your_song: str):
    recommendations = get_recommend(your_song)
    return {"recommendations": recommendations}
