word = input("შეიყვანეთ სიტრიქონი: ")

lutsi = len(word) % 2 == 0

index = 0
if lutsi:
    print("შუა ორი ასო:", word[int(len(word)/2) - 1], word[int(len(word)/2)])
else:
    while index < 5:
        print("პირველი ასო:", word[0])
        print("შუა ასო:", word[int(len(word)/2)])
        print("ბოლო ასო:", word[-1])
        index += 1
