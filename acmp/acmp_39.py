def max_elem_with_border(arr, start, stop):
    max_elem = arr[start]
    for i in range(start, stop + 1, 1):
        if arr[i] > max_elem:
            max_elem = arr[i]

    return max_elem


n = int(input())
arr = list(map(int, input().split()))

max_index = -1

summa = 0

last_pos = 0


while max_index < n - 1:
    max_elem = max_elem_with_border(arr, max_index + 1, n - 1)
    max_index = arr.index(max_elem, max_index + 1, n)

    summa += max_elem * (max_index - last_pos + 1)

    last_pos = max_index + 1

print(summa)
