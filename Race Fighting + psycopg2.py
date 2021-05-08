import random
import psycopg2

conn = psycopg2.connect(dbname='Race_Fight', user='postgres', password='07051998Sasha')
cur = conn.cursor()

def card_in_game(*args):
    x = 0
    card_in_game = []
    while x < 5:
        selected_cards = random.choice(*args)
        card_in_game.append(selected_cards)
        x += 1
    return card_in_game

def hit(health, damage):
    health -= damage
    return health

def mana_use(manapull, manacost):
    manapull -= manacost
    return manapull

def healing(health, healing, manapull, manacost):
    health += healing
    manapull -= manacost
    return health and manapull

def defence(armor_pers, armor_card, manapull, manacost):
    armor_pers += armor_card
    manapull -= manacost
    return

def hp_regen(p1_health, p1_hp_max, p1_hp_regen):
    if p1_health < p1_hp_max:
        p1_health += p1_hp_regen
    else:
        pass
    return p1_health

def stamina_regen(p1_stamina, p1_stamina_max, p1_stamina_regen):
    if p1_stamina < p1_stamina_max:
        p1_stamina += p1_stamina_regen
    else:
        pass
    return p1_stamina

def mana_regen(p1_manapull, p1_mana_max, p1_mana_regen):
    if p1_manapull < p1_mana_max:
        p1_manapull += p1_mana_regen
    else:
        pass
    return p1_manapull


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


    def __init__(self, name, damage, manacost, card_type):
        self.name = name
        self.damage = damage
        self.manacost = manacost
        self.card_type = card_type



class Healing_Cards():

    def __init__(self, name, healing, manacost, card_type):
        self.name = name
        self.healing = healing
        self.manacost = manacost
        self.card_type = card_type

class Protective_Cards():

    def __init__(self, name, armor, manacost, card_type):
        self.name = name
        self.armor = armor
        self.manacost = manacost
        self.card_type = card_type

#Damage Cards===================================
small_fireball = Damage_Cards('Малый фаерболл', 15, 20, 'a')
avalanche = Damage_Cards('Лавина', 20, 30, 'a')
power_shot = Damage_Cards('Мощный выстрел', 10, 15, 'a')
ice_blast = Damage_Cards('Ледяной взрыв', 13, 18, 'a')
dark_dagger = Damage_Cards('Теневой кинжал', 5, 10, 'a')
#===============================================

#Healing Cards=========================================
small_healing = Healing_Cards('Малое лечение', 10, 20, 'h')
middle_healing = Healing_Cards('Среднее лечение', 15, 25, 'h')
strong_healing = Healing_Cards('Сильное лечение', 20, 30, 'h')
#=======================================================

#Protective Cards=======================================
raise_shields = Protective_Cards('Поднять щиты', 5, 15, 'p')
put_a_block = Protective_Cards('Поставить блок', 10, 20, 'p')
block_the_blow = Protective_Cards('Блокировать удар', 15, 25, 'p')
#============================================================

#Champion===================================
Ork = Champion('Гул`дан', 10, 120, 40, 5, 5, 2, 120, 40, 100, 100, 10)
Ork_1 = Champion('Чернорук', 10, 120, 40, 5, 5, 2, 120, 40, 100, 100, 10)

Elf = Champion('Мэйв', 15, 100, 60, 0, 2, 5, 100, 60, 100, 100, 10)
Elf_1 = Champion('Сильвана', 15, 100, 60, 0, 2, 5, 100, 60, 100, 100, 10)

Human = Champion('Андуин Лотар', 12, 110, 50, 2, 3, 3, 110, 50, 100, 100, 10)
Human_1 = Champion('Медив', 12, 110, 50, 2, 3, 3, 110, 50, 100, 100, 10)

Undead = Champion('Кел`тузед', 9, 130, 50, 3, 4, 2, 130, 50, 100, 100, 10)
Undead_1 = Champion('Ануб`арак', 9, 130, 50, 3, 4, 2, 130, 50, 100, 100, 10)
#=============================================

