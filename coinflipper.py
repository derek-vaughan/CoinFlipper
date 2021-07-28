import random

numberOfCoins = int(input("How many coins? "))

print("Number of Coins: " + str(numberOfCoins))

for coin in range(numberOfCoins):
    print(random.randint(0,1))


