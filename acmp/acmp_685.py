all = list(map(int, input().split()))
result = 0

a = all[0:3]
b = all[3:]

a.sort()
b.sort()

for i in range(3):
    result += a[i] * b[i]

print(result)
    
