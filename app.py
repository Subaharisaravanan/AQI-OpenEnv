from fastapi import FastAPI
from env.environment import AQIEnv

app = FastAPI()

env = AQIEnv()

@app.get("/")
def home():
    return {"message": "AQI API Running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()