# +создать генератор произшевствий
# +найдено зелье хп (умерено)
# +найден монстр (умеренно)
# +найден сундук с лутом (редко)
# +упал в яму (очень редко)
# +поднялся по леснице (очень редко)
# +комната отдыха ( на каждом 10 этаже)
# поставить лагерь
# добавить торговца как вариант (на будущее)
# добавить точки реса (на будущее)
# найдено зелье мп (будущее)
# Бросить кубик = 1
# Выпить зелье = 2
# Вступить в бой = 4
# Убежать = 5
# Осмотреть сундук = 3


from random import randint
import creatures


def eventMap(floorPl):
    eventToMap = int(randint(0, 100))

    if floorPl % 10 == 0:
        command = room()
        return command
    else:
        if 0 <= eventToMap < 10:
            command = potHP()
            return command
        elif 10 <= eventToMap < 30:
            command = monster()
            return command
        elif 30 <= eventToMap < 50:
            command = chest()
            return command
        #       elif 90 <= eventToMap < 95:
        #          command = down()
        #        return command
        #       elif 95 <= eventToMap <= 100:
        #         command = up()
        #       return command
        elif 50 <= eventToMap < 60:
            command = camp()
            return command
        else:
            command = empty()
            return command


# не готовые

def Loot():
    i = int(randint(0, 100))
    if 0 <= i < 40:
        print('вы нашли маленькое')
    elif 40 <= i < 75:
        print('вы нашли среднее')
    elif 85 <= i < 95:
        print('вы нашли большое')
    else:
        print('вы нашли свиток')


def down():
    print("Вы упали в яму, и пролетели несколько этажей.\n Кости вроде целы.")
    print('выбери действие: \n Бросить кубик = 1\n Выпить зелье = 2')
    command = str(input())
    while True:
        if command == '1':
            break
        if command == '2':
            break
        else:
            command = str(input('не верная команда\n'))
    return command


def up():
    print('Вы наткнулись на тайный проход, удалось сократить путь!')
    print('выбери действие: \n Бросить кубик = 1\n Выпить зелье = 2')
    command = str(input())
    while True:
        if command == '1':
            break
        if command == '2':
            break
        else:
            command = str(input('не верная команда\n'))
    return command


# готовые

def room():
    print('Вы наткнулись на комнату где можете отдохнуть.\n Ваше здоровье востановилось!')
    print('выбери действие: \n Бросить кубик = 1')
    command = str(input())
    while True:
        if command == '1':
            break
        else:
            command = str(input('не верная команда\n'))
    return command


def camp():
    print('Вы нашли место чей-то стоянки. Оно была брошено давным-давно.\n Может удастя найти что ценное?')
    print('выбери действие: \n Бросить кубик = 1\n Выбрать зелье = 2\n Осмотреть стоянку = 3')
    command = str(input())
    while True:
        if command == '1':
            break
        if command == '2':
            break
        if command == '3':
            break
        else:
            command = str(input('не верная команда\n'))
    return command


def chest():
    print('Вы нашли СУНДУК! Что же там может быть?!')
    print('выбери действие: \n Бросить кубик = 1\n Выпить зелье = 2\n Осмотреть сундук = 3')
    command = str(input())
    while True:
        if command == '1':
            break
        if command == '2':
            break
        if command == '3':
            break
        else:
            command = str(input('не верная команда\n'))
    return command


def potHPLoot():
    i = int(randint(0, 100))
    if 0 <= i < 40:
        print('вы нашли маленькое зелье. Оно востанавливает 20% здоровья.')
        creatures.playerItem['potMin'] = creatures.playerItem['potMin'] + 1
    elif 40 <= i < 75:
        print('вы нашли среднее зелье. Оно востанавливает 50% здоровья.')
        creatures.playerItem['potStand'] = creatures.playerItem['potStand'] + 1
    elif 85 <= i < 95:
        print('вы нашли большое зелье. Оно востанавливает 100% здоровья.')
        creatures.playerItem['potMax'] = creatures.playerItem['potMax'] + 1
    else:
        print('вы нашли свиток воскрешения. Он воскресит вас в случае гибели!')
        creatures.playerItem['scroll'] = creatures.playerItem['scroll'] + 1


def potHP():
    i = int(randint(0, 100))
    if 0 <= i < 40:
        print('вы нашли маленькое зелье. Оно востанавливает 20% здоровья.')
        creatures.playerItem['potMin'] = creatures.playerItem['potMin'] + 1
    elif 40 <= i < 75:
        print('вы нашли среднее зелье. Оно востанавливает 50% здоровья.')
        creatures.playerItem['potStand'] = creatures.playerItem['potStand'] + 1
    elif 85 <= i < 95:
        print('вы нашли большое зелье. Оно востанавливает 100% здоровья.')
        creatures.playerItem['potMax'] = creatures.playerItem['potMax'] + 1
    else:
        print('вы нашли свиток воскрешения. Он воскресит вас в случае гибели!')
        creatures.playerItem['scroll'] = creatures.playerItem['scroll'] + 1
    print('выбери действие: \n Бросить кубик = 1\n Выпить зелье = 2')
    command = str(input())
    while True:
        if command == '1':
            break
        if command == '2':
            break
        if command == '3':
            break
        else:
            command = str(input('не верная команда\n'))
    return command


def empty():
    print('Пустая комната... ')
    print('выбери действие: \n Бросить кубик = 1\n Выбрать зелье = 2')
    command = str(input())
    while True:
        if command == '1':
            break
        if command == '2':
            break
        else:
            command = str(input('не верная команда\n'))
    return command


def monster():
    i = int(randint(0, 100))
    if 0 <= i <= 25:
        print('Вы наткнулись на скелета')
        print(creatures.skeleton)
        mob = creatures.skeleton.copy()
    elif 26 <= i <= 50:
        print('Вы наткнулись на призрака')
        print(creatures.ghost)
        mob = creatures.ghost.copy()
    elif 51 <= i <= 75:
        print('Вы наткнулись на гоблина')
        print(creatures.goblin)
        mob = creatures.goblin.copy()
    elif 76 <= i <= 85:
        print('Вы наткнулись на орка')
        print(creatures.ork)
        mob = creatures.ork.copy()
    else:
        print('Вы наткнулись на троля')
        print(creatures.troll)
        mob = creatures.troll.copy()
    print('выбери действие: \n Вступить в бой = 4\n Убежать (от 10 до 20 шагов назад) = 5')
    c = str(input())
    while True:
        if c == '4':
            command = []
            command.append(c)
            command.append(mob)
            return command
        if c == '5':
            command = '5'
            return command
        else:
            c = str(input('не верная команда\n'))
