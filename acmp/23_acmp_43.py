chain = input()
chain += "1"

count_0 = 0
max_count_0 = 0

for i in range(len(chain)):
    if chain[i] == "0":
        count_0 += 1
    else:
        if count_0 > max_count_0:
            max_count_0 = count_0
        count_0 = 0

print(max_count_0)
