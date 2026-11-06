n = int(input())
i = 1
result = 0
while i <= n:
    if n % i == 0:
        result += i
    i += 1
print(result)

    