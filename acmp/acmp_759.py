N, M = map(int, input().split())
jewelry = list(map(int, input().split()))
jewelry = sorted(jewelry)
jewelry.reverse()
result = 0
for i in range(M):
    if jewelry[i] < 0:
        break
    result += jewelry[i]
print(result)
