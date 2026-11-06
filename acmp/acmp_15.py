N = int(input())
map = []
result = 0
for i in range(N):
    map.append([x for x in input().split()])

for i in range(N):
    for j in range(N):
        if map[i][j] == "1":
            result += 1
print(int(result/2))

