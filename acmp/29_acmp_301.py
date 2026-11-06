S, K = map(int, input().split())

max_num = 0
rem = S
for i in range(K):
    d = min(9, rem)
    max_num = max_num * 10 + d
    rem -= d

first = max(1, S - 9 * (K - 1))
min_num = first
rem = S - first
for i in range(K - 1):
    d = max(0, rem - 9 * (K - i - 2))
    min_num = min_num * 10 + d
    rem -= d

print(max_num, min_num)
