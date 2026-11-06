all = list(map(int, input().split()))

if all[0] >= 94 and all[0] <= 727 and all[1] >= 94 and all[1] <= 727 and all[2] >= 94 and all[2] <= 727:
    print(max(all))
else:
    print("Error")