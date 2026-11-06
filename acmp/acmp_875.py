def one_tick(grid):
    """Один шаг на торе. grid - список списков из 0 и 1."""
    # Рамка: по бокам копии противоположных столбцов, сверху и снизу копии строк
    padded = [[row[-1]] + row + [row[0]] for row in grid]
    padded = [padded[-1]] + padded + [padded[0]]

    new_grid = []
    for i in range(1, len(grid) + 1):
        up, mid, down = padded[i - 1], padded[i], padded[i + 1]
        new_grid.append([
            # s - число живых соседей; клетка живёт, если s == 3 или (s == 2 и она уже жива)    
            1 if (s := u0 + u1 + u2 + m0 + m2 + d0 + d1 + d2) == 3 or (s == 2 and m1) else 0
            for u0, u1, u2, m0, m1, m2, d0, d1, d2 in zip(
                up, up[1:], up[2:],
                mid, mid[1:], mid[2:],
                down, down[1:], down[2:],
            )
        ])
    return new_grid


def main(x, y, tick, get_map):
    grid = [[1 if ch == "*" else 0 for ch in row] for row in get_map]

    for _ in range(tick):
        grid = one_tick(grid)

    return ["".join("*" if cell else "." for cell in row) for row in grid]


y, x, tick = map(int, input().split())
get_map = [input() for _ in range(y)]

for row in main(x, y, tick, get_map):
    print(row)