def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def three_divisors(n):
    divisors = find_divisors(n)
    if len(divisors) <= 3:
        return divisors
    else:
        return divisors[-3:]

n = int(input("შეიყვანეთ დადებით მთელი რიცხვი (0 < n < 50): "))
if 0 < n < 50:
    print("სამი გამყოფი:", three_divisors(n))
else:
    print("შეიყვანეთ 0-დან 50-მდე დადებით მთელი რიცხვი.")
