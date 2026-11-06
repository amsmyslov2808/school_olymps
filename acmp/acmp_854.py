t = list(map(int, input().split()))
mode= input()

if mode == "freeze":
    if t[0] > t[1]:
        print(t[1])
    else:
        print(t[0])
elif mode == "heat":
    if t[0] < t[1]:
        print(t[1])
    else:
        print(t[0])
elif mode == "auto":
    print(t[1])
else:
    print(t[0])
