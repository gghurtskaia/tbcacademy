num = int(input("შემოიტანეთ დადებითი მთელი 11-ზე ნაკლები რიცხვი: "))
while num > 10:
    print("რიცხვი 10-ზე მეტია, სცადეთ ახლიდან.")
    num = int(input("შემოიტანეთ დადებითი მთელი 11-ზე ნაკლები რიცხვი: "))
else:
    martivi = []
    gamkopi = 2
    while num > 1:
        if num % gamkopi == 0:
            martivi.append(gamkopi)
            num //= gamkopi
        else:
            gamkopi += 1

    print("მარტივი გამყოფებია:", *martivi, sep=" ")




