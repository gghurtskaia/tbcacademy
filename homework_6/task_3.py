import random

# ჩაფიქრებული რიცხვი
computer_number = random.randint(0, 100)

# მცდელობების რაოდენობა
guesses = 0

while guesses < 10:
    user_number = int(input("შეიყვანეთ რიცხვი (0-100): "))
    guesses += 1

    if user_number == computer_number:
        print(f"გამოცნობის მცდელობები:{guesses} - ჩაფიქრებული რიცხვი: {computer_number}. You are a winner.")
        break
    elif user_number > computer_number:
        print("high")
    else:
        print("low")

if guesses == 10:
    print(f"გამოცნობის მცდელობები:{guesses} - ჩაფიქრებული რიცხვი: {computer_number}. Computer is a winner.")
