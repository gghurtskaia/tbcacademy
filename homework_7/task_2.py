while True:
    num = int(input("Enter number: "))
    if 0 < num <= 1000:
            while num != 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = num * 3 + 1
            print(num)
            break
    else:
        print("შეიყვანეთ რიცხვი 1-დან 1000-მდე.")

