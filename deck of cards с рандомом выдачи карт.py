import random
import time

def card_in_game(*args):
    x = 0
    card_in_game = []
    while x < 5:
        selected_cards = random.choice(*args)
        card_in_game.append(selected_cards)
        x += 1
    return card_in_game

class Champion():

    def __init__(self, name, attack, health, manapull, armor, hp_regen, mana_regen, hp_max, mana_max,
                 stamina, stamina_max, stamina_regen):

        self.name = name
        self.attack = attack
        self.health = health
        self.manapull = manapull
        self.armor = armor
        self.hp_regen = hp_regen
        self.mana_regen = mana_regen
        self.hp_max = hp_max
        self.mana_max = mana_max
        self.stamina = stamina
        self.stamina_max = stamina_max
        self.stamina_regen = stamina_regen

class Damage_Cards():


    def __init__(self, name, damage, manacost):
        self.name = name
        self.damage = damage
        self.manacost = manacost

    def hit(self, a):
        a -= self.damage

class Healing_Cards():

    def __init__(self, name, healing, manacost):
        self.name = name
        self.healing = healing
        self.manacost = manacost

class Protective_Cards():

    def __init__(self, name, armor, manacost):
        self.name = name
        self.armor = armor
        self.manacost = manacost

#Damage Cards===================================
small_fireball = Damage_Cards('Малый фаерболл', 15, 20)
avalanche = Damage_Cards('Лавина', 20, 30)
power_shot = Damage_Cards('Мощный выстрел', 10, 15)
ice_blast = Damage_Cards('Ледяной взрыв', 13, 18)
dark_dagger = Damage_Cards('Теневой кинжал', 5, 10)
#===============================================

#Healing Cards=========================================
small_healing = Healing_Cards('Малое лечение', 10, 20)
middle_healing = Healing_Cards('Среднее лечение', 15, 25)
strong_healing = Healing_Cards('Сильное лечение', 20, 30)
#=======================================================

#Protective Cards=======================================
raise_shields = Protective_Cards('Поднять щиты', 5, 15)
put_a_block = Protective_Cards('Поставить блок', 10, 20)
block_the_blow = Protective_Cards('Блокировать удар', 15, 25)
#============================================================


Ork = Champion('Гул`дан', 10, 120, 40, 5, 5, 2, 120, 40, 100, 100, 10)
Ork_1 = Champion('Чернорук', 10, 120, 40, 5, 5, 2, 120, 40, 100, 100, 10)


personal_cards_1 = []
personal_cards_2 = []
x = 0
y = 0
while True:
    card_pull = [small_fireball.name, avalanche.name, power_shot.name, ice_blast.name, dark_dagger.name,
                 small_healing.name, middle_healing.name, strong_healing.name,
                 raise_shields.name, put_a_block.name, block_the_blow.name]
    # card_in_game_1 = []
    # card_in_game_2 = []

    card_in_game_1 = card_in_game(card_pull)

    card_in_game_2 = card_in_game(card_pull)

    # while x < 5 and y < 5:
    #     selected_cards = random.choice(card_pull)
    #     card_in_game_1.append(selected_cards)
    #     x += 1
    #
    #     selected_cards = random.choice(card_pull)
    #     card_in_game_2.append(selected_cards)
    #     y += 1
    print(f"В этом раунде у первого чемпиона есть следующие карты: {card_in_game_1}")
    print(f"В этом раунде у второго чемпиона есть следующие карты: {card_in_game_2}")

    c1 = int(input(f"Выберите карту из списка первого чемпиона: "
                   f"{card_in_game_1[0]} - 1, {card_in_game_1[1]} - 2, {card_in_game_1[2]} - 3, {card_in_game_1[3]} - 4, "
                   f"{card_in_game_1[4]} - 5: "))

    if c1 == 1:
        personal_cards_1.append(card_in_game_1[0])
        card_in_game_1.pop(0)
    elif c1 == 2:
        personal_cards_1.append(card_in_game_1[1])
        card_in_game_1.pop(1)
    elif c1 == 3:
        personal_cards_1.append(card_in_game_1[2])
        card_in_game_1.pop(2)
    elif c1 == 4:
        personal_cards_1.append(card_in_game_1[3])
        card_in_game_1.pop(3)
    elif c1 == 5:
        personal_cards_1.append(card_in_game_1[4])
        card_in_game_1.pop(4)

    c2 = int(input(f"Выберите карту из списка второго чемпиона: "
                   f"{card_in_game_2[0]} - 1, {card_in_game_2[1]} - 2, {card_in_game_2[2]} - 3, {card_in_game_2[3]} - 4, "
                   f"{card_in_game_2[4]} - 5: "))

    if c2 == 1:
        personal_cards_2.append(card_in_game_2[0])
        card_in_game_2.pop(0)
    elif c2 == 2:
        personal_cards_2.append(card_in_game_2[1])
        card_in_game_2.pop(1)
    elif c2 == 3:
        personal_cards_2.append(card_in_game_2[2])
        card_in_game_2.pop(2)
    elif c2 == 4:
        personal_cards_2.append(card_in_game_2[3])
        card_in_game_2.pop(3)
    elif c2 == 5:
        personal_cards_2.append(card_in_game_2[4])
        card_in_game_2.pop(4)

    time.sleep(1)
    print(f"У первого чемпиона остались следующие карты: {card_in_game_1}")
    print(f"У второго чемпиона остались следующие карты: {card_in_game_2}")

    time.sleep(1)
    print(f"У первого чемпиона на руках следующие карты: {personal_cards_1}")
    print(f"У второго чемпиона на руках следующие карты: {personal_cards_2}")
    time.sleep(1)