import datetime

def find_weekday(birth_year, birth_month, birth_day):

    birth_date = datetime.date(birth_year, birth_month, birth_day)
    
    weekday = birth_date.strftime("%A")
    
    return weekday

birth_year = int(input("შეიყვანეთ დაბადების წელი: "))
birth_month = int(input("შეიყვანეთ დაბადების თვე: "))
birth_day = int(input("შეიყვანეთ დაბადების რიცხვი: "))


weekday = find_weekday(birth_year, birth_month, birth_day)
print(f"დაბადების დღეა: {weekday}")
