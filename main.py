import time
import json
import playerobject

print('test')


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
    while True:
        if text[0] == '!':
            return is_command_known(text.replace("!", ""))
        else:
            print("Please, type a valid command.")



def is_command_known(text):
    """
    :param text: str
    :return:
    """
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
        possible_choice = ['0', '1']
        user_choice = user_type_text()
        if user_choice in possible_choice:
            if user_choice == '0':
                return globals()[data['menu_options'][user_choice]]()
            elif user_choice == '1':
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
    if not player.have_weapon():
        player.change_item(item)
    else:
        player.add_inventory(player.weapon)
        player.change_item(item)


def exit():
    return

player.add_inventory('id_card')

