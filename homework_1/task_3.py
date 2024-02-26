side1 = float(input("შეიყვანეთ სამკუთხედის პირველი გვერდის სიგრძე: "))
side2 = float(input("შეიყვანეთ სამკუთხედის მეორე გვერდის სიგრძე: "))
side3 = float(input("შეიყვანეთ სამკუთხედის მესამე გვერდის სიგრძე: "))
perimeter = (side1 + side2 + side3)
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print("სამკუთხედის პერმიეტრია:", perimeter)
print("სამკუთხედის ფართობია:", area)