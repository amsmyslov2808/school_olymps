N = int(input())
marks = list(map(int, input().split()))
even_marks = []
odd_marks = []
for item in marks:
    if item % 2 == 0:
        even_marks.append(item)
    else:
        odd_marks.append(item)
for item in odd_marks:
    print(item, end=" ")
print()
for item in even_marks:
    print(item, end=" ")
print()
if len(even_marks) > len(odd_marks) or len(even_marks) == len(odd_marks):
    print("YES")
else:
    print("NO")