def draw_tree(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        if i == 0:
            print(spaces + "*" + spaces)
        else:
            branches = "/" * i + "|" + "\\" * i
            print(spaces + branches + spaces)

n = int(input("შეიყვანეთ დადებით მთელი რიცხვი (0 < n < 50): "))
if 0 < n < 50:
    draw_tree(n)
else:
    print("შეიყვანეთ 0-დან 50-მდე დადებით მთელი რიცხვი.")
