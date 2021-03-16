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
    time = main.data["travel"][[town for town in main.data["towns"].keys()].index(placefrom)][
        [town for town in main.data["towns"].keys()].index(placeto)]
    for battle in range(int(time / main.data["ships"][main.player.ship]["size"])):
        if main.player.is_alive():
            traveling_message(battle, placefrom, placeto)
            mob = def_mob(placefrom, placeto)
            mob_message(mob)
            fight.battle(mob, def_mob_level(placefrom, placeto))
        else:
            return fight.death_player()
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


def traveling_message(battlenumber, placefrom, placeto):
    """
    :param placefrom: str
    :param placeto: str
    :param battlenumber: int
    :return:
    """
    if battlenumber == 0:
        print("You start your journey from " + main.data["towns"][placefrom]["name"] + " to "
              + main.data["towns"][placeto]["name"]
              + ".")
    else:
        print("You continue your journey.")


def mob_message(mobname):
    """
    :param mobname: str
    :return:
    """
    print("A terrible monster rises from the depths of the sea. This horrible " + main.data['mobs'][mobname]['name']
          + " begins to attack you.")
