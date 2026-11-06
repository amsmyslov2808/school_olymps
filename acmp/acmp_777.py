all = list(map(int, input().split()))

if all[1] > all[0]:
    print(all[1] - all[0])
else:
    print((12 - all[0]) + all[1])