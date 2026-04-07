from environment import AQIEnv

env = AQIEnv()

def reset():
    return env.reset()

def step(action):
    return env.step(action)

def get_state():
    return env.state()