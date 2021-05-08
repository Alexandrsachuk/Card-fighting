class Damage_Cards():


    def __init__(self, name, damage, manacost, quantity):
        self.name = name
        self.damage = damage
        self.manacost = manacost
        self.quantity = quantity
    def choice_card(self, name):
        self.quantity -= 1
        print(f"Вы взяли карту {name}, в колоде осталось {self.quantity} шт.")

#Damage Cards===================================
small_fireball = Damage_Cards('Малый фаерболл', 15, 20, 2)
avalanche = Damage_Cards('Лавина', 20, 30, 2)
power_shot = Damage_Cards('Мощный выстрел', 10, 15, 2)
#===============================================


while True:

    c1 = int(input(f"Чемпион №1. Выберите карту из колоды. "
                   f"Малый фаерболл - 1, Лавина - 2: "))

    if small_fireball.quantity == 0 and c1 == 1:
        print(f"Карт {small_fireball.name} в колоде не осталось. Выберите другую карту.")
        continue
    elif avalanche.quantity == 0 and c1 == 2:
        print(f"Карт {avalanche.name} в колоде не осталось. Выберите другую карту.")
        continue

    if c1 == 1:
        small_fireball.choice_card('Малый фаерболл')
    elif c1 == 2:
        avalanche.choice_card('Лавина')

#============================================================================================


    c2 = int(input(f"Чемпион №2. Выберите карту из колоды. "
                   f"Малый фаерболл - 1, Лавина - 2: "))

    if small_fireball.quantity == 0 and c2 == 1:
        print(f"Карт {small_fireball.name} в колоде не осталось. Выберите другую карту.")
        continue
    elif avalanche.quantity == 0 and c2 == 2:
        print(f"Карт {avalanche.name} в колоде не осталось. Выберите другую карту.")
        continue

    if c2 == 1:
        small_fireball.choice_card('Малый фаерболл')
    elif c2 == 2:
        avalanche.choice_card('Лавина')
