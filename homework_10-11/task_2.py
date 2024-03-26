import random
import math

n = int(input("შეიყვანეთ 1-ზე მეტი დადებითი მთელი რიცხვი: "))

while n <= 1:
    print("შეყვანილია არასწორი რიცხვი.")
    n = int(input("შეიყვანეთ 1-ზე მეტი დადებითი მთელი რიცხვი: "))

counter = 0

for i in range(n):
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    if math.sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1

x = 4 * counter / n
print(f"x-ის მნიშვნელობა როცა n = {n}, counter {counter}, შედეგი: {x}")
# აქაც, რაც დიდია N-ის მნიშვნელობა, მით უფრო მიახლოებუილია პი-ს მნიშვნელობასთან
