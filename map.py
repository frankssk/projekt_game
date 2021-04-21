import action as ac
import event as ev
import battle as bt
import creatures as cr

print('заглушка')

start = 0
name = ''
floor = 0

def commandPL(c):
    cube = 0
    if c == '1':
        cube = ac.rollTheDice()
        print(f'Выпало {cube}')
    elif c == '2':
        ac.howPot()
        com = str(input('выбери действие: \n Бросить кубик = 1\n Выбрать зелье = 2\n'))
        while True:
            if com == '1':
                break
            if com == '2':
                break
            else:
                com = str(input('не верная команда\n'))
        cube = commandPL(com)
    elif c == '3':
        ac.inspect()
        com = str(input('выбери действие: \n Бросить кубик = 1\n Выбрать зелье = 2\n'))
        while True:
            if com == '1':
                break
            if com == '2':
                break
            else:
                com = str(input('не верная команда\n'))
        cube = commandPL(com)
    elif c[0] == '4':
        hp = battleMod(c[1])
        if hp == 'dead':
            return hp
        elif hp == 'life':
            return hp
        else:
            com = str(input('выбери действие: \n Бросить кубик = 1\n Выбрать зелье = 2\n'))
            while True:
                if com == '1':
                    break
                if com == '2':
                    break
                else:
                    com = str(input('не верная команда\n'))
            cube = commandPL(com)
    elif c == '5':
        cube = ac.reversRollTheDice()
        print(f'Выпало {cube}')
    else:
        print('dff')
    return cube

# готово
def floorOne():
    print('Ты на первом этаже. Всего 100 этажей')
    print('Ты должен бросить кубик \nОн определит, на сколько этажей ты поднимешься')
    command = str(input(' Бросить кубик = "1"\n'))
    while command != '1':
        print('Не-не-не... не то!')
        command = str(input(' Бросить кубик = "1"\n'))

def battleMod(mob):
    mobCom = []
    print('Идет бой!')
    while cr.playerCopy['hp'] > 0:
        if mob['hp'] > 0:
            print(f'ВЫ:     {cr.playerCopy}')
            print(f'Монстр: {mob}')
            com = str(input(' Удар   = 1   Блок    = 2\n Зелье  = 3   сбежать = 4\n'))
            com = bt.commandTrue(com)
            mobCom.append(com)
            mobCom.append(mob)
            bt.commandPLayer(mobCom)
        else:
            print(f"Вы одалели {mob['name']}")
    else:
        print('Вы пали в битве')
        com = str(input('Начнем с начала?: \n Да  = 1\n Нет = 2\n'))
        while True:
            if com == '1':
                hp = 'life'
                return hp
            if com == '2':
                hp = 'dead'
                return hp
            else:
                com = str(input('не верная команда\n'))


while True:
    if floor == 0:
        print('Здраствуй путник. Как тебя зовут?')
        name = str(input('введи свое имя\n'))
        print(f'Привет {name}. Вот и начался твой поход из этого подземелья')
        floor += 1
    elif floor == 1:
        print('Этаж 1')
        floorOne()
        cube = ac.rollTheDice()
        print(f'Выпало {cube}')
        floor += cube
    elif 1 < floor < 100:
        print(f'Этаж {floor}')
        command = ev.eventMap(floor)
        cube = commandPL(command)
        if cube == 'dead':
            break
        elif cube == 'life':
            floor = 1
        else:
            floor += cube
    elif 100 >= floor >= 150:
        print(floor)
        floor = 100
        print('Этаж 100')
        print(f'Поздравляю {name}. Ты выбрался.')
        break
    else:
        print('Попробуй в следующий раз')