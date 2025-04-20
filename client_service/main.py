from fastapi import FastAPI, HTTPException, Header
import os
import requests
from db.database import MusicLib

app = FastAPI()
BUSINESS = "http://localhost:8002"
DB = "http://localhost:8004"
TOKEN = "token"
APP_TOKEN = os.getenv("TOKEN", TOKEN)

@app.get("/")
def root():
    return {"message": "Client Service for music library"}

def verify_token(authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "You are authorized!"}

@app.get("/health")
def health_check():
    try:
        db_health = requests.get(f"{DB}/health").json()
        b_health = requests.get(f"{BUSINESS}/health").json()
        return {
            "database": db_health['status'],
            "business logic": b_health['status']}
    except requests.exceptions.RequestException as e:
        return {"Something went wrong, you have an error": str(e)}

@app.post("/save")
def save_song(track: MusicLib, authorization: str):
    verify_token(authorization)
    requests.post(f"{DB}/save", json={"name" : track.name ,
                                      "artist" : track.artist, 
                                      "genre": track.genre, 
                                      "year": track.year})
    return f"{track.name} was saved"

@app.get("/get")
def all_songs(authorization: str):
    verify_token(authorization)
    response = requests.get(f"{DB}/get")
    return response.json()

@app.get("/get/{track_id}")
def get_song(track_id: int, authorization: str):
    verify_token(authorization)
    response = requests.get(f"{DB}//get/{track_id}", params={"track_id": track_id})
    if not response:
        raise HTTPException(status_code=404, detail="You have no such song in the liabrary")
    return response.json()

@app.get("/recommendations")
def recommend(your_song: str, authorization: str):
    verify_token(authorization)
    response = requests.get(f"{BUSINESS}/recommendations", params={"your_song": your_song})
    return response.json()
