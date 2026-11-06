home_or_school = input()
skok_poezdok = int(input())
if home_or_school == "Home":
    print("Yes")
else:
    if skok_poezdok % 2 == 1:
        print("Yes")
    else:
        print("No")

