n = int(input())
count_slices = 0

if n == 1:
    print(0)
else:
    if n % 2 == 0:
        count_slices = n // 2
    else:
        count_slices = n

    print(count_slices)
