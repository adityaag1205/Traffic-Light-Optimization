from flask import Flask, jsonify
from flask_cors import CORS
from environment import TrafficEnv
from dqn_agent import DQNAgent

app = Flask(__name__)
CORS(app)

env = TrafficEnv()
agent = DQNAgent()

state = env.reset()
reward_history = []
step_count = 0   

@app.route("/")
def home():
    return "Traffic RL Backend Running"

@app.route("/step")
def step():
    global state, step_count

    step_count += 1   

    action = agent.act(state)
    next_state, reward = env.step(action)
    agent.update(state, action, reward, next_state)

    state = next_state
    reward_history.append(reward)

    return jsonify({
        "ns": int(env.ns),
        "ew": int(env.ew),
        "signal": int(env.signal),
        "reward": float(reward)
    })

@app.route("/stats")
def stats():
    recent_rewards = reward_history[-100:]

    steps = list(range(
        step_count - len(recent_rewards) + 1,
        step_count + 1
    ))

    return jsonify({
        "rewards": recent_rewards,
        "steps": steps
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)