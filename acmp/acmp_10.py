A, B, C, D = map(int, input().split())
 
roots = []
for x in range(-100, 101):
    if A * x**3 + B * x**2 + C * x + D == 0:
        roots.append(x)
 
print(" ".join(map(str, roots)))