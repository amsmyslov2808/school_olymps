letter = ["A", "B", "C", "D", "E", "F", "G", "H"]

# 1. Считываем координаты из консоли
q_str, r_str, k_str = input().split()

# Переводим в удобные координаты [col, row] от 1 до 8
q = [letter.index(q_str[0]) + 1, int(q_str[1])]
r = [letter.index(r_str[0]) + 1, int(r_str[1])]
k = [letter.index(k_str[0]) + 1, int(k_str[1])]

result = 0

# 2. Перебираем все 64 клетки шахматной доски
for col in range(1, 9):
    for row in range(1, 9):
        cell = [col, row]
        
        # Клетка под боком должна быть пустой (на ней не должно стоять фигур)
        if cell == q or cell == r or cell == k:
            continue
            
        # Считаем расстояние по осям X и Y от текущей клетки до каждой фигуры
        dq_x, dq_y = abs(col - q[0]), abs(row - q[1])
        dr_x, dr_y = abs(col - r[0]), abs(row - r[1])
        dk_x, dk_y = abs(col - k[0]), abs(row - k[1])
        
        # Проверяем условия атаки:
        if (
            (dq_x == dq_y or dq_x == 0 or dq_y == 0) or  # Ферзь (диагональ, горизонталь или вертикаль)
            (dr_x == 0 or dr_y == 0) or                  # Ладья (горизонталь или вертикаль)
            ((dk_x == 1 and dk_y == 2) or (dk_x == 2 and dk_y == 1))  # Конь (буквой "Г")
        ):
            result += 1

# 3. Выводим итоговый ответ
print(result)