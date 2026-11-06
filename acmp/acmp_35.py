count_number = int(input())
result = []

for _ in range(count_number):
    n, m = list(map(int, input().split()))
    d = 19 * m + (n + 239) * (n + 366) / 2
    result.append(int(d))

for i in range(len(result)):
    print(result[i])

