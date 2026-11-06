count_number = int(input())
all = list(map(int, input().split()))
j = count_number - 1

for i in range(count_number):
    print(all[j], end= " ")
    j -= 1