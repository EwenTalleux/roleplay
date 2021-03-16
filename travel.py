import main
import fight
import place
import random


def travel(placefrom, placeto):
    """
    :param placefrom: str
    :param placeto: str
    :return:
    """
    time = main.data["travel"][[town for town in main.data["towns"].keys()].index(placefrom)][[town for town in main.data["towns"].keys()].index(placeto)]
    print(time)
    for battle in range(int(time / main.data["ships"][main.player.ship]["size"])):
        if main.player.is_alive():
            # todo add traveling message
            fight.battle(def_mob(placefrom, placeto), def_mob_level(placefrom, placeto))
        else:
            return fight.death_player()  # todo add death_player in fight.py
    main.player.currentplace = placeto
    return place.choice_direction_menu(placeto)


def def_mob(placefrom, placeto):
    """
    :param placefrom: str
    :param placeto: str
    :return:
    """
    return "mob_fish"

    # choice_mob = random.randint(len(main.data["mob_zone"][placefrom][placeto]))  # todo add "mob_zone" in storage.json
    # return main.data["mob_zone"][placefrom][placeto][choice_mob]


def def_mob_level(placefrom, placeto):
    """
    :param placefrom: str
    :param placeto: str
    :return:
    """
    return 2
