n = int(input())

watermellons = list(map(int, input().split()))

min_elem = watermellons[0]
max_elem = watermellons[0]

i = 1

while i < n:
    if watermellons[i] < min_elem:
        min_elem = watermellons[i]

    elif watermellons[i] > max_elem:
        max_elem = watermellons[i]

    i += 1

print(f"{min_elem} {max_elem}")
