all = input().split()
mistake = int(all.pop(0)) - 1
words = all[0]
letters = list(words)

for i in range(len(letters)):
    if i != mistake:
        print(letters[i], end= "")