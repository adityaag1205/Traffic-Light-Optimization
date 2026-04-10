Here’s a **clean, professional README.md** you can directly paste into your repo.

---

# Traffic Light Optimization using Deep Reinforcement Learning

## Overview

This project implements an adaptive traffic signal control system using Deep Reinforcement Learning (DQN). The system dynamically adjusts traffic signals based on real-time vehicle queues to minimize congestion and maintain balanced traffic flow at an intersection.

---

## Objective

* Reduce total vehicle waiting time
* Balance traffic between directions (NS and EW)
* Avoid unnecessary signal switching

---

## Approach

The problem is modeled as a reinforcement learning task:

* **Agent:** Traffic signal controller
* **Environment:** Simulated intersection with vehicle queues
* **State:** Discretized queue levels (NS, EW) and current signal
* **Actions:**

  * 0 → Keep current signal
  * 1 → Switch signal
* **Reward:** Based on total queue, imbalance, and switching penalty

A Deep Q-Network (DQN) is used to learn the optimal policy.

---

## Key Features

* Adaptive signal control using reinforcement learning
* Real-time traffic simulation (Poisson-based arrivals)
* Balanced handling of traffic across directions
* Minimum green time constraint for realistic behavior
* Live visualization of queues and performance
* Full-stack implementation (Flask backend + React frontend)

---

## Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** PyTorch (DQN)
* **Frontend:** React.js
* **Visualization:** Chart.js
* **Simulation:** NumPy

---

## Project Structure

```
traffic-rl-project/
│
├── backend/
│   ├── app.py
│   ├── environment.py
│   ├── dqn_agent.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│
└── README.md
```

---

## How to Run

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

---

### 2. Frontend

```bash
cd frontend
npm install
npm start
```

---

## How It Works

1. The frontend requests `/step` from the backend
2. The agent selects an action (keep/switch signal)
3. The environment updates traffic conditions
4. A reward is calculated
5. The agent learns using DQN
6. Results are sent back and visualized

---

## Reward Function

```
Reward = -(NS + EW) - 0.5 × |NS - EW| - switching_penalty
```

* Minimizes congestion
* Ensures fairness between directions
* Prevents frequent switching

---

## Results

* Reduction in total queue length
* Balanced traffic flow
* Stable signal switching behavior

---

## Future Improvements

* Multi-intersection traffic systems
* Integration with real-world traffic data
* Adaptive signal duration (variable green time)
* Emergency vehicle prioritization

---

## Screenshot

![Traffic RL Optimisation](https://raw.githubusercontent.com/adityaag1205/Traffic-Light-Optimization/main/image.png)

---

## Author

Aditya Agarwal

---

## License

This project is for academic and educational use.

---
