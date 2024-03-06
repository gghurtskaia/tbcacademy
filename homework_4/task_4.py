def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

n = int(input("შეიყვანეთ დადებითი მთლი რიცხვი (0 <= n < 20): "))

if 0 <= n < 20:
    result = fibonacci(n)
    print(f"{n}-ის ფიბანაჩის მიმდევრობის რიცხვი: {result}")
else:
    print("შეიყვანეთ 20-ზე ნაკლები დადებითი მთლი რიცხვი.")
