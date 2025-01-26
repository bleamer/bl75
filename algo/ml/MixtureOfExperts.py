import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
def generate_data(n_samples=1000):
    X = np.linspace(-10, 10, n_samples)
    y = np.piecewise(X, [X < 0, X >=0], [lambda x: x**2, lambda x: np.sin(x)])
    return X.reshape(-1,1), y

# Define expert Networks
class Expert(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(1, 10),
            nn.ReLU(),
            nn.Linear(10, 20),
            nn.ReLU(),
            nn.Linear(20, 1)
        )

    def forward(self, x):
        return self.network(x)

# Define Gating Network
class GatingNetwork(nn.Module):
    def __init__(self, n_experts):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(1,10),
            nn.ReLU(),
            nn.Linear(10, n_experts),
            nn.Softmax(dim=1)
        )

    def forward(self,x):
        return self.network(x)
    

# Define Mixture of Experts Model
class MixtureOfExperts(nn.Module):
    def __init__(self, n_experts):
        super().__init__()
        self.experts = nn.ModuleList([Expert() for _ in range(n_experts)])
        self.gating_network = GatingNetwork(n_experts)


    def forward(self, x):
        gating_weights = self.gating_network(x)
        expert_outputs = torch.stack([expert(x) for expert in self.experts], dim = 1)
        output = torch.sum(gating_weights.unsqueeze(2) * expert_outputs, dim = 1)
        return output


def train(model, X_train, y_train, epochs = 10000, lr = 0.0001):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr = lr)
    for epoch in range(epochs):
        model.train()
        inputs = torch.from_numpy(X_train).float()
        targets = torch.from_numpy(y_train).float()
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0) # Gradient clipping
        optimizer.step()
        if (epoch +1) % 1000 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.6f}')

def init_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)
        nn.init.zeros_(m.bias)

# Generate Data
X, y = generate_data()
X = (X - np.mean(X)) / np.std(X)
y = (y - np.mean(y)) / np.std(y)
y = y.reshape(-1, 1)

print(X[:40], y[:40])
X_train, y_train = X[:800], y[:800]
X_test, y_test = X[800:], y[800:]

#initialize and train experts model
n_experts = 5
model = MixtureOfExperts(n_experts)
for expert in model.experts:
    expert.apply(init_weights)
model.gating_network.apply(init_weights)
train(model, X_train, y_train)

# Evaluate the model
model.eval()
with torch.no_grad():
    X_test_tensor = torch.from_numpy(X_test).float()
    predictions = model(X_test_tensor).numpy()

# Plot the results
plt.scatter(X_test, y_test, label='True Data')
plt.scatter(X_test, predictions, label='MoE Predictions')
plt.legend()
plt.show()








import unittest 
class TestExpertNetwork(unittest.TestCase):
    def test_initialization(self):
        expert = Expert()
        self.assertIsInstance(expert, Expert)
    
    def test_gating_initialization(self):
        gating_net = GatingNetwork(n_experts=2)
        self.assertIsInstance(gating_net, GatingNetwork)


    def test_forward_pass(self):
        expert = Expert()
        input_tensor = torch.tensor([[1.0]], dtype=torch.float32)
        output = expert(input_tensor)
        self.assertEqual(output.shape, torch.Size([1,1]))

    def test_forward_pass_moe(self):
        moe_model = MixtureOfExperts(n_experts=2)
        input_tensor = torch.tensor([[1.]], dtype=torch.float32)
        output = moe_model(input_tensor)
        self.assertEqual(output.shape, torch.Size([1,1]))

if __name__ == '__main__':
    unittest.main()






