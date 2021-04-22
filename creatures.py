#+ создать игрока
#+ создать скелета
#+ создать призрака
#+ создать гоблина
#+ создать орка
#+ создать троля

player = {'name': '', 'hp': 100, 'dmg': 5, "arm": 1, 'blok': 10}

playerItem = {'potMin': 1, 'potStand': 1, 'potMax': 1, 'scroll': 0}

#playerClothes = {'head': False, 'body': False, 'legs': False, 'feet': False, 'hands': False,
 #                'gloves': False, 'rightHand': False, 'leftHand': False}

playerCopy = player.copy()

skeleton = {'name': 'Скелет', 'hp': 50, 'dmg': 5, "arm": 1, 'blok': 0}

ghost = {'name': 'Призрак', 'hp': 50, 'dmg': 5, "arm": 1, 'blok': 0}

ork = {'name': 'Орк', 'hp': 100, 'dmg': 10, "arm": 5, 'blok': 5}

troll = {'name': 'Троль', 'hp': 200, 'dmg': 20, "arm": 1, 'blok': 10}

goblin = {'name': 'Гоблин', 'hp': 75, 'dmg': 10, "arm": 2, 'blok': 2}