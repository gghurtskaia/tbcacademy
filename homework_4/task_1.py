import random

def roll_dice(players):
    for i in range(1, players + 1):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print(f"Player {i} rolled: {roll1}, {roll2}")

players = int(input("Enter number of players: "))
roll_dice(players)
