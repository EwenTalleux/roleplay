import json
import main

with open("storage.json") as file:
    data = json.load(file)


def greetings(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return: str
    """
    main_line = '|   ' + data["locations"][shopid] + '   |'
    welcome_message = 'Welcome To'
    little_length = (len(main_line) - (len(welcome_message) + 2))
    little_length2 = (len(main_line) - (len(data["towns"][town]) + 2))
    if little_length % 2 != 0:
        spacing1 = int(little_length / 2)
        spacing2 = int(little_length / 2) + 1
    else:
        spacing1 = int(little_length / 2)
        spacing2 = int(little_length / 2)

    if little_length2 % 2 != 0:
        spacing3 = int(little_length2 / 2)
        spacing4 = int(little_length2 / 2) + 1
    else:
        spacing3 = int(little_length2 / 2)
        spacing4 = int(little_length2 / 2)

    for length in range(len(main_line)):
        print('_', end='')
    print()
    print('|', end='')
    for length in range(len(main_line) - 2):
        print(' ', end='')
    print('|')
    print('|', end='')
    for length in range(spacing1):
        print(' ', end='')
    print(welcome_message, end='')
    for length in range(spacing2):
        print(' ', end='')
    print('|')
    print(main_line)
    print('|', end='')
    for length in range(spacing3):
        print(' ', end='')
    print(data["towns"][town], end='')
    for length in range(spacing4):
        print(' ', end='')
    print('|')
    print('|', end='')
    for length in range(len(main_line) - 2):
        print('_', end='')
    print('|')


def display_shop_menu():
    """
    :return: str
    """
    print('____________________')
    print('|                  |')
    print('|     0 - Exit     |')
    print('|     1 - Sell     |')
    print('|     2 - Buy      |')
    print('|__________________|')


def shop(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return:
    """
    greetings(town, shopid)
    while True:
        display_shop_menu()
        playerchoice = main.user_type_text()
        if playerchoice in main.data["shop_menu_options"]:
            globals()[main.data['shop_menu_options'][playerchoice]](town, shopid)
        elif playerchoice == "0":
            return
        else:
            print('Invalid option, please type one of the options above.')


def display_selling_menu(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return:
    """
    possible_choice = ['0']
    salable_items = salable_in_inventory(town, shopid)
    if not salable_items:
        print('[---No Salable Item---]')
        print('____________________')
        print('|                  |')
        print('|     0 - Exit     |')
        print('|__________________|')
    else:
        display_salable_item(town, shopid)
        print('____________________')
        print('|                  |')
        print('|     0 - Exit     |')
        print('| Type item number |')
        print('|     to use it    |')
        print('|__________________|')

    for count in range(len(salable_items)):
        possible_choice.append(str(count + 1))

    while True:
        user_choice = main.user_type_text()
        if user_choice in possible_choice:
            if user_choice == '0':
                return False
            else:
                return sell_item(user_choice, town, shopid)
        else:
            print('Invalid option, please type one of the options above.')


def sell_shop_item(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return: list
    """
    return [item for item in data["shops"][town][shopid]["sell"].keys()]


def salable_in_inventory(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return:
    """
    return [item for item in main.player.inventory if item in sell_shop_item(town, shopid)]


def display_salable_item(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return: str
    """
    count = 1
    main_line = '|   '
    for item in salable_in_inventory(town, shopid):
        main_line = main_line + str(count) + ' - ' + data["items"][item]["name"] + ' : ' + str(
            data["shops"][town][shopid]["sell"][item]) + '   '
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


def sell_item(user_choice, town, shopid):
    """
    :param town: str
    :param shopid: str
    :param user_choice: str
    :return:
    """
    main.player.money = main.player.money + data["shops"][town][shopid]["sell"][
        salable_in_inventory(town, shopid)[int(user_choice) - 1]]
    main.player.inventory.pop(main.player.inventory.index(salable_in_inventory(town, shopid)[int(user_choice) - 1]))
    return


def display_buying_menu(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return:
    """
    possible_choice = ['0']
    purchasable_items = purchasable_item(town, shopid)
    if not purchasable_items:
        print('[---No Purchasable Item---]')
        print('____________________')
        print('|                  |')
        print('|     0 - Exit     |')
        print('|__________________|')
    else:
        display_purchasable_item(town, shopid)
        print('____________________')
        print('|                  |')
        print('|     0 - Exit     |')
        print('| Type item number |')
        print('|     to use it    |')
        print('|__________________|')

    for count in range(len(purchasable_items)):
        possible_choice.append(str(count + 1))

    while True:
        user_choice = main.user_type_text()
        if user_choice in possible_choice:
            if user_choice == '0':
                return False
            else:
                return buy_item(user_choice, town, shopid)
        else:
            print('Invalid option, please type one of the options above.')


def display_purchasable_item(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return:
    """
    count = 1
    main_line = '|   '
    for item in purchasable_item(town, shopid):
        main_line = main_line + str(count) + ' - ' + data["items"][item]["name"] + ' : ' + str(
            data["shops"][town][shopid]["buy"][item]) + '   '
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


def purchasable_item(town, shopid):
    """
    :param town: str
    :param shopid: str
    :return:
    """
    return [item for item in data["shops"][town][shopid]["buy"].keys()]


def buy_item(user_choice, town, shopid):
    """
    :param user_choice: str
    :param town: str
    :param shopid: str
    :return:
    """
    if main.player.money >= data["shops"][town][shopid]["buy"][purchasable_item(town, shopid)[int(user_choice) - 1]]:
        main.player.money = main.player.money - data["shops"][town][shopid]["buy"][purchasable_item(town, shopid)[int(
            user_choice) - 1]]
        main.player.add_inventory(purchasable_item(town, shopid)[int(user_choice) - 1])
    else:
        print("You don't have enough money to buy this item.")
    return
