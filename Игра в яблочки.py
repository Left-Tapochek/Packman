from random import randint, choice
 
def create_sides(feld):
    for i in range(len(feld[0])):
        feld[-1][i] = chr(9552)
        feld[0][i] = chr(9552)
    
    for i in range(len(feld)):
        feld[i][0] = chr(9553)
        feld[i][-1] = chr(9553)
    
    feld[0][0] = chr(9556)
    feld[0][-1] = chr(9559)
    feld[-1][0] = chr(9562)
    feld[-1][-1] = chr(9565)
    
def create_sides_in_feld(feld, n, m):
    coordinates_sides = []
    
    for _ in range(4):
        x = randint(1, n - 3)
        y = randint(1, m - 3)
        
        for i in range(1, randint(2, 4)):
            feld[x][i] = chr(9552)
            coordinates_sides.append((x, i))
        feld[x][0] = chr(9568)
            
        for i in range(1, randint(2, 4)):
            feld[i][y] = chr(9553)
            coordinates_sides.append((i, y))
        feld[0][y] = chr(9574)
        
        for i in range(randint(38, m), m - 1):
            feld[x][i] = chr(9552)
            coordinates_sides.append((x, i))
        feld[x][-1] = chr(9571)
        
        for i in range(randint(6, 20),randint(20, 28)):
            feld[x][i] = chr(9552)
            coordinates_sides.append((x, i))
        
        for i in range(randint(6, 11),randint(12, 17)):
            feld[i][y] = chr(9553)
            coordinates_sides.append((i, y))
        
    return coordinates_sides

def all_coordinates(feld):
    coordinates = []
    for i in range(1, len(feld)):
        for j in range(1, len(feld)):
            coordinates.append((i, j))
    return coordinates

def del_coordinates(all_coordinates, coordinates):
    for i in range(len(coordinates)):
        if coordinates[i] not in all_coordinates:
            continue
        else:
            all_coordinates.remove(coordinates[i])

def create_aplles(coordinate, count_apples, feld, m):
    apples = []
    coordinate = coordinate[2 : len(coordinate) - m]
    for _ in range(count_apples):
        x_y = choice(coordinate)
        feld[x_y[0]][x_y[1]] = chr(9679) 
        apples.append(x_y)
        coordinate.remove(x_y)
    return apples

def create_player(coordinate, feld, m):
   coordinate = coordinate[2 : len(coordinate) - m]
   x_y = choice(coordinate)
   feld[x_y[0]][x_y[1]] = chr(9675)
   coordinate.remove(x_y)
   return x_y[0], x_y[1]

def scores(apples_coordinates, x, y, score, feld):
    for i in range(len(apples_coordinates) - 1):
        for j in range(1):
            if x == apples_coordinates[i][j] and y == apples_coordinates[i][j + 1]:
                score += 1
                del apples_coordinates[i]
    return score

