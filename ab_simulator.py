import pandas as pd
import numpy as np
from pathlib import Path

# Load Transition Matrix
ROOT = Path(__file__).resolve().parent
file = ROOT / "transition_summary.csv"
matrix = pd.read_csv(file)
transition_matrix = (
    matrix
    .pivot(index="count", columns="next_count", values="pct")
    .fillna(0.0)
)

# Sample Next Count Data
def sample_next_count(current_count: str) -> str:
    probs = transition_matrix.loc[current_count]

    next_counts = probs.index.to_list()
    weights = probs.values

    return np.random.choice(next_counts, p=weights)

# Simulate a single at-bat
def simulate_at_bat(start_count: str = "0-0"):
    current = start_count
    pitch_num = 1

    print("\n--- New At-Bat ---")
    print(f"Start count: {current}")

    while True:
        input("\nPress SPACE + Enter to throw next pitch ")

        next_state = sample_next_count(current)

        print(f"Pitch {pitch_num}: {current} → {next_state}")

        if next_state == "New AB" or next_state =="0-0":
            print("\nAt-bat ended.")
            break

        current = next_state
        pitch_num += 1

simulate_at_bat() 
