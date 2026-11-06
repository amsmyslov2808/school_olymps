n = int(input())

answer = 0

if n == 1:
    answer = 4
elif n == 2:
    answer = 7
elif n == 3:
    answer = 10
elif n == 4:
    answer = 12
elif n % 2 == 0:
    count_3 = n // 2
    count_2 = (n - 4) // 2 + 1
    answer = 4 + 3 * count_3 + 2 * count_2
elif n % 2 != 0:
    count_3 = n // 2 + 1
    count_2 = (n - 4) // 2 + 1
    answer = 4 + 3 * count_3 + 2 * count_2

print(answer)
