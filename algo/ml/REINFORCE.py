import numpy as np
import matplotlib.pyplot as plt

# Non parametric implementation of REINFORCE
class Bandit:
    """Bandit or the problem we are trying to solve
    using RL
    """
    def __init__(self, num_actions) -> None:
        self.num_actions = num_actions
        self.true_means =  np.random.normal(0, 1, num_actions)

    def select_action(self, action):
        return np.random.normal(self.true_means[action], 1)
    


# REINFORCE Algorithm
class REINFORCEAgent:
    def __init__(self, num_actions, learning_rate) -> None:
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.policy = np.ones(num_actions) / num_actions

    def select_action(self):
        return np.random.choice(self.num_actions, p = self.policy)
    
    def update_policy(self, action, reward):

        softmax_probs = np.exp(self.policy) / np.sum(np.exp(self.policy))
        baseline  = np.average(reward)
        log_likelihood = -np.log(softmax_probs[action])

        gradient = (reward - baseline) * (softmax_probs)

        # update the policy
        self.policy += self.learning_rate * gradient

def train_bandit(agent, bandit, num_episodes):
    rewards = []

    for episode in range(num_episodes):
        action = agent.select_action()
        reward = bandit.select_action(action)
        agent.update_policy(action, reward)
        
        rewards.append(reward)

    return rewards 



if __name__ =='__main__':
    num_actions = 5
    learning_rate = 0.1
    num_episodes = 1000
    bandit = Bandit(num_actions)
    agent = REINFORCEAgent(num_actions, learning_rate)
    rewards = train_bandit(agent, bandit, num_episodes)


    plt.plot(rewards)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('REINFORCE Algorithm training')

    plt.show()