# H
import main
import shops
import travel
import sys
import os
import npcobject
import json

with open("storage.json") as file:
    data = json.load(file)

sys.setrecursionlimit(1500)


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# demo functions
def check_item_given_and_talk_to_hilltown_tm():
    return "hilltowntm" in main.player.mission_ncp_end


#  actual place.py functions
def choice_direction_menu(place=main.player.currentplace, demo=False):
    """
    :param demo: boolean
    :param place: str
    :return:
    """
    while True:
        if place == main.player.currentplace:
            if not demo:
                if check_item_given_and_talk_to_hilltown_tm():
                    return
                display_current_place(place)
                possible_choice = [str(choice) for choice in range(1, len(data["towns"][place]["go_to"]) + 1)]
                display_possible_choice(place, possible_choice)
                user_choice = main.user_type_text()
                if user_choice in possible_choice:
                    if data["towns"][place]["go_to"][int(user_choice) - 1] in data["shops"][place]:
                        cls()
                        shops.shop(place, data["towns"][place]["go_to"][int(user_choice) - 1])
                        cls()
                    elif data["towns"][place]["go_to"][int(user_choice) - 1] in data["npcs"]:
                        cls()
                        eval("npcobject.Npc('" + data['towns'][place]["go_to"][int(user_choice) - 1] + "').start")()
                    elif data["towns"][place]["go_to"][int(user_choice) - 1] in data["potion_brewer"][place]:
                        cls()
                        shops.brewer(place, data["towns"][place]["go_to"][int(user_choice) - 1])
                    else:
                        cls()
                        globals()[data['towns'][place]["go_to"][int(user_choice) - 1]](place)
                else:
                    if main.is_command(user_choice):
                        cls()
                        main.is_command_known(user_choice)
                    else:
                        cls()
                        print('Invalid option, please type one of the options above.')
            else:
                return
        else:
            return choice_direction_menu(main.player.currentplace)


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
        cls()
        return
    else:
        cls()
        return travel.travel(place, destinations[int(user_choice) - 1])


def display_port(destinations):
    """
    :param destinations: list
    :return:
    """
    lignes = [str(destinations.index(destination) + 1) + " : " + data["towns"][destination]["name"]
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
    lignes = [numberplace + " : " + data["locations"][data["towns"][place]["go_to"][int(numberplace) - 1]] if
              data["towns"][place]["go_to"][int(numberplace) - 1] in data["locations"] else
              numberplace + " : " + data["npcs"][data["towns"][place]["go_to"][int(numberplace) - 1]]["name"]
              for numberplace in possible_choice]
    print()
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
