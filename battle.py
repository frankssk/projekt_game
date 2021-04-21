# счет блока
# счет брони
# вычет хп
# сам бой
import creatures as cr

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
        attackMob(mobCom[1])
   # elif mobCom == '2':
  #  elif mobCom == '3':
  #  elif mobCom == '4':
   # elif mobCom == '5':
   # else:

#def attack(mobCom):
 #   mob = mobCom
  #  mob['hp'] = mob['hp'] - cr.playerCopy['dmg']
   # return mob['hp']
def attackMob(mobCom):
    mob = mobCom
    cr.playerCopy['hp'] = cr.playerCopy['hp'] - mob['dmg']
    return cr.playerCopy['hp']






