import torch
import torch.nn as nn
import torch.optim as optim
import random

class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 2)
        )

    def forward(self, x):
        return self.net(x)

class DQNAgent:
    def __init__(self):
        self.model = DQN()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.loss_fn = nn.MSELoss()

        self.gamma = 0.9
        self.epsilon = 0.3   # more exploration

    def act(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 1)

        state = torch.FloatTensor(state)
        q_values = self.model(state)
        return torch.argmax(q_values).item()

    def update(self, state, action, reward, next_state):
        state = torch.FloatTensor(state)
        next_state = torch.FloatTensor(next_state)

        q_values = self.model(state)
        next_q = self.model(next_state)

        target = q_values.clone()
        target[action] = reward + self.gamma * torch.max(next_q)

        loss = self.loss_fn(q_values, target.detach())

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        #  epsilon decay
        self.epsilon *= 0.995
        self.epsilon = max(0.05, self.epsilon)