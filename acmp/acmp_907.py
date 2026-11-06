w, h, r = map(int, input().split())

d = r * 2

if d <= w and d <= h:
    print("YES")
else:
    print("NO")
