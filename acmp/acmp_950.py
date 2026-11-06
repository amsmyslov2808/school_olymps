N = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = ""
i = 0
while len(N) > 0:
    if N[i] == "1":
        result += alphabet[i]
        N = N[i+1:]
        i = 0
    else:
        i += 1
print(result)