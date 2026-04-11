import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    """
    Returns: action index (int)
    """
    if rng is None:
        rng = np.random.default_rng()

    # Roll the dice: if less than epsilon, explore
    if rng.random() < epsilon:
        # Explore: Choose a random action index
        return rng.integers(0, len(q_values))
    else:
        # Exploit: Choose the action with the highest Q-value
        # If there are ties, np.argmax returns the first occurrence
        return np.argmax(q_values)