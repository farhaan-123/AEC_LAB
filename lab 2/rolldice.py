#Simulate Rolling of a Dice

import numpy as np

#Roll a dice n times
Dice = np.random.choice([1,2,3,4,5,6], size=100)

#count the number of times each face appears
counts = [np.sum(Dice == i) for i in range(1, 7)]
probabilities = [count / len(Dice) for count in counts]

#print the probabilities and counts for each face of the dice
for face, probability in zip(range(1, 7), probabilities):
	print(f'Probability of rolling {face}: {probability:.3f}')
	print(f'Count of dice {face}: {counts[face-1]}')
