carousel = int(input())
answer = list(map(int, input().split()))

mark_add = 3
mark = 0

for i in range(carousel):
    if answer[i] == 1:
        mark += mark_add
        mark_add += 1
    else:
        mark_add -= 3
        if mark_add < 3:
            mark_add = 3

print(mark)
