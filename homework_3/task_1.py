import math

def power_of_x(x, y):
    return math.pow(x, y)

x = float(input("შეიყვანეთ x: "))
y = float(input("შეიყვანეთ y: "))
result = power_of_x(x, y)
print(f"{x}-ის {y} ხარისხში აყვანით არის: {result}")
