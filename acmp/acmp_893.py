N = int(input())
print(N*(N-1)*(N-2) if N > 2 else 1 if N <= 1 else 2)