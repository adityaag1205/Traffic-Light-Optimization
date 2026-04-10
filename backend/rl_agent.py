import numpy as np
import random

ALPHA = 0.1
GAMMA = 0.9
EPSILON = 0.1

class QAgent:
    def __init__(self):
        self.q = np.zeros((3,3,2,2))

    def act(self, state):
        if random.random() < EPSILON:
            return random.randint(0,1)
        return np.argmax(self.q[state])

    def update(self, s, a, r, s2):
        self.q[s][a] += ALPHA * (
            r + GAMMA * np.max(self.q[s2]) - self.q[s][a]
        )