def can_place(image, state, x, y):
    for i in range(y):
        for j in range(x):
            if not check_can_print(image, state, i, j):
                return False
    return True

def check_can_print(image, state, x, y):
    if state[x][y] in statist[image[x][y]]:
        return True
    return False


y, x = map(int, input().split())
image = [input() for _ in range(y)]
state = [input().split() for _ in range(y)]
statist = {"R": ["4","5","6","7"], "G": ["2", "3", "6", "7"], "B": ["1", "3", "5", "7"], ".": ["0", "1", "2", "3", "4", "5", "6", "7"]}

print("YES" if can_place(image, state, x, y) else "NO")
