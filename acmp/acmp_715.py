def invert(string: str):
    return "W" if string == "B" else "B"



n, m = map(int, input().split())
result = 0
original = [input() for _ in range(n)]
input()
negative = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if original[i][j] != invert(negative[i][j]):
            result += 1

print(result)


