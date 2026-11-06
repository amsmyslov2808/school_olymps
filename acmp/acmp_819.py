all = list(map(int, input().split()))

p = all[0] * all[1] * 2 + all[0] * all[2] * 2 + all[1] * all[2] * 2
v = all[0] * all[1] * all[2]

print(p, v)