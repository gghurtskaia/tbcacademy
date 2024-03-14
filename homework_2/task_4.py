speed = int(input("შეიყვანეთ ავტომობილის სიჩქარე km/h: "))

if speed >= 120:
        speed=("VERY FAST")
elif speed >= 60:
        speed=("FAST")
elif speed >= 30:
        speed=("moderate")
else:
        speed=("slow")
categorize_speed= speed
print(f"The speed category is: {categorize_speed}")


