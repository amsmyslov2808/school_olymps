flovers = ["G", "C", "V"]
flovers_update = ["G", "C", "V"]

day = int(input())

for _ in range(day):
    flovers[1] = flovers_update[2]
    flovers[2] = flovers_update[1]
    flovers_update.clear()
    for i in range(3):
        flovers_update.append(flovers[i])
    flovers[0] = flovers_update[1]
    flovers[1] = flovers_update[0]
    flovers_update.clear()
    for i in range(3):
        flovers_update.append(flovers[i])
    
for j in range(3):
    print(flovers[j], end="")

    