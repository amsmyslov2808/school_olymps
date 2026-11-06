n = int(input())

if n == 1:
    print(45)
else:
    # num_start = int("1" + "0" * (n - 1))
    # num_finish = int("9" * n)
    num_start = 10 ** (n - 1)
    num_finish = 10**n - 1

    count_nums = num_finish - num_start + 1

    summa = ((num_start + num_finish) / 2) * count_nums

    print(int(summa))
