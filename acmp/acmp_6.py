import os
import time

def main():
    rows_count, cols_count = map(int, input().split())
    grid = [list(input()) for _ in range(rows_count)]

    source_row = source_col = -1
    for row in range(rows_count):
        for col in range(cols_count):
            if grid[row][col] == 'X':
                source_row, source_col = row, col
                break
        if source_row != -1:
            break

    def is_wall(row, col):
        if row < 0 or row >= rows_count or col < 0 or col >= cols_count:
            return True
        return grid[row][col] == '*'

    def mark_cell(row, col, row_dir, col_dir):
        if row == source_row and col == source_col:
            return
        new_symbol = '\\' if row_dir * col_dir > 0 else '/'
        current_symbol = grid[row][col]
        if current_symbol == '.':
            grid[row][col] = new_symbol
        elif (current_symbol == '\\' or current_symbol == '/') and current_symbol != new_symbol:
            grid[row][col] = 'X'

    def trace_ray(row_dir, col_dir):
        corner_row = source_row if row_dir == -1 else source_row + 1
        corner_col = source_col if col_dir == -1 else source_col + 1

        visited = set()

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n'.join(''.join(row) for row in grid))
            time.sleep(0.05)
            state = (corner_row, corner_col, row_dir, col_dir)
            if state in visited:
                return
            visited.add(state)

            forward_row = corner_row - 1 if row_dir == -1 else corner_row
            forward_col = corner_col - 1 if col_dir == -1 else corner_col
            forward_is_wall = is_wall(forward_row, forward_col)

            side1_row = corner_row - 1 if row_dir == -1 else corner_row
            side1_col = corner_col - 1 if -col_dir == -1 else corner_col
            side2_row = corner_row - 1 if -row_dir == -1 else corner_row
            side2_col = corner_col - 1 if col_dir == -1 else corner_col
            side1_is_open = not is_wall(side1_row, side1_col)
            side2_is_open = not is_wall(side2_row, side2_col)

            if not forward_is_wall:
                if not (side1_is_open or side2_is_open):
                    return
            else:
                if side1_is_open and not side2_is_open:
                    col_dir = -col_dir
                elif side2_is_open and not side1_is_open:
                    row_dir = -row_dir
                else:
                    return
                forward_row = corner_row - 1 if row_dir == -1 else corner_row
                forward_col = corner_col - 1 if col_dir == -1 else corner_col

            mark_cell(forward_row, forward_col, row_dir, col_dir)
            corner_row += row_dir
            corner_col += col_dir

    for row_dir, col_dir in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        trace_ray(row_dir, col_dir)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'.join(''.join(row) for row in grid))


main()