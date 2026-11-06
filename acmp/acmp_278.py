a = input()
b = input()

count_exist = 0

for i in a:
    ind = b.find(i)
    if ind != -1:
        b = b[ind + 1 :]
        count_exist += 1
    else:
        break
if len(a) == count_exist:
    print("YES")
else:
    print("NO")