#Выбор чемпионов===========================================
p1 = int(input('Выберите чемпиона: '
           'Орк - 1, Ельф - 2, Человек - 3, Нежить - 4: '))
if p1 == 1:
    p1 = Ork
elif p1 == 2:
    p1 = Elf
elif p1 == 3:
    p1 = Human
elif p1 == 4:
    p1 = Undead
else:
    print(f"Введено неправильное значение")

p2 = int(input('Выберите опонента: '
           'Орк - 1, Ельф - 2, Человек - 3, Нежить - 4: '))
if p2 == 1:
    p2 = Ork_1
elif p2 == 2:
    p2 = Elf_1
elif p2 == 3:
    p2 = Human_1
elif p2 == 4:
    p2 = Undead_1
#===========================================================

#Объявление начала матча и номер раунда=====================
print(f"Схватка началась. "
      f"{p1.name} VS {p2.name}!!!!!")
round = 0
#===========================================================

#Карманные колоды персонажей================================
personal_cards_1 = []
personal_cards_2 = []
#===========================================================


#Итоговая статистика========================================
#Запись использованных карт=================================
using_cards_1 = []
using_cards_2 = []
#===========================================================

#Сумма нанесенного маг урона====================================
total_magic_damage_1 = 0
total_magic_damage_2 = 0
#===========================================================

#Сумма нанесенного физ урона================================
total_phisical_damage_1 = 0
total_phisical_damage_2 = 0
#===========================================================

#Сумма полученого лечения===================================
total_healing_1 = 0
total_healing_2 = 0
#===========================================================

#Общий бафф брони===========================================
total_armor_1 = 0
total_armor_2 = 0
#===========================================================

#Переменные для набора карт=================================
x = 0
y = 0
#===========================================================

