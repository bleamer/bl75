# Policy Evaluation Algo
# Estimates value function of a given policy
# The value function Vπ(s) estimates the expected return 
# (total reward) from any state s, 
# assuming the agent follows a specific policy π. This process 
# iteratively updates the value function until it converges.

import numpy as np

class PolicyEvaluation:
    def __init__(self, states, actions, transition_probs, rewards, policy, gamma=0.9, theta=1e-6):
        """Initialize Policy Evaluation

        Arguments:
            states -- List of all states
            actions -- List of all actions
            transition_probs -- Transition probabilities P(s'|s,a), in the form:
                {(s,a, s'): proba}
            rewards -- Rewards R(s,a, s') in the form {(s,a,s'): reward}
            policy -- Policy in the form {(s, a): proba}

        Keyword Arguments:
            gamma -- Discount Factor (default: {0.9})
            theta -- Convergence threshold (default: {1e-6})
        """
        
        self.states = states
        self.actions = actions
        self.transition_probs = transition_probs
        self.rewards = rewards
        self.policy = policy
        self.gamma = gamma
        self.theta = theta
        self.value_function = {s: 0. for s in states} # initialize V(s) =0 for all states

    
    def evaluate(self):
        """P
        Perform policy evaluation to compute the value function V(s)
        """
        
        while True:
            delta = 0 # Maximum change in V(s) during an iteration

            new_values = self.value_function.copy()

            for s in self.states:
                v = 0 # accumulate the value  for state s
                for a in self.actions:
                    action_proba = self.policy.get((s,a), 0) # pi(a|s)
                    for s_next in self.states:
                        prob = self.transition_probs.get((s, a, s_next), 0) # P'(s'|s,a)
                        reward = self.rewards.get((s,a,s_next), 0) # R(s,a,s')
                        v += action_proba * prob *(reward+self.gamma * self.value_function[s_next])

                new_values[s] = v
                delta = max(delta, abs(v - self.value_function[s]))
            self.value_function = new_values

            if delta < self.theta:
                break
        return self.value_function
    

states = [ 0, 1, 2]
actions = ['a', 'b']

transition_probs = {
    (0, 'a', 0): .5,
    (0, 'a', 1): .5,
    (1, 'a', 2): 1.,
    (2, 'a', 0): 1,
}

rewards = {
    (0, 'a', 0): 5,
    (0, 'a', 1): 10,
    (1, 'a', 2): 2,
    (2, 'a', 0): 1,
}

policy = {
    (0, 'a'): 1.0, # always take action 'a' in state 0
    (1, 'a'): 1.0, # always take action 'a' in state 1
    (2, 'b'): 1.0, # always take action 'b' in state 2
}


# Run policy evaluation
gamma = 0.9
evaluator = PolicyEvaluation(states, actions, transition_probs, rewards, policy, gamma)

value_function = evaluator.evaluate()

print(" Value Function")
for state, value in value_function.items():
    print(f'V({state}): {value:.2f}')

import matplotlib.pyplot as plt

plt.bar(value_function.keys(), value_function.values(), color='skyblue')
plt.xlabel('States')
plt.ylabel('Value Function')
plt.title('Value Function after Policy Evaluation')
plt.show()