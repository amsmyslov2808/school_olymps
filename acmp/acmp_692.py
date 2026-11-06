number = int(input())
i = 1

if number <= 0:
    result = "NO"
else:
    while i < number:
        i *= 2

if i == number:
    result = "YES"
else:
    result = "NO"

print(result)