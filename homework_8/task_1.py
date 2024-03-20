input_string = input("შეიყვანეთ სტრიქონი: ")
result = ""
for i in range(len(input_string)):
    if i % 2 == 0 and input_string[i] != 'e':
        result += input_string[i]
print(f"შეყვანილი სტრიქონის ლუწი ინდექსების სიმბოლოები გარდა 'e'-სიმბოლოსი: {result}")
