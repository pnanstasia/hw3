from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
music_library = {}
CURRENT_ID = 1

class MusicLib(BaseModel):
    name: str
    artist: str
    genre: str
    year: int

@app.get("/")
def root():
    return {"message": "Music Library where you can add and find all your favourite songs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/save")
def save_track(track: MusicLib):
    global CURRENT_ID
    music_library[CURRENT_ID] = {
        'name': track.name,
        'artist': track.artist,
        'genre': track.genre,
        'year':track.year
    }
    CURRENT_ID+=1
    return music_library

@app.get("/get")
def get_tracks():
    return music_library

@app.get("/get/{track_id}")
def get_track_by_id(track_id: int):
    if track_id not in music_library:
        raise HTTPException(status_code=404, detail="Track wasn't found")
    return music_library[track_id]
