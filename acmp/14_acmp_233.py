n = int(input())

bridges = list(map(int, input().split()))

index_crash = -1

for i in range(n):
    if bridges[i] <= 437:
        index_crash = i
        break

if index_crash == -1:
    print("No crash")
else:
    print(f"Crash {index_crash+1}")
