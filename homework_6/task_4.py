n = int(input("შეიყვანეთ n (0 < n < 10): "))

if n <= 0 or n >= 10:
    print("შეიყვანეთ სწორი n-ის მნიშვნელობა!")
else:
    i = 1
    while i <= 2 * n - 1:
        j = 1
        while j <= min(i, 2 * n - i):
            print(j, end="")
            j += 1
        print()
        i += 1
