n = int(input())
i = 0

count_1 = 0
count_0 = 0
while i < n:
    current_monetka = int(input())

    if current_monetka == 0:
        count_0 += 1
    elif current_monetka == 1:
        count_1 += 1

    i += 1

print(min(count_0, count_1))
