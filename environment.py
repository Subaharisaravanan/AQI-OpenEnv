import random

class AQIEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.aqi = random.randint(200, 300)
        self.budget = 100
        self.time = 0
        return self.state()

    def step(self, action):
        prev_aqi = self.aqi

        if action["type"] == "factory_shutdown":
            self.aqi -= 20
            cost = 10
        elif action["type"] == "traffic_control":
            self.aqi -= 10
            cost = 5
        else:
            cost = 2

        self.budget -= cost
        self.time += 1

        reward = (prev_aqi - self.aqi) - cost * 0.1

        done = self.time >= 20 or self.budget <= 0

        return self.state(), reward, done, {}

    def state(self):
        return {
            "avg_aqi": self.aqi,
            "budget": self.budget,
            "time": self.time
        }