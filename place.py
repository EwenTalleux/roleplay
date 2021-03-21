# H
import main
import shops
import travel
import json

with open("storage.json") as file:
    data = json.load(file)


def choice_direction_menu(place=main.player.currentplace, demo = False):
    """
    :param place: str
    :return:
    """
    while True:
        display_current_place(place)
        if not demo:
            possible_choice = [str(choice) for choice in range(1, len(data["towns"][place]["go_to"])+1)]
            display_possible_choice(place, possible_choice)
            user_choice = main.user_type_text()
            if user_choice in possible_choice:
                if data["towns"][place]["go_to"][int(user_choice) - 1] in data["shops"][place]:
                    shops.shop(place, data["towns"][place]["go_to"][int(user_choice) - 1])
                else:
                    return globals()[data['towns'][place]["go_to"][int(user_choice) - 1]](place)
            else:
                if main.is_command(user_choice):
                    main.is_command_known(user_choice)
                else:
                    print('Invalid option, please type one of the options above.')
        else:
            return


def display_current_place(place):
    """
    :param place: str
    :return: str
    """
    main_line = '|   ' + main.data["towns"][place]["name"] + '   |'
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


def port(place):
    """
    :param place: str
    :return:
    """
    destinations = [destination for destination in data["towns"].keys()]
    destinations.remove(place)
    display_port(destinations)
    user_choice = main.user_type_text()
    if user_choice == "0":
        return
    else:
        return travel.travel(place, destinations[int(user_choice)-1])


def display_port(destinations):
    """
    :param destinations: list
    :return:
    """
    lignes = [str(destinations.index(destination)+1) + " : " + data["towns"][destination]["name"]
              for destination in destinations]
    lignes = ['0 : Exit'] + lignes
    max_lenght = 0
    for mot in lignes:
        if len(mot) > max_lenght:
            max_lenght = len(mot)
    for _ in range(max_lenght + 6):
        print('_', end='')
    print()
    print('|', end='')
    for _ in range(max_lenght + 4):
        print(' ', end='')
    print('|')
    for place in lignes:
        lenght = len(place)
        while lenght < max_lenght + 4:
            place = place + ' '
            lenght = len(place)
            if lenght < max_lenght + 4:
                place = ' ' + place
                lenght = len(place)
        print('|' + place + '|')
    print('|', end='')
    for _ in range(max_lenght + 4):
        print('_', end='')
    print('|')
    return


def display_possible_choice(place, possible_choice):
    """
    :param place: str
    :param possible_choice: list
    :return:
    """
    lignes = [numberplace+" : "+data["locations"][data["towns"][place]["go_to"][int(numberplace) - 1]]
              for numberplace in possible_choice]
    max_lenght = 0
    for mot in lignes:
        if len(mot) > max_lenght:
            max_lenght = len(mot)
    for _ in range(max_lenght+6):
        print('_', end='')
    print()
    print('|', end='')
    for _ in range(max_lenght+4):
        print(' ', end='')
    print('|')
    for place in lignes:
        lenght = len(place)
        while lenght < max_lenght+4:
            place = place + ' '
            lenght = len(place)
            if lenght < max_lenght+4:
                place = ' ' + place
                lenght = len(place)
        print('|'+place+'|')
    print('|', end='')
    for _ in range(max_lenght+4):
        print('_', end='')
    print('|')
    return
