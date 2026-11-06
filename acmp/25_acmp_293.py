count_firms = int(input())

firms = list(map(int, input().split()))
taxs = list(map(int, input().split()))

max_val = -1
max_num = -1

for i in range(count_firms):
    current_earning = firms[i] / 100 * taxs[i]

    if current_earning > max_val:
        max_val = current_earning
        max_num = i + 1

print(max_num)
