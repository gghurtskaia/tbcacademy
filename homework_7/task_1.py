n = int(input("შეიყვანეთ რიცხვი: "))

if n == 0:
    print(0)
elif n == 1:
    print("0 1")
else:
    a = 0
    b = 1
    print(a, b, end=" ")

    i = 2
    while i <= n:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        i += 1
