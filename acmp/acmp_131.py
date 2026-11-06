n = int(input())
pairs = []

for _ in range(n):
    age, gender = map(int, input().split())
    pairs.append([age, gender])

number_max = -1
max_age = -1

for i in range(n):
    if pairs[i][1] == 1:
        if pairs[i][0] > max_age:
            number_max = i + 1
            max_age = pairs[i][0]

print(number_max)
