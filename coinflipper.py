# Author: Derek Vaughan
# Coin Toss Simulator (Python Practice)
# Created 7/27/2021

import random

currentSequentialCounter = 0
highestSequentialCounter = 0
previousResult = 0

print("Let's toss some coins! Heads = 0, Tails = 1")
numberOfCoins = int(input("How many coins do you want to flip? "))

print("Number of Coins: " + str(numberOfCoins))

# Loop from 0 - N (N = Number of Coins Entered):
for coin in range(numberOfCoins):
   # Generate a random result (0 = head, 1 = tails) & print it
   randomResult = random.randint(0,1)
   print(randomResult, end="")

   # Check for the case of it being the first coin to assign initial "previousResult":
   if coin == 0:
        previousResult = randomResult
        highestSequentialCounter += 1
        currentSequentialCounter += 1
   # If it is not the first coin flip:
   else:
        # Check if the current coin flip is the same result as the previous one:
        if previousResult == randomResult:
            currentSequentialCounter += 1
            # If the current number of sequential heads or tails exceeds the previous
            # max, reassign to the current count:
            if currentSequentialCounter > highestSequentialCounter:
                highestSequentialCounter = currentSequentialCounter
        # If the current coin flip result is different than the previous result,
        # reset currentSeqentialCounter:
        else:
            currentSequentialCounter = 0

print("\nHighest # of Sequential Heads or Tails: " + str(highestSequentialCounter))
print("Now let's calculate the probabilty of this happening, based upon " + 
       str(numberOfCoins) + " coins being tossed...")

# Calculating probability of the highest number of sequential heads or tails
# Formula: Probability = (Chance of Heads or Tails)^(Highest Number of Sequential Heads or Tails)
# Multiplying by 100 to convert the result to a percentage value
probability = 100*(0.5**highestSequentialCounter)

print("The probabilty of this outcome is: " + str(round(probability, 4)) + "%")