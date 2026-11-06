buttons = input()

current_floor = 0

max_up = 0
max_down = 0


for i in range(len(buttons)):
    if buttons[i] == "1":
        current_floor += 1

        if current_floor > max_up:
            max_up = current_floor

    elif buttons[i] == "2":
        current_floor -= 1

        if current_floor < max_down:
            max_down = current_floor

print(max_up + abs(max_down) + 1)
