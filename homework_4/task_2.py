import random

def generate_numbers(n):
    numbers = [random.randint(0, 1000) for _ in range(n)]
    max_number = max(numbers)
    return numbers, max_number

n = int(input("შეიყვანეთ დადებითი მთელი რიცხვი (0 < n < 30): "))

while n <= 0 or n >= 30:
    print("არასწორია! შეიყვანეთ დადებითი მთელი რიცხვი 0-დან 30-ის ჩათვლით.")
    n = int(input("შეიყვანეთ დადებითი მთელი რიცხვი (0 < n < 30): "))
else:
    numbers, max_number = generate_numbers(n)
    print(f"დაგენერირებული რიცხვები: {numbers}")
    print(f"უდიდესი რიცხვი: {max_number}")
