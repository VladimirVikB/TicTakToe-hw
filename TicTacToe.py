import random


def main():  # Главная функция занускает игру

    print("\n", "X*O*" * 5, "Добро пожаловать в игру - 'Крестики-нолики'.", "*O*X" * 5)
    print("\n", "    Правила игры: Случайным образом определяется кто из игроков", "\n"
            "играет за 'Х', кто играет за 'О'. 'Х' - ходит первым", "\n"
          "Затем поочередно выбираеют поле для установки знака.", "\n"
           "Выигрывает тот игрок который сумеет поставить в ряд 3 знака.", "\n"
          "Если ни одному игроку, не удается занять ряд - обьявляется ничья.", "\n")

    turn = get_First_Pl()  # выводим на экран кто из игроков ходит первым
    print("Первым будет ходить -  " + turn + ", Ваш знак 'Х'" + "\n")


def get_First_Pl():  # Вводим имена игроков и выбираем первый ход
    global player, pl_er1, pl_er2
    pl_er1 = input("Первый игрок введите имя :")
    pl_er2 = input("Второй грок введите имя :")
    if random.randint(0, 1) == 0:
        player = pl_er1
        return f"{pl_er1}"
    else:
        player = pl_er2
        return f"{pl_er2}"


def print_map(field):  # печатаем карту
    rows = len(field)
    print('     0   1   2')
    print("   ----+---+----")
    for r in range(rows):
        print(str(r) + "  | " + field[r][0], "|", field[r][1], "|", field[r][2], "|")
        print("   ----+---+----")
    return field


def start_game(field, player):  # начало игры ввод координат
    global o
    global x
    while True:
        print(f"Игрок { player } введите координаты:")
        row = input("Выберите строку:")
        column = input("Выберите столбец:")
        point = [row, column]
        if len(point) != 2:
            print('Введите две координаты')
            continue
        if not (point[0].isdigit() and point[1].isdigit()):
            print('Введите числа')
            continue
        x, o = map(int, point)
        if not (x >= 0 and x < 3 and o >= 0 and o < 3):
            print('Вышли из диапазона')
            continue
        if field[x][o] != '-':
            print('Клетка занята')
            continue
        break
    return x, o


def terms_of_win(field):# условия для определения победителя
    f_list = []
    print("f", field) # удалить после
    print("\n" "Новый ход")
    for l in field:
        f_list += l
        print("f list", f_list) # удалить после
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]
    indices = set([key for key, val in enumerate(f_list) if val == simb])
    print("indices",  indices) # удалить после
    for p in positions:
        if len(indices & (set(p))) == 3:  # пересечение множеств
            return True
    return False


def start(field): # основной цикл игры
    count = 0
    while True:
        print_map(field)
        if count % 2 == 0:
            player = pl_er1
            simb = "X"
        else:
            player = pl_er2
            simb = "O"
        if count < 9:
            x, o = start_game(field, player)
            field[x][o] = simb

        elif count == 9:
            print('Никто не смог победить - Ничья')
            break
        if terms_of_win(field):
            print(f"Победил:  {player}")
            break
        count += 1



pl_er1 = ""
pl_er2 = ""
player = ""
simb = "X"

field = [['-', '-', '-'],  # первичное наполнение карты
         ['-', '-', '-'],
         ['-', '-', '-']]

main()
print_map(field)
start_game(field, player)
terms_of_win(field)
start(field)
