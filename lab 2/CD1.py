cricket = 60
football = 40
both = 25

#Calculate the probability of each event
probability_football = both / football
probability_cricket = both / cricket

#print the probabilities
print("The probability of a student plays Football given they play Cricket:", f"{probability_cricket*100:.2f}%")
print("The probability of a student plays Cricket given they play Football:", f"{probability_football*100:.2f}%")