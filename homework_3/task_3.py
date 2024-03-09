import random

suits = ['♣', '♦', '♥', '♠']
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

def print_random_card():
    suit = random.choice(suits)
    rank = random.choice(ranks)
    card = rank + suit
    print("შემთხვევითი ბანქო: ", card)

print_random_card()
