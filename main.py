import numpy as np
import matplotlib.pyplot as plt
from simulation import play_hand
from strategies import random_strategy, basic_strategy

N = 100000  # Number of simulations

def run_simulation(strategy, label):
    results = np.array([play_hand(strategy) for _ in range(N)])

    ev = np.mean(results)
    win_rate = np.sum(results == 1) / N
    loss_rate = np.sum(results == -1) / N

    print(f"--- {label} Strategy ---")
    print(f"Expected Value per Hand: {ev:.4f}")
    print(f"Win Rate: {win_rate:.4f}")
    print(f"Loss Rate: {loss_rate:.4f}")
    print("-" * 30)

    return np.cumsum(results)

if __name__ == "__main__":
    random_bankroll = run_simulation(random_strategy, "Random")
    basic_bankroll = run_simulation(basic_strategy, "Basic")

    plt.plot(random_bankroll, label="Random Strategy")
    plt.plot(basic_bankroll, label="Basic Strategy")
    plt.xlabel("Number of Hands")
    plt.ylabel("Cumulative Profit")
    plt.title("Bankroll Growth Comparison")
    plt.legend()
    plt.show()
