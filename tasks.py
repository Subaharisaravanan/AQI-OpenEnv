def easy_task(state):
    aqi = state["avg_aqi"]

    if aqi < 200:
        return 1.0
    elif aqi < 250:
        return 0.5
    else:
        return 0.0


def medium_task(state):
    aqi = state["avg_aqi"]
    budget = state["budget"]

    if aqi < 150 and budget >= 20:
        return 1.0
    elif aqi < 180:
        return 0.5
    else:
        return 0.0


def hard_task(state):
    aqi = state["avg_aqi"]
    budget = state["budget"]

    score = ((300 - aqi) / 200 + (budget / 100)) / 2
    return max(0.0, min(1.0, score))


def evaluate_all(state):
    return {
        "easy": easy_task(state),
        "medium": medium_task(state),
        "hard": hard_task(state)
    }