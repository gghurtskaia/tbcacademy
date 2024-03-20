word = input("შეიყვანეთ სიტრიქონი: ")
result = ""
for char in word:
    if char not in 'aeiou':
        result += char

print(f"სიტყვიდან თანხმოვანი კონსონანტის ასოები: {result}")
