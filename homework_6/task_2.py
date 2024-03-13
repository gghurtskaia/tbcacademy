a=input("write your password: ")
tries = 1
for a in range (1, 5):
    if a!=("gamishvi"):
        print ("ver gamoxval")
        a=input("write your password: ")
        tries +=1
        if tries==5:
            break
if tries >5:
    print("Blocked")
else:
    print ("Welcome back")