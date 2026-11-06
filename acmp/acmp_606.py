section = list(map(int, input().split()))

if section[0] + section[1] > section[2] and section[1] + section[2] > section[0] and section[0] + section[2] > section[1] :
    print("YES")
else:
    print("NO")