all = list(map(int, input().split()))

result = ((all[2] - all[0]) ** 2 + (all[3] - all[1]) ** 2) ** (1/2)

print(result) 
