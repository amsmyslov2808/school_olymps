pos = input().strip()

col = ord(pos[0]) - ord('a') + 1
row = int(pos[1])

moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

result = []

for dc, dr in moves:
    new_col = col + dc
    new_row = row + dr

    if 1 <= new_col <= 8 and 1 <= new_row <= 8:
        result.append(chr(new_col - 1 + ord('a')) + str(new_row))

for move in result:
    print(move)