g, l = map(int, input().split())

sum_prostrel = g + l - 1

nG = sum_prostrel - g
nL = sum_prostrel - l

print(f"{nG} {nL}")
