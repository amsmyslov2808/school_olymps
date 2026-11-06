N = int(input())
if N >= 1:
    s = N * (N + 1) // 2
else:
    s = (N + 1) * (2 - N) // 2
print(s)