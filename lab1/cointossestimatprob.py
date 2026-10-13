import matplotlib.pyplot as plt
import numpy as np

result = np.random.choice(["Head","Tail"], size=100)

head = np.sum(result == "Head")

print("Heads:", head)
print("Probability of Heads:", head/100)

trials = [10, 100, 1000, 10000]

for trial in trials:
    result = np.random.choice(["Head","Tail"], size=trial)
    head = np.sum(result == "Head")
    print(f"Trial: {trial}, Heads: {head}, Probability of Heads: {head/trial}")
    
counts = [
    np.sum(result == "Head"),
    np.sum(result == "Tail")
]

plt.bar(["Head", "Tail"], counts)
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.title("Coin Toss Results")
plt.show()