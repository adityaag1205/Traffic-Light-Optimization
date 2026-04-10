import numpy as np
import random

MAX_QUEUE = 20

#  UPDATED PARAMETERS (balanced & realistic)
ARRIVAL_RATE = 1.2     # reduced from 2 → smoother inflow
SERVICE_RATE = 4       # keeps clearing efficient
MIN_GREEN_TIME = 5     # prevents frequent switching

def discretize(q):
    if q <= 3: return 0
    elif q <= 7: return 1
    return 2

class TrafficEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.ns = random.randint(0, 5)
        self.ew = random.randint(0, 5)
        self.signal = 0
        self.green_time = 0
        return self.get_state()

    def get_state(self):
        return [discretize(self.ns), discretize(self.ew), self.signal]

    def step(self, action):
        prev_signal = self.signal

        # -----------------------------
        # MIN GREEN TIME LOGIC
        # -----------------------------
        if action == 1 and self.green_time >= MIN_GREEN_TIME:
            self.signal = 1 - self.signal
            self.green_time = 0
        else:
            self.green_time += 1

        # -----------------------------
        # CONTROLLED ARRIVALS (FIX)
        # -----------------------------
        new_ns = min(np.random.poisson(ARRIVAL_RATE), 3)
        new_ew = min(np.random.poisson(ARRIVAL_RATE), 3)

        self.ns += new_ns
        self.ew += new_ew

        # -----------------------------
        # SERVICE
        # -----------------------------
        if self.signal == 0:
            self.ns = max(0, self.ns - SERVICE_RATE)
        else:
            self.ew = max(0, self.ew - SERVICE_RATE)

        self.ns = min(self.ns, MAX_QUEUE)
        self.ew = min(self.ew, MAX_QUEUE)

        # -----------------------------
        # IMPROVED REWARD
        # -----------------------------
        total_queue = self.ns + self.ew
        reward = -total_queue

        # balance both directions
        reward -= abs(self.ns - self.ew) * 0.5

        # penalize switching
        if action == 1 and prev_signal != self.signal:
            reward -= 2

        return self.get_state(), reward