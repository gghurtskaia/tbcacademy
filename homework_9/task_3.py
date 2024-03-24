from datetime import datetime
input_date = input("შეიყვანეთ თარიღი, მაგალითად: 2024-03-04T11:17:42.000123+04:00 : ")

formatted_date = datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f%z")
timezone = formatted_date.utcoffset().total_seconds() // 3600
final_timezone = str(int(timezone))

if timezone >= 0:
    final_timezone = "+" + final_timezone

final_date = formatted_date.strftime("%d-%m-%Y %H:%M:%S ") + final_timezone
print(f"{input_date}-ის ფორმატირებული თარიღი: {final_date}")
