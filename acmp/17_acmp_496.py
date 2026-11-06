n = int(input())
arr = list(map(int, input().split()))
first = arr[0]
last = arr[n - 1]

arr.append(first)
arr.insert(0, last)

max_val = 0
n += 2

for i in range(1, n - 1):
    cur_val = arr[i] + arr[i - 1] + arr[i + 1]

    if cur_val > max_val:
        max_val = cur_val

print(max_val)
