N, S = map(int,input().split())
cars = list(map(int, input().split()))
cars = sorted(cars)
now = 0
result = 0
for i in range(len(cars)):
    if cars[i] + now <= S:
        now += cars[i]
        result += 1
        continue
    break
print(result)