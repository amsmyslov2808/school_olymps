radius = list(map(int, input().split()))

if radius[0] >= radius[1] + radius[2]:
    print("YES")
else:
    print("NO")