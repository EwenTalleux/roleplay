import main
import json

with open("storage.json") as file:
    data = json.load(file)


def choice_direction_menu(place=main.player.currentplace):
    """
    :param place: str
    :return:
    """
    display_current_place(place)


def display_current_place(place):
    """
    :param place: str
    :return: str
    """
    main_line = '|   ' + main.data["towns"][place] + '   |'
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
