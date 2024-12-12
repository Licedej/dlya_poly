# №1

def co():
    xy = []
    i = 0
    while i < 1:
        try:
            xy1 = list(map(float, input('Введите координаты (x, y) для первой точки: ').split()))
            if len(xy1) != 2:
                print('Ведите координаты (x, y) для точки')
                continue
            xy.append(xy1)
            xy2 = list(map(float, input('Введите координаты (x, y) для второй точки: ').split()))
            if len(xy2) != 2:
                print('Ведите координаты (x, y) для точки')
                continue
            xy.append(xy2)
            xy3 = list(map(float, input('Введите координаты (x, y) для третий точки: ').split()))
            if len(xy3) != 2:
                print('Ведите координаты (x, y) для точки')
                continue         
            xy.append(xy3)
            y_x = [xy1[1]/xy1[0], xy2[1]/xy2[0], xy3[1]/xy3[0]]
            indes = (y_x.index(min(y_x)))
            if indes == 0:
                print(f'Угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный у точки с координатой ({xy[0][0]}, {xy[0][1]})')
            elif indes == 1:
                print(f'Угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный у точки с координатой ({xy[1][0]}, {xy[1][1]})')
            elif indes == 2:
                print(f'Угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный у точки с координатой ({xy[2][0]}, {xy[2][1]})')
            i += 1
        except ValueError:
            print('Вводите коректные числа')
co()


# №2

def check(n):
    try:
        n = int(n)
        if n >= 0:
            return 1
        elif n < 0:
            return -1
    except ValueError:
        return -1

def main():
    n = input('Введите натуральное число n : ')
    strn = []
    if check(n) == 1:
        n = int(n)
        for i in range(n+1):
            if bin(i)[2:] == bin(i)[2:][::-1]:
                strn.append(str(i))
        print(f'Числа палиндромы от 0 до {n} : ', ', '.join(strn))
    elif check(n) == -1:
        print('Вводите НАТУРАЛЬНОЕ число. ')
main()