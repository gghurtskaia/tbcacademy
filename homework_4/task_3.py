def find_factors(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

n = int(input("შეიყვანეთ დადებითი რიცხვი (0 < n < 1000): "))

while n <= 0 or n >= 1000:
    print("არასწორია! შეიყვანეთ დადებითი მთელი 1000-ზე ნაკლები რიცხვი .")
    n = int(input("შეიყვანეთ დადებითი რიცხვი (0 < n < 1000): "))

else:
    factors = find_factors(n)
    print(f"{n} რიცხვის გამყოფებია: {factors}")
