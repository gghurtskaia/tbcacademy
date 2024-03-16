num = int(input("Enter number: "))
if 0 <= num < 10000:
    reversed_num = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    temp = num
    sum_of_digits = 0
    while temp > 0:
        sum_of_digits += temp % 10
        temp //= 10

    print(f"შებრუნებული რიცხვი არის: {reversed_num}")
    print(f"ციფრების ჯამია: {sum_of_digits}")
else:
    print("შეიყვანეთ რიცხვი 0-დან 1000-მდე.")
