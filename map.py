import action as ac
import event as ev
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
        elif hp == 'escaped':
            cube = ac.reversRollTheDice()
            print(f'Выпало {cube}')
            return cube
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
        return cube
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
    print('Идет бой!')
    while cr.playerCopy['hp'] > 0:
        if mob['hp'] > 0:
            mobCom = []
            print(f'ВЫ:     {cr.playerCopy}')
            print(f'Монстр: {mob}')
            com = str(input(' Удар   = 1   Блок    = 2\n Зелье  = 3   сбежать = 4\n'))
            com = commandTrue(com)
            if com == '4':
                hp = 'escaped'
                return hp
            else:
                mobCom.append(com)
                mobCom.append(mob)
                commandPLayer(mobCom)
        else:
            print(f"Вы одалели {mob['name']}")
            break
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


def commandTrue(com):
    while True:
        if com == '1':
            return com
        if com == '2':
            return com
        if com == '3':
            return com
        if com == '4':
            return com
        else:
            com = str(input('не верная команда\n'))


def commandPLayer(mobCom):
    if mobCom[0] == '1':
        attack(mobCom[1])
        if mobCom[1]['hp'] > 0:
            attackMob(mobCom[1])
    elif mobCom[0] == '2':
        bloked(mobCom[1])
        if mobCom[1]['hp'] > 0:
            blokedMob(mobCom[1])
    elif mobCom[0] == '3':
        ac.howPot()
    elif mobCom[0] == '4':
        commandPL(mobCom)


def attackMob(mob):
    cr.playerCopy['hp'] = cr.playerCopy['hp'] - mob['dmg']
    return cr.playerCopy['hp']


def attack(mob):
    mob['hp'] = mob['hp'] - cr.playerCopy['dmg']
    return mob['hp']


def bloked(mob):
    mob['hp'] = mob['hp'] - dmgblok(cr.playerCopy['dmg'], mob['blok'])
    return mob['hp']


def blokedMob(mob):
    cr.playerCopy['hp'] = cr.playerCopy['hp'] - dmgblok(mob['dmg'], cr.playerCopy['blok'])
    return cr.playerCopy['hp']


def dmgblok(dmg, blok):
    damage = dmg - blok
    if damage < 0:
        damage = 0
        return damage
    return damage


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
            cr.playerCopy = cr.player.copy()
        floor += cube
        if floor <= 0:
            floor = 1
    else:
        print(floor)
        floor = 100
        print('Этаж 100')
        print(f'Поздравляю {name}. Ты выбрался.')
        break