def movement_player(feld, x, y, apples_coordinates, n, m, coordinates, count_apples):
    score = 0
    print(f'\nКоличество яблок на поле ({count_apples})\n')
    print_feld(feld)
    flag = True
    apples_coordinates.append((1, 1))
    while score < count_apples:
        step = input('\nВведите ход:\t').lower()
        if step == 'w':
            if x != 1:
                if flag:
                    if (x - 1, y) in coordinates:
                        print_feld(feld)
                        print(x, y)
                        print(f'\nКоличество собранных яблок {score} из {count_apples}')
                        continue
                    else:
                        feld[x][y], feld[x - 1][y] = feld[x - 1][y], feld[x][y]
                        x -= 1
                        score = scores(apples_coordinates, x, y, score, feld) 
                        feld[x + 1][y] = ' '
                        print_feld(feld) 
                        print(f'x = {x} y = {y}')
                else:
                    if (x - 1, y) in coordinates:
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                        print(f'\nКоличество собранных яблок {score} из {count_apples}')
                        continue
                    else:
                        feld[x][y], feld[x - 1][y] = feld[x - 1][y], feld[x][y]
                        x -= 1
                        score = scores(apples_coordinates, x, y, score, feld) 
                        feld[-1][y] = chr(9552)
                        feld[x][y] = chr(9786)
                        feld[x + 1][y] = ' '
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
            else:
                feld[x][y], feld[-2][y] = feld[-2][y], feld[x][y]
                x -= 1
                score = scores(apples_coordinates, x, y, score, feld) 
                x += n - 2
                flag = False
                print_feld(feld)


        elif step == 's':
            if x != n - 2:
                if flag:
                    if (x + 1, y) in coordinates:
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                        print(f'\nКоличество собранных яблок {score} из {count_apples}')
                        continue
                    else:
                        feld[x][y], feld[x + 1][y] = feld[x + 1][y], feld[x][y]
                        x += 1
                        score = scores(apples_coordinates, x, y, score, feld) 
                        feld[x - 1][y] = ' '
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                else:
                    if (x + 1, y) in coordinates:
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                        print(f'\nКоличество собранных яблок {score} из {count_apples}')
                        continue
                    else:
                        feld[x][y], feld[x + 1][y] = feld[x + 1][y], feld[x][y]
                        x += 1
                        score = scores(apples_coordinates, x, y, score, feld) 
                        feld[-1][y] = chr(9552)
                        feld[x][y] = chr(9786)
                        feld[x - 1][y] = ' '
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
            else:
                feld[x][y], feld[1][y] = feld[1][y], feld[x][y]
                x += 1
                score = scores(apples_coordinates, x, y, score, feld) 
                x -= n - 2
                flag = False
                print_feld(feld)
                
        elif step == 'a':
            if y != 1:
                if flag:
                    if (x, y - 1) in coordinates:
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                        print(f'\nКоличество собранных яблок {score} из {count_apples}')
                        continue
                    else:
                        feld[x][y], feld[x][y - 1] = feld[x][y - 1], feld[x][y]
                        y -= 1
                        score = scores(apples_coordinates, x, y, score, feld) 
                        feld[x][y + 1] = ' '
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                else:
                    if (x, y - 1) in coordinates:
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                        print(f'\nКоличество собранных яблок {score} из {count_apples}')
                        continue
                    else:
                        feld[x][y], feld[x][y - 1] = feld[x][y - 1], feld[x][y]
                        y -= 1
                        score = scores(apples_coordinates, x, y, score, feld) 
                        feld[x][-1] = chr(9553)
                        feld[x][y] = chr(9786)
                        feld[x][y + 1] = ' '
                        print_feld(feld)  
                        print(f'x = {x} y = {y}')
            else:
                feld[x][y], feld[x][-2] = feld[x][-2], feld[x][y]
                y -= 1
                score = scores(apples_coordinates, x, y, score, feld) 
                y += m - 2
                flag = False
                print_feld(feld)
                    
        elif step == 'd':
            if y != m - 2:
                if flag:
                    if (x, y + 1) in coordinates:
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                        print(f'\nКоличество собранных яблок {score} из {count_apples}')
                        continue
                    else:
                        feld[x][y], feld[x][y + 1] = feld[x][y + 1], feld[x][y]
                        y += 1
                        score = scores(apples_coordinates, x, y, score, feld)     
                        feld[x][y - 1] = ' '
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                else:
                    if (x, y + 1) in coordinates:
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
                        print(f'\nКоличество собранных яблок {score} из {count_apples}')
                        continue
                    else:
                        feld[x][y], feld[x][y + 1] = feld[x][y + 1], feld[x][y]
                        y += 1
                        score = scores(apples_coordinates, x, y, score, feld)   
                        feld[x][-1] = chr(9553)
                        feld[x][y] = chr(9786)
                        feld[x][y - 1] = ' '
                        print_feld(feld)
                        print(f'x = {x} y = {y}')
            else:
                feld[x][y], feld[x][1] = feld[x][1], feld[x][y]
                y += 1
                score = scores(apples_coordinates, x, y, score, feld) 
                y -= m - 2
                flag = False
                print_feld(feld)
            
        print(f'\nКоличество собранных яблок {score} из {count_apples}')
        
        if score == count_apples:
            print('\nВы собрали все яблочки!\nИгра окончена')
            a = input(f'Для выхода нажмите клавишу Enter')

def print_feld(feld):
    for row in feld:
        for el in row:
            print(el, end = '')
        print()
   
print('Это игра \"Игра в яблочки\"!\
      \n\nПосле запуска игры, появится:\
          \n-Ввод количества яблок, которое нужно будет собрать\
              \n-Игровое поле\n-Координаты нахождение персонажа\
                  \n-Поле для ввода хода\
                  \n-Количество собранных яблок\
                      \n\nПравила игры:\
                          \n-Собрать все яблоки\
                      \n\nУправление персонажем:\
                          \nВ поле \'Введите ход:\' введите:\
                              \nw - верх\
                                  \ns - вниз\
                                      \na - влево\
                                          \nd - вправо')


                                          
ask = input('\nХотите начать игру? Y - да, N - нет:\t').lower()
if ask == 'y':
    n = 20
    m = 45
    count_apples = int(input('\nВведите количество яблок, которые нужно будет собрать:\t'))
    apples = []
    
    feld = [[' ' for _ in range(m)] for _ in range(n)]
    create_sides(feld)
    coordinates_sides = create_sides_in_feld(feld, n, m)
    all_coordinates = all_coordinates(feld)
    del_coordinates(all_coordinates, coordinates_sides)
    coordinates_apples = create_aplles(all_coordinates, count_apples, feld, m)
    del_coordinates(all_coordinates, coordinates_apples)
    coordinates = create_player(all_coordinates, feld, m)
    movement_player(feld, coordinates[0], coordinates[1], coordinates_apples, n, m, coordinates_sides, count_apples)
else:
    print('\nНу я всё-таки старался, прошу попробовать поиграть')
    n = 20
    m = 45
    count_apples = int(input('\nВведите количество яблок, которые нужно будет собрать:\t'))
    apples = []
    
    feld = [[' ' for _ in range(m)] for _ in range(n)]
    create_sides(feld)
    coordinates_sides = create_sides_in_feld(feld, n, m)
    all_coordinates = all_coordinates(feld)
    del_coordinates(all_coordinates, coordinates_sides)
    coordinates_apples = create_aplles(all_coordinates, count_apples, feld, m)
    del_coordinates(all_coordinates, coordinates_apples)
    coordinates = create_player(all_coordinates, feld, m)
    movement_player(feld, coordinates[0], coordinates[1], coordinates_apples, n, m, coordinates_sides, count_apples)
    
