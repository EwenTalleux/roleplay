# L
import mobsobject
import main
import place
import os
import effects


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def battle(mob, level):
    """
    :param mob: str
    :param level: int
    :return:
    """
    Mob = mobsobject.Mob(mob, level)
    while main.player.currentlifespan > 0 and Mob.currentlifespan > 0:
        status(Mob)
        do_enemy_turn = playerturn(Mob)
        if Mob.currentlifespan > 0:
            enemyturn(Mob, do_enemy_turn)
        cls()
    if Mob.currentlifespan <= 0:
        giveloots(Mob)
        giveexp(Mob)
        rewards(Mob)
        main.player.levelup()
        return True
    elif main.player.currentlifespan <= 0:
        print("You lost against " + main.data["mobs"][Mob.name]["name"] + " level " + str(Mob.level) + ".")
        return False


def playerturn(Mob):
    """
    :return:
    """
    while True:
        display_fight_menu()
        playerchoice = main.user_type_text()
        if playerchoice in main.data["fight_menu_options"]:
            do_enemy_turn = globals()[main.data['fight_menu_options'][playerchoice]](Mob)
            return do_enemy_turn
        else:
            print('Invalid option, please type one of the options above.')


def playerattacks(Mob):
    """
    :param Mob: Mob object
    :return:
    """
    damage = calcul_damage()
    # todo add after kick effect
    Mob.currentlifespan = round((Mob.currentlifespan - damage), 1)
    return True


def useitem(user_choice_item, Mob):
    """
    :return:
    """
    for effect, value in main.data['items'][create_fight_inventory()[int(user_choice_item) - 1]]['effect'].items():
        if main.data["effects"][effect]["effect_on"] == "self":
            effect_on = main.player
        elif main.data["effects"][effect]["effect_on"] == "mob":
            effect_on = Mob
        eval('effects.' + effect + '_effect')(value, value > 0, effect_on)
        main.player.inventory.pop(main.player.inventory.index(create_fight_inventory()[int(user_choice_item) - 1]))
    return


def display_fight_menu():
    """
    :return: str
    """
    print('____________________')
    print('|                  |')
    print('|    1 - Attack    |')
    print('|   2 - Use Item   |')
    print('|__________________|')


def fight_inventory_menu(Mob):
    """

    :return: str
    """
    possible_choice = ['0']
    fight_inventory = create_fight_inventory()
    if not fight_inventory:
        print('[---No Usable Item---]')
        print('____________________')
        print('|                  |')
        print('|     0 - Exit     |')
        print('|__________________|')
    else:
        display_fight_inventory()
        print('____________________')
        print('|                  |')
        print('|     0 - Exit     |')
        print('| Type item number |')
        print('|     to use it    |')
        print('|__________________|')

    for count in range(len(fight_inventory)):
        possible_choice.append(str(count + 1))

    while True:
        user_choice = main.user_type_text()
        if user_choice in possible_choice:
            if user_choice == '0':
                return False
            else:
                return useitem(user_choice, Mob)
        else:
            print('Invalid option, please type one of the options above.')


def create_fight_inventory():
    """
    :return:
    """
    return [item for item in main.player.inventory if main.data['items'][item]['use_in_fight'] == 1]


def display_fight_inventory():
    """
        :return: str
        """
    count = 1
    main_line = '|   '
    for item in create_fight_inventory():
        main_line = main_line + str(count) + ' : ' + main.data["items"][item]["name"] + '   '
        count += 1
    main_line = main_line + '|'
    for lenght in range(len(main_line)):
        print('_', end='')
    print()
    print('|', end='')
    for lenght in range(len(main_line) - 2):
        print(' ', end='')
    print('|')
    print(main_line)
    print('|', end='')
    for lenght in range(len(main_line) - 2):
        print('_', end='')
    print('|')


def status(Mob):
    """
    :param Mob: Mob object
    :return: str
    """
    if int(Mob.currentlifespan) == Mob.currentlifespan:
        moblife = int(Mob.currentlifespan)
    else:
        moblife = Mob.currentlifespan
    if int(main.player.currentlifespan) == main.player.currentlifespan:
        playerlife = int(main.player.currentlifespan)
    else:
        playerlife = main.player.currentlifespan
    print(main.data['mobs'][Mob.name]['name'] + ' : ' + str(moblife) + '/' + str(Mob.maxlifespan))
    print(main.player.name + " : " + str(playerlife) + '/' + str(main.player.maxlifespan))


def enemyturn(Mob, do_enemy_turn):
    """
    :param do_enemy_turn: boolean
    :param Mob: mob object
    :return:
    """
    if do_enemy_turn:
        damage = (Mob.strength - ((main.player.defense - 1) / 100) - (main.player.armor / 10))
        if damage < 0:
            damage = 0
        main.player.currentlifespan = round(
            main.player.currentlifespan - damage
            , 1)


def giveloots(Mob):
    """
    :param Mob: mob object
    :return:
    """
    Mob.set_looting()
    for item in Mob.loots:
        main.player.add_inventory(item)


def giveexp(Mob):
    """
    :param Mob: mob object
    :return:
    """
    main.player.exppoints = main.player.exppoints + Mob.exp


def rewards(Mob):
    """
    :param Mob: mob object
    :return:
    """
    if not Mob.loots:
        print("You received nothing.")
    elif len(Mob.loots) == 1:
        print("You received : " + main.data["items"][Mob.loots[0]]["name"])
    else:
        print("You received ", end="")
        for item_index in range(len(Mob.loots) - 2):
            print(main.data["items"][Mob.loots[item_index]]["name"])
            print(", ", end="")
        print(main.data["items"][Mob.loots[-2]]["name"] + " and " + main.data["items"][Mob.loots[-1]]["name"] + ".")
    print("You won " + str(Mob.exp) + " exp points.")


def calcul_damage():
    """
    :return:
    """
    return main.data["weapons"][main.player.weapon]["damage"] * main.player.attack


def death_player():
    print("You have no more life points. Travelers have found you very weak on the beaches of "
          + main.data["towns"][main.player.currentplace]["name"]
          + ". You were taken to the nearest health center and paid 5 coins.")
    main.player.healing()
    return place.choice_direction_menu(main.player.currentplace)
