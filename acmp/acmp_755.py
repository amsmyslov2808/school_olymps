all = list(map(int,input().split()))

if all[0] + all[1]  - all[2] >= 0:
    print((all[0] + all[1]) - all[2])
else:
    print("Impossible") 