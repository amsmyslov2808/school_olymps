n = int(input())
array = list(map(int, input().split()))
m = int(input())
pairs = []

for _ in range(m):
    start, finish = map(int, input().split())
    start -= 1
    finish -= 1

    pairs.append([start, finish])


for i in range(m):
    start = pairs[i][0]
    finish = pairs[i][1]

    for k in range(start, finish + 1):
        print(f"{array[k]} ", end="")

    print()
