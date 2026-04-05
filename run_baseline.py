import requests

BASE_URL = "http://127.0.0.1:8000"

# Reset environment
res = requests.post(f"{BASE_URL}/reset")
obs = res.json()

done = False

while not done:
    if obs["avg_aqi"] > 200:
        action = {"type": "factory_shutdown"}
    else:
        action = {"type": "traffic_control"}

    res = requests.post(f"{BASE_URL}/step", json=action)
    data = res.json()

    obs = data["observation"]
    done = data["done"]

    print(obs)

print("Finished")