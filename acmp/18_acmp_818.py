n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(arr[0])
else:
    print(sum(arr) - n + 1)
