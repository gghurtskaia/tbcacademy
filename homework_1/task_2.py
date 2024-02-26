import datetime

today = datetime.date.today()
year = today.year

name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
birth_year = int(input("შეიყვანეთ თქვენი დაბადების წელი: "))

age = year - birth_year

print("გამარჯობა,", name, surname, "თქვენ ხართ:", age, "წლის")


