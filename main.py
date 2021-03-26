# O
import time
import json
import playerobject

player = playerobject.Player('name', 'gender')

with open("storage.json") as file:
    data = json.load(file)


def print_text(text):
    """
    :param text: str
    :return: str
    """
    for character in text:
        print(character, end='')
        if character != ' ':
            time.sleep(0.1)


def user_type_text():
    """
    :return: str
    """
    return input()


def is_command(text):
    """
    :param text: str
    :return:
    """
    if text[0] == '!':
        return True
    else:
        print("Please, type a valid command.")


def is_command_known(text):
    """
    :param text: str
    :return:
    """
    text = text.replace("!", "")
    if text in data['commands']:
        return globals()[data['commands'][text]]()
    else:
        print('Unknown command')
        return is_command(user_type_text())


def menu_open():
    """
    :return: str
    """
    display_menu()
    while True:
        possible_choice = [choice for choice in data["menu_options"].keys()]
        user_choice = user_type_text()
        if user_choice in possible_choice:
            if user_choice == '0':
                return globals()[data['menu_options'][user_choice]]()
            else:
                globals()[data['menu_options'][user_choice]]()
                display_menu()
        else:
            print('Invalid option, please type one of the options above.')


def exit_menu():
    """
    :return: NoneType
    """
    return None


def display_menu():
    print('____________________')
    print('|                  |')
    print('|     0 - Exit     |')
    print('|   1 - Inventory  |')
    print('|   2 - Equipment  |')
    print('|__________________|')


def inventory_menu():
    """
    :return: str
    """
    possible_choice = ['0']
    for count in range(len(player.inventory)):
        possible_choice.append(str(count + 1))

    while True:
        check_inventory()
        user_choice = user_type_text()
        if user_choice in possible_choice:
            if user_choice == '0':
                return
            else:
                display_item_description(player.inventory[int(user_choice) - 1])
                if data["items"][player.inventory[int(user_choice) - 1]]["equipable"]:
                    equip_menu(player.inventory[int(user_choice) - 1])
        else:
            print('Invalid option, please type one of the options above.')


def check_inventory():
    """
    :return: str
    """
    if not player.inventory:
        print('[---Empty Inventory---]')
        print('____________________')
        print('|                  |')
        print('|     0 - Exit     |')
        print('|__________________|')
    else:
        display_inventory()
        print('____________________')
        print('|                  |')
        print('|     0 - Exit     |')
        print('| Type item number |')
        print('|    to see more   |')
        print('|__________________|')


def display_inventory():
    """
    :return: str
    """
    count = 1
    main_line = '|   '
    for item in player.inventory:
        main_line = main_line + str(count) + ' : ' + data["items"][item]["name"] + '   '
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


def display_item_description(id_item):
    """
    :param id_item: str
    :return: str
    """
    print(data["items"][id_item]["name"] + ' : ' + data["items"][id_item]["description"])


def equip_menu(item):
    """
    :param item: str
    :return:
    """
    print('Do you want to equip this item ?')
    print('____________________')
    print('|                  |')
    print('|     1 - Yes      |')
    print('|     2 - No       |')
    print('|__________________|')
    while True:
        choice_player = user_type_text()
        if choice_player == "1":
            return equip_item(item)
        elif choice_player == "2":
            return
        else:
            print('Invalid option, please type one of the options above.')


def equip_item(item):
    """
    :param item: str
    :return:
    """
    if not eval("player.have_" + data["items"][item]["equipable_type"])():
        eval("player.change_" + data["items"][item]["equipable_type"])(item)
    else:
        player.add_inventory(eval("player."+data["items"][item]["equipable_type"]))
        eval("player.change_" + data["items"][item]["equipable_type"])(item)


def exit():
    return


def equipment_list():
    equipment = []
    if player.helmet != "head":
        equipment.append("1")
    else:
        equipment.append("Ø")
    if player.chestplate != "chest":
        equipment.append("2")
    else:
        equipment.append("Ø")
    if player.legging != "legs":
        equipment.append("3")
    else:
        equipment.append("Ø")
    if player.boots != "feet":
        equipment.append("4")
    else:
        equipment.append("Ø")
    if player.weapon != "hand":
        equipment.append("5")
    else:
        equipment.append("Ø")
    return equipment


def display_equipment(equipment):
    print("_______            _______")
    print("|     |            |     |")
    print("|  "+equipment[0]+"  |   Helmet   |  "+equipment[4]+"  |   Weapon")
    print("|_____|            |_____|")
    print("_______")
    print("|     |")
    print("|  " + equipment[1] + "  |   Chestplate")
    print("|_____|")
    print("_______")
    print("|     |")
    print("|  " + equipment[2] + "  |   Legging")
    print("|_____|")
    print("_______")
    print("|     |")
    print("|  " + equipment[3] + "  |   Boots")
    print("|_____|")
    print("       ")


def display_defense_damage(item):
    if data["items"][item]["equipable_type"] != "weapon":
        print("Defense : "+str(data["armor"][item]["defense"]))
    else:
        print("Damage : " + str(data["weapons"][item]["damage"]))


def equipment_menu():
    possible_choice = ['0']+equipment_list()

    while True:
        display_equipment(equipment_list())
        user_choice = user_type_text()
        if user_choice in possible_choice:
            if user_choice == '0':
                return
            else:
                if user_choice == "1":
                    item = player.helmet
                if user_choice == "2":
                    item = player.chestplate
                if user_choice == "3":
                    item = player.legging
                if user_choice == "4":
                    item = player.boots
                if user_choice == "5":
                    item = player.weapon
                display_item_description(item)
                display_defense_damage(item)
        else:
            print('Invalid option, please type a valid option.')


player.add_inventory('id_card')
player.add_inventory('small_knife')
player.add_inventory('dirty_helmet')
player.ship = "rawboat1"
