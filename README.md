# AQI Mobile Monitoring OpenEnv

## 📌 Description
This environment simulates air pollution control in cities like Chennai.

An AI agent acts as a pollution control officer and takes actions to reduce AQI.

---

## 🎯 Objective
- Reduce AQI
- Manage budget
- Optimize actions

---

## 🔁 API

### Reset
POST /reset

### Step
POST /step

### State
GET /state

### Tasks
GET /tasks

---

## 🧠 Actions

- factory_shutdown
- traffic_control
- public_warning

---

## 📊 Observation

- avg_aqi
- budget
- time

---

## 🧪 Tasks

| Level | Goal |
|------|------|
| Easy | AQI < 200 |
| Medium | AQI < 150 + budget control |
| Hard | Optimize AQI + budget |

---

## 🚀 Run

```bash
python -m uvicorn app:app --reload