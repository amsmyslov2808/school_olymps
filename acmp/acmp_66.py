word = input()
keyboard = "qwertyuiopasdfghjklzxcvbnm"

index = keyboard.index(word)
result = keyboard[(index + 1) % len(keyboard)]
print(result)