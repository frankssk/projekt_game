# +бросить кубик
# +надеть шмотку
# +снять шмотку
# + использовать зелье
# + использовать свиток
# + бой
# + ударить
# + блокировать
# + бежать
# сколько зелий
# открыть/осмотреть лагерь
import random
from random import randint
import event
import creatures as ac


# command = int(input('выбери команду '))
def putOn():
    print("dff")


def takeOff():
    print("dff")


def scroll():
    print("dff")


# готово

def inspect():
    i = random.randint(1, 100)
    if 0 <= i < 40:
        event.potHPLoot()
    #  elif 40 <= i < 75:
    #     event.Loot()
    else:
        print('Вы ничего не нашли')


def howPot():
    print(
        f'Маленьких: {ac.playerItem["potMin"]} Средних: {ac.playerItem["potStand"]} Больших: {ac.playerItem["potMax"]} Свитки воскрешения(пока не работает): {ac.playerItem["scroll"]}')
    command = str(input(
        'Какое зелье вы хотите использовать?\n Маленькое 10% = 1\n Среднее 50% = 2\n Большое 100% = 3\n Отменить выбор = 4\n'))
    while True:
        if command == '1':
            while ac.playerItem['potMin'] == 0:
                break
            else:
                ac.playerItem['potMin'] = ac.playerItem['potMin'] - 1
                ac.playerCopy['hp'] = ac.playerCopy['hp'] + ((ac.player['hp'] // 100) * 10)
                if ac.playerCopy['hp'] > ac.player['hp']:
                    ac.playerCopy['hp'] = ac.player['hp']
                break
        if command == '2':
            while ac.playerItem['potStand'] == 0:
                break
            else:
                ac.playerItem['potStand'] = ac.playerItem['potStand'] - 1
                ac.playerCopy['hp'] = ac.playerCopy['hp'] + ((ac.player['hp'] // 100) * 50)
                if ac.playerCopy['hp'] > ac.player['hp']:
                    ac.playerCopy['hp'] = ac.player['hp']
                break
        if command == '3':
            while ac.playerItem['potMax'] == 0:
                break
            else:
                ac.playerItem['potMax'] = ac.playerItem['potMax'] - 1
                ac.playerCopy['hp'] = ac.player['hp']
                break
        if command == '4':
            break
        else:
            command = str(input('У вас его нет, выберите другое\n'))
    return command


def rollTheDice():
    i = int(randint(1, 10))
    return i


def reversRollTheDice():
    i = int(randint(-20, -10))
    return i
