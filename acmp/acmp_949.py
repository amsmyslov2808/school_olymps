n, a, b = map(int, input().split())
c = 0

for _ in range(n - 1):
    c = b - a
    b = a
    a = c

print(f"{a} {b}")
