n = int(input("შეიყვანეთ n (0 < n < 10): "))

if n <= 0 or n >= 10:
    print("შეიყვანეთ სწორი n-ის მნიშვნელობა!")
else:
    i = 0
    while i < n:
        j = n - i
        while j > 0:
            print(" ", end="")
            j -= 1

        j = i
        while j >= 0:
            print(j, end="")
            j -= 1

        j = 1
        while j <= i:
            print(j, end="")
            j += 1

        print()
        i += 1
