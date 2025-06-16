from fastapi import FastAPI, Query
from threading import Thread
import uvicorn
import time

from scent_player import play_scented_track, load_scent_track
from sensorylab_smeller import Smeller

app = FastAPI()
current_time = 0
smeller = Smeller()
track = load_scent_track("example_track.scent")

@app.get("/start")
def start_scent_playback():
    Thread(target=play_scented_track, args=(track, smeller, current_time)).start()
    return {"status": "Started"}

@app.get("/time")
def update_time(ts: int = Query(...)):
    global current_time
    current_time = ts
    return {"current_time": current_time}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)