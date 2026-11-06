def cute(tile):
    for i in range(3):
        for j in range(3):
            if not check_cube(i, j, tile):
                return False
    return True

def check_cube(x, y, title):
    if title[x][y] == "B" and title[x+1][y] == "B" and title[x][y+1] == "B" and title[x+1][y+1] == "B" or title[x][y] == "W" and title[x+1][y] == "W" and title[x][y+1] == "W" and title[x+1][y+1] == "W":
        return False
    return True
tile = [input() for _ in range(4)]
print("Yes" if cute(tile) else "No")