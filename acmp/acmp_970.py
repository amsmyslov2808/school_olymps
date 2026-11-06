all = list(map(int, input().split()))

if all[0] + all[1] == all[2] or all[0] + all[2] == all[1] or all[1] + all[2] == all[0]:
    print("YES")
else:
    print("NO")