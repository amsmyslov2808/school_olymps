count_cub = int(input())
i = 1

while count_cub > 0:
    count_cub -= i
    i += 1

if count_cub < 0:
    print(i - 2)
else:
    print(i - 1)
    