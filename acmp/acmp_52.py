ticket = int(input())
number_1 = 0
number_2 = 0

for i in range(6):
    if i <= 2:
        number_1 += ticket % 10
    else:
        number_2 += ticket % 10
    ticket = ticket // 10
if number_1 == number_2:
    print("YES")
else:
    print("NO")