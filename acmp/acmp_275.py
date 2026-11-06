N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

for item in numbers:
    if int(str(item), 2) % 7 == 0:
        print("Yes")
    else:
        print("No")