while True:
    #Общая колода карт==================================================================================
    card_pull = [small_fireball, avalanche, power_shot, ice_blast, dark_dagger,
                 small_healing, middle_healing, strong_healing,
                 raise_shields, put_a_block, block_the_blow]
    #===================================================================================================

    #Пулл карт раунда каждого персонажа=================================================================
    card_in_game_1 = card_in_game(card_pull)
    card_in_game_2 = card_in_game(card_pull)
    #===================================================================================================

    round += 1
    print(f"Раунд {round}")

    #Логика выбора одной карты из 5 предложенных для первого персонажа==========================================
    c1 = int(input(f"Выберите карту из списка первого чемпиона: "
                   f"{card_in_game_1[0].name} - 1, {card_in_game_1[1].name} - 2, {card_in_game_1[2].name} - 3, {card_in_game_1[3].name} - 4, "
                   f"{card_in_game_1[4].name} - 5: "))

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

    #Логика выбора одной карты из 5 предложенных для второго персонажа=========================================
    c2 = int(input(f"Выберите карту из списка второго чемпиона: "
                   f"{card_in_game_2[0].name} - 1, {card_in_game_2[1].name} - 2, {card_in_game_2[2].name} - 3, {card_in_game_2[3].name} - 4, "
                   f"{card_in_game_2[4].name} - 5: "))

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
    #============================================================================================================

    #Демонстрация, какие карты у персонажей======================================================================
    # print(f"У первого чемпиона на руках следующие карты: {personal_cards_1}")
    # print(f"У второго чемпиона на руках следующие карты: {personal_cards_2}")
    #============================================================================================================

    #Выбор карты из карманной колоды для действия================================================================

    if len(personal_cards_1) == 0:
        print(f'Ваша колода пуста')
    elif len(personal_cards_1) == 1:
        pc1 = int(input(f"Выберите карту из списка первого чемпиона: {personal_cards_1[0].name} - 1: "))
    # elif len(personal_cards_1) == 2:
    #     pc1 = int(input(f"Выберите карту из списка первого чемпиона: {personal_cards_1[0].name} - 1, {personal_cards_1[1].name} - 2: "))
    # elif len(personal_cards_1) == 3:
    #     pc1 = int(input(f"Выберите карту из списка первого чемпиона: {personal_cards_1[0].name} - 1, {personal_cards_1[1].name} - 2, "
    #                     f"{personal_cards_1[2]} - 3: "))
    # elif len(personal_cards_1) == 4:
    #     pc1 = int(input(f"Выберите карту из списка первого чемпиона: {personal_cards_1[0].name} - 1, {personal_cards_1[1].name} - 2, "
    #                     f"{personal_cards_1[2].name} - 3, {personal_cards_1[3].name} - 4: "))
    # elif len(personal_cards_1) == 5:
    #     pc1 = int(input(
    #         f"Выберите карту из списка первого чемпиона: {personal_cards_1[0].name} - 1, {personal_cards_1[1].name} - 2, "
    #         f"{personal_cards_1[2].name} - 3, {personal_cards_1[3].name} - 4, {personal_cards_1[4].name} - 5: "))

    # Дописать возможность сохранения карт из персональной колоды
        if pc1 == 1 and p1.manapull >= personal_cards_1[0].manacost:
            if personal_cards_1[0].card_type == 'a':
                p2.health -= personal_cards_1[0].damage
                p1.manapull -= personal_cards_1[0].manacost
                using_cards_1.append(personal_cards_1[0].name)
                total_magic_damage_1 += personal_cards_1[0].damage
                personal_cards_1.pop(0)
            elif personal_cards_1[0].card_type == 'h':
                p1.health += personal_cards_1[0].healing
                p1.manapull -= personal_cards_1[0].manacost
                using_cards_1.append(personal_cards_1[0].name)
                total_healing_1 += personal_cards_1[0].healing
                personal_cards_1.pop(0)
            elif personal_cards_1[0].card_type == 'p':
                p1.armor += personal_cards_1[0].armor
                p1.manapull -= personal_cards_1[0].manacost
                using_cards_1.append(personal_cards_1[0].name)
                total_armor_1 += personal_cards_1[0].armor
                personal_cards_1.pop(0)
        else:
            a = personal_cards_1[0].manacost - p1.manapull
            print(f"У {p1.name} недостаточно маны. Нужно еще {a} ед. маны")
        #
        #
        # elif pc1 == 2:
        #     if personal_cards_1[1].card_type == 'a':
        #         p2.health -= personal_cards_1[1].damage
        #         p1.manapull -= personal_cards_1[1].manacost
        #         personal_cards_1.pop(1)
        #     elif personal_cards_1[1].card_type == 'h':
        #         p1.health += personal_cards_1[1].healing
        #         p1.manapull -= personal_cards_1[1].manacost
        #         personal_cards_1.pop(1)
        #     elif personal_cards_1[1].card_type == 'p':
        #         p1.armor += personal_cards_1[1].armor
        #         p1.manapull -= personal_cards_1[1].manacost
        #         personal_cards_1.pop(1)
        #
        # elif pc1 == 3:
        #     if personal_cards_1[2].card_type == 'a':
        #         p2.health -= personal_cards_1[2].damage
        #         p1.manapull -= personal_cards_1[2].manacost
        #         personal_cards_1.pop(2)
        #     elif personal_cards_1[2].card_type == 'h':
        #         p1.health += personal_cards_1[2].healing
        #         p1.manapull -= personal_cards_1[2].manacost
        #         personal_cards_1.pop(2)
        #     elif personal_cards_1[2].card_type == 'p':
        #         p1.armor += personal_cards_1[2].armor
        #         p1.manapull -= personal_cards_1[2].manacost
        #         personal_cards_1.pop(2)
        #
        # elif pc1 == 4:
        #     if personal_cards_1[3].card_type == 'a':
        #         p2.health -= personal_cards_1[3].damage
        #         p1.manapull -= personal_cards_1[3].manacost
        #         personal_cards_1.pop(3)
        #     elif personal_cards_1[3].card_type == 'h':
        #         p1.health += personal_cards_1[3].healing
        #         p1.manapull -= personal_cards_1[3].manacost
        #         personal_cards_1.pop(3)
        #     elif personal_cards_1[3].card_type == 'p':
        #         p1.armor += personal_cards_1[3].armor
        #         p1.manapull -= personal_cards_1[3].manacost
        #         personal_cards_1.pop(3)
        #
        # elif pc1 == 5:
        #     if personal_cards_1[4].card_type == 'a':
        #         p2.health -= personal_cards_1[4].damage
        #         p1.manapull -= personal_cards_1[4].manacost
        #         personal_cards_1.pop(4)
        #     elif personal_cards_1[4].card_type == 'h':
        #         p1.health += personal_cards_1[4].healing
        #         p1.manapull -= personal_cards_1[4].manacost
        #         personal_cards_1.pop(4)
        #     elif personal_cards_1[4].card_type == 'p':
        #         p1.armor += personal_cards_1[4].armor
        #         p1.manapull -= personal_cards_1[4].manacost
        #         personal_cards_1.pop(4)

    if p2.health < 1:
        log_file = open('history.txt', 'a')
        log_file.write(f"Чемпион {p1.name} победил за {round} раундов!\n"
                       f"{p1.name} были использованы следующие карты: {using_cards_1}\n"
                       f"{p1.name} нанес маг. урона  - {total_magic_damage_1} ед.\n"
                       f"{p1.name} нанес физ. урона  - {total_phisical_damage_1} ед.\n"
                       f"{p1.name} получил лечения  - {total_healing_1} ед.\n"
                       f"{p1.name} получил брони - {total_armor_1} ед.\n"


                       f"{p2.name} были использованы следующие карты: {using_cards_2}\n"
                       f"{p2.name} нанес маг. урона - {total_magic_damage_2} ед.\n"
                       f"{p2.name} нанес физ. урона - {total_phisical_damage_2} ед.\n"
                       f"{p2.name} получил лечения - {total_healing_2} ед.\n"
                       f"{p2.name} получил брони - {total_armor_2} ед.\n"
                       f"\n")
        log_file.close()

        cur.execute(f"INSERT INTO history_log (winner, rounds, total_magic_damage_1, total_magic_damage_2, "
                    "total_phisical_damage_1, total_phisical_damage_2, total_healing_1, total_healing_2, "
                    "total_armor_1, total_amor_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (p1.name, round, total_magic_damage_1, total_magic_damage_2, total_phisical_damage_1,
                     total_phisical_damage_2, total_healing_1, total_healing_2, total_armor_1, total_armor_2))
        conn.commit()
        cur.close()
        conn.close()

        print(f"Чемпион {p1.name} победил за {round} раундов!\n"
              f"{p1.name} были использованы следующие карты: {using_cards_1}\n"
              f"{p1.name} нанес маг. урона  - {total_magic_damage_1} ед.\n"
              f"{p1.name} нанес физ. урона  - {total_phisical_damage_1} ед.\n"
              f"{p1.name} получил лечения  - {total_healing_1} ед.\n"
              f"{p1.name} получил брони - {total_armor_1} ед.\n"
              
              
              f"{p2.name} были использованы следующие карты: {using_cards_2}\n"
              f"{p2.name} нанес маг. урона - {total_magic_damage_2} ед.\n"
              f"{p2.name} нанес физ. урона - {total_phisical_damage_2} ед.\n"
              f"{p2.name} получил лечения - {total_healing_2} ед.\n"
              f"{p2.name} получил брони - {total_armor_2} ед.\n")
        break

    if len(personal_cards_2) == 0:
        print(f'Ваша колода пуста')
    elif len(personal_cards_2) == 1:
        pc2 = int(input(f"Выберите карту из списка второго чемпиона: {personal_cards_2[0].name} - 1: "))
    # elif len(personal_cards_2) == 2:
    #     pc2 = int(input(f"Выберите карту из списка первого чемпиона: {personal_cards_2[0].name} - 1, {personal_cards_2[1].name} - 2: "))
    # elif len(personal_cards_2) == 3:
    #     pc2 = int(input(f"Выберите карту из списка первого чемпиона: {personal_cards_2[0].name} - 1, {personal_cards_2[1].name} - 2, "
    #                     f"{personal_cards_2[2].name} - 3: "))
    # elif len(personal_cards_2) == 4:
    #     pc2 = int(input(f"Выберите карту из списка первого чемпиона: {personal_cards_2[0].name} - 1, {personal_cards_2[1].name} - 2, "
    #                     f"{personal_cards_2[2].name} - 3, {personal_cards_2[3].name} - 4: "))
    # elif len(personal_cards_2) == 5:
    #     pc2 = int(input(f"Выберите карту из списка первого чемпиона: {personal_cards_2[0].name} - 1, {personal_cards_2[1].name} - 2, "
    #                     f"{personal_cards_2[2].name} - 3, {personal_cards_2[3].name} - 4, {personal_cards_2[4].name} - 5: "))

        # Дописать возможность сохранения карт из персональной колоды
        if pc2 == 1 and p2.manapull >= personal_cards_2[0].manacost:
            if personal_cards_2[0].card_type == 'a':
                p1.health -= personal_cards_2[0].damage
                p2.manapull -= personal_cards_2[0].manacost
                using_cards_2.append(personal_cards_2[0].name)
                total_magic_damage_2 += personal_cards_2[0].damage
                personal_cards_2.pop(0)
            elif personal_cards_2[0].card_type == 'h':
                p2.health += personal_cards_2[0].healing
                p2.manapull -= personal_cards_2[0].manacost
                using_cards_2.append(personal_cards_2[0].name)
                total_healing_2 += personal_cards_2[0].healing
                personal_cards_2.pop(0)
            elif personal_cards_2[0].card_type == 'p':
                p2.armor += personal_cards_2[0].armor
                p2.manapull -= personal_cards_2[0].manacost
                using_cards_2.append(personal_cards_2[0].name)
                total_armor_2 += personal_cards_2[0].armor
                personal_cards_2.pop(0)
        else:
            b = personal_cards_2[0].manacost - p2.manapull
            print(f"У {p2.name} недостаточно маны. Нужно еще {b} ед. маны")
        #
        #
        # elif pc2 == 2:
        #     if personal_cards_2[1].card_type == 'a':
        #         p1.health -= personal_cards_2[1].damage
        #         p2.manapull -= personal_cards_2[1].manacost
        #         personal_cards_2.pop(1)
        #     elif personal_cards_2[1].card_type == 'h':
        #         p2.health += personal_cards_2[1].healing
        #         p2.manapull -= personal_cards_2[1].manacost
        #         personal_cards_2.pop(1)
        #     elif personal_cards_2[1].card_type == 'p':
        #         p2.armor += personal_cards_2[1].armor
        #         p2.manapull -= personal_cards_2[1].manacost
        #         personal_cards_2.pop(1)
        #
        # elif pc2 == 3:
        #     if personal_cards_2[2].card_type == 'a':
        #         p1.health -= personal_cards_2[2].damage
        #         p2.manapull -= personal_cards_2[2].manacost
        #         personal_cards_2.pop(2)
        #     elif personal_cards_2[2].card_type == 'h':
        #         p2.health += personal_cards_2[2].healing
        #         p2.manapull -= personal_cards_2[2].manacost
        #         personal_cards_2.pop(2)
        #     elif personal_cards_2[2].card_type == 'p':
        #         p2.armor += personal_cards_2[2].armor
        #         p2.manapull -= personal_cards_2[2].manacost
        #         personal_cards_2.pop(2)
        #
        # elif pc2 == 4:
        #     if personal_cards_2[3].card_type == 'a':
        #         p1.health -= personal_cards_2[3].damage
        #         p2.manapull -= personal_cards_2[3].manacost
        #         personal_cards_2.pop(3)
        #     elif personal_cards_2[3].card_type == 'h':
        #         p2.health += personal_cards_2[3].healing
        #         p2.manapull -= personal_cards_2[3].manacost
        #         personal_cards_2.pop(3)
        #     elif personal_cards_2[3].card_type == 'p':
        #         p2.armor += personal_cards_2[3].armor
        #         p2.manapull -= personal_cards_2[3].manacost
        #         personal_cards_2.pop(3)
        #
        # elif pc2 == 5:
        #     if personal_cards_2[4].card_type == 'a':
        #         p1.health -= personal_cards_2[4].damage
        #         p2.manapull -= personal_cards_2[4].manacost
        #         personal_cards_2.pop(4)
        #     elif personal_cards_2[4].card_type == 'h':
        #         p2.health += personal_cards_2[4].healing
        #         p2.manapull -= personal_cards_2[4].manacost
        #         personal_cards_2.pop(4)
        #     elif personal_cards_2[4].card_type == 'p':
        #         p2.armor += personal_cards_2[4].armor
        #         p2.manapull -= personal_cards_2[4].manacost
        #         personal_cards_2.pop(4)
    if p1.health < 1:
        log_file = open('history.txt', 'a')
        log_file.write(f"Чемпион {p1.name} победил за {round} раундов!\n"
                       f"{p1.name} были использованы следующие карты: {using_cards_1}\n"
                       f"{p1.name} нанес маг. урона  - {total_magic_damage_1} ед.\n"
                       f"{p1.name} нанес физ. урона  - {total_phisical_damage_1} ед.\n"
                       f"{p1.name} получил лечения  - {total_healing_1} ед.\n"
                       f"{p1.name} получил брони - {total_armor_1} ед.\n"


                       f"{p2.name} были использованы следующие карты: {using_cards_2}\n"
                       f"{p2.name} нанес маг. урона - {total_magic_damage_2} ед.\n"
                       f"{p2.name} нанес физ. урона - {total_phisical_damage_2} ед.\n"
                       f"{p2.name} получил лечения - {total_healing_2} ед.\n"
                       f"{p2.name} получил брони - {total_armor_2} ед.\n"
                       f"\n")
        log_file.close()

        cur.execute(f"INSERT INTO history_log (winner, rounds, total_magic_damage_1, total_magic_damage_2, "
                    "total_phisical_damage_1, total_phisical_damage_2, total_healing_1, total_healing_2, "
                    "total_armor_1, total_amor_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (p1.name, round, total_magic_damage_1, total_magic_damage_2, total_phisical_damage_1,
                     total_phisical_damage_2, total_healing_1, total_healing_2, total_armor_1, total_armor_2))
        conn.commit()
        cur.close()
        conn.close()

        print(f"Чемпион {p2.name} победил за {round} раундов!\n")
        print(f"{p1.name} были использованы следующие карты: {using_cards_1}\n"
              f"{p1.name} нанес маг. урона  - {total_magic_damage_1} ед.\n"
              f"{p1.name} нанес физ. урона  - {total_phisical_damage_1} ед.\n"
              f"{p1.name} получил лечения  - {total_healing_1} ед.\n"
              f"{p1.name} получил брони - {total_armor_1} ед.\n"


              f"{p2.name} были использованы следующие карты: {using_cards_2}\n"
              f"{p2.name} нанес маг. урона - {total_magic_damage_2} ед.\n"
              f"{p2.name} нанес физ. урона - {total_phisical_damage_2} ед.\n"
              f"{p2.name} получил лечения - {total_healing_2} ед.\n"
              f"{p2.name} получил брони - {total_armor_2} ед.\n")
        break

#Выбор действия=====================================================================
    a1 = int(input(f"Выберите действие {p1.name}: "
          "Атака - 1, Мощная атака - 2, Ваншот - 4, Пропустить ход - 5: "))

# Логика действий====================================================================
    if a1 == 1:
        p2.health -= p1.attack
        p1.stamina -= 10
        total_phisical_damage_1 += p1.attack
    elif a1 == 2:
        p2.health -= 1.5*p1.attack
        p1.stamina -= 15
        total_phisical_damage_1 += 1.5*p1.attack
    # elif a1 == 3: Block
    #     p2.health -= 0.5 * p1.attack
    elif a1 == 4:
        p2.health -= p2.health
        total_phisical_damage_1 += p2.health
    elif a1 == 5:
        pass

# Условия победы=================================
    if p2.health < 1:
        log_file = open('history.txt', 'a')
        log_file.write(f"Чемпион {p1.name} победил за {round} раундов!\n"
                       f"{p1.name} были использованы следующие карты: {using_cards_1}\n"
                       f"{p1.name} нанес маг. урона  - {total_magic_damage_1} ед.\n"
                       f"{p1.name} нанес физ. урона  - {total_phisical_damage_1} ед.\n"
                       f"{p1.name} получил лечения  - {total_healing_1} ед.\n"
                       f"{p1.name} получил брони - {total_armor_1} ед.\n"


                       f"{p2.name} были использованы следующие карты: {using_cards_2}\n"
                       f"{p2.name} нанес маг. урона - {total_magic_damage_2} ед.\n"
                       f"{p2.name} нанес физ. урона - {total_phisical_damage_2} ед.\n"
                       f"{p2.name} получил лечения - {total_healing_2} ед.\n"
                       f"{p2.name} получил брони - {total_armor_2} ед.\n"
                       f"\n")
        log_file.close()

        cur.execute(f"INSERT INTO history_log (winner, rounds, total_magic_damage_1, total_magic_damage_2, "
                    "total_phisical_damage_1, total_phisical_damage_2, total_healing_1, total_healing_2, "
                    "total_armor_1, total_amor_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (p1.name, round, total_magic_damage_1, total_magic_damage_2, total_phisical_damage_1,
                     total_phisical_damage_2, total_healing_1, total_healing_2, total_armor_1, total_armor_2))
        conn.commit()
        cur.close()
        conn.close()

        print(f"Чемпион {p1.name} победил за {round} раундов!\n"
              f"{p1.name} были использованы следующие карты: {using_cards_1}\n"
              f"{p1.name} нанес маг. урона  - {total_magic_damage_1} ед.\n"
              f"{p1.name} нанес физ. урона  - {total_phisical_damage_1} ед.\n"
              f"{p1.name} получил лечения  - {total_healing_1} ед.\n"
              f"{p1.name} получил брони - {total_armor_1} ед.\n"


              f"{p2.name} были использованы следующие карты: {using_cards_2}\n"
              f"{p2.name} нанес маг. урона - {total_magic_damage_2} ед.\n"
              f"{p2.name} нанес физ. урона - {total_phisical_damage_2} ед.\n"
              f"{p2.name} получил лечения - {total_healing_2} ед.\n"
              f"{p2.name} получил брони - {total_armor_2} ед.\n")
        break

# #===================================================================================

# Выбор действия=====================================================================
    a2 = int(input(f"Выберите действие {p2.name}: "
                   "Атака - 1, Мощная атака - 2, Блок - 3, Ваншот - 4, Пропустить ход - 5: "))

# Логика действий====================================================================
    if a2 == 1:
        p1.health -= p2.attack
        p2.stamina -= 10
        total_phisical_damage_2 += p2.attack
    elif a2 == 2:
        p1.health -= 1.5*p2.attack
        p2.stamina -= 15
        total_phisical_damage_2 += 1.5*p2.attack
    # elif a2 == 3: Block
    #     p1.health -= 0.5 * p2.attack
    elif a2 == 4:
        p1.health -= p1.health
        total_phisical_damage_2 += p1.health
    elif a2 == 5:
        pass

# Условия победы=================================
    if p1.health < 1:
        log_file = open('history.txt', 'a')
        log_file.write(f"Чемпион {p1.name} победил за {round} раундов!\n"
                  f"{p1.name} были использованы следующие карты: {using_cards_1}\n"
                  f"{p1.name} нанес маг. урона  - {total_magic_damage_1} ед.\n"
                  f"{p1.name} нанес физ. урона  - {total_phisical_damage_1} ед.\n"
                  f"{p1.name} получил лечения  - {total_healing_1} ед.\n"
                  f"{p1.name} получил брони - {total_armor_1} ед.\n"
    
    
                  f"{p2.name} были использованы следующие карты: {using_cards_2}\n"
                  f"{p2.name} нанес маг. урона - {total_magic_damage_2} ед.\n"
                  f"{p2.name} нанес физ. урона - {total_phisical_damage_2} ед.\n"
                  f"{p2.name} получил лечения - {total_healing_2} ед.\n"
                  f"{p2.name} получил брони - {total_armor_2} ед.\n"
                       f"\n")
        log_file.close()

        cur.execute(f"INSERT INTO history_log (winner, rounds, total_magic_damage_1, total_magic_damage_2, "
                    "total_phisical_damage_1, total_phisical_damage_2, total_healing_1, total_healing_2, "
                    "total_armor_1, total_amor_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (p1.name, round, total_magic_damage_1, total_magic_damage_2, total_phisical_damage_1,
                     total_phisical_damage_2, total_healing_1, total_healing_2, total_armor_1, total_armor_2))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Чемпион {p1.name} победил за {round} раундов!\n"
              f"{p1.name} были использованы следующие карты: {using_cards_1}\n"
              f"{p1.name} нанес маг. урона  - {total_magic_damage_1} ед.\n"
              f"{p1.name} нанес физ. урона  - {total_phisical_damage_1} ед.\n"
              f"{p1.name} получил лечения  - {total_healing_1} ед.\n"
              f"{p1.name} получил брони - {total_armor_1} ед.\n"


              f"{p2.name} были использованы следующие карты: {using_cards_2}\n"
              f"{p2.name} нанес маг. урона - {total_magic_damage_2} ед.\n"
              f"{p2.name} нанес физ. урона - {total_phisical_damage_2} ед.\n"
              f"{p2.name} получил лечения - {total_healing_2} ед.\n"
              f"{p2.name} получил брони - {total_armor_2} ед.\n"
              )
        break
#==================================================================================

    #Регенерация здоровья в конце хода=================================================
    p1.health = hp_regen(p1.health, p1.hp_max, p1.hp_regen)
    p2.health = hp_regen(p2.health, p2.hp_max, p2.hp_regen)
    #==================================================================================

    #Регенерация выносливости==========================================================
    p1.stamina = stamina_regen(p1.stamina, p1.stamina_max, p1.stamina_regen)
    p2.stamina = stamina_regen(p2.stamina, p2.stamina_max, p2.stamina_regen)
    #==================================================================================

    #Регенерация маны==================================================================
    p1.manapull = mana_regen(p1.manapull, p1.mana_max, p1.mana_regen)
    p2.manapull = mana_regen(p2.manapull, p2.mana_max, p2.mana_regen)
    #=================================================================================

    #Вывод результатов раунда==========================================================
    print(f"У {p1.name} {p1.health} ед. здоровья, {p1.stamina} ед. выносливости, {p1.armor} брони и {p1.manapull} маны")
    print(f"У {p2.name} {p2.health} ед. здоровья, {p2.stamina} ед. выносливости, {p2.armor} брони и {p2.manapull} маны")
    #==================================================================================
