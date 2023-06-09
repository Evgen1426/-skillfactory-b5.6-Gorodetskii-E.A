def greet():
    print(" Формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def board():
    print()
    print("     0  1  2  ")
    for i, row in enumerate(field):
        row_str = f"  {i}  {'  '.join(row)}  "
        print(row_str)
    print()


def player_turn():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл O!!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    board()
    if count % 2 == 1:
        print(" Ходит X")
    else:
        print(" Ходит 0")

    x, y = player_turn()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        breakS