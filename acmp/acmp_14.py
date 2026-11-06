a, b = map(int, input().split())
i = 1
while True:
    current = a * i
    if current % b == 0:
        print(current)
        break
    i += 1