month = int(input())
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif 3 <= month < 6:
    print("Spring")
elif 6 <= month < 9:
    print("Summer")
elif 9 <= month < 12:
    print("Autumn")
else:
    print("Error")