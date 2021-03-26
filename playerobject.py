# E
import json

with open("storage.json") as file:
    data = json.load(file)


class Player:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.maxlifespan = 10
        self.currentlifespan = 10
        self.inventory = []
        self.exppoints = 0
        self.money = 0
        self.weapon = "hand"
        self.helmet = "head"
        self.chestplate = "chest"
        self.legging = "legs"
        self.boots = "feet"
        self.currentplace = "hilltown"
        self.ship = None
        self.attack = 1
        self.defense = 1
        self.level = 1
        self.items_given = []
        self.mission_ncp_end = []

    def add_inventory(self, id_item):
        """
        :param id_item: str
        :return: str
        """
        if id_item in data["items"]:
            self.inventory.append(id_item)
            return
        else:
            print('items id unknown')
            return

    def have_weapon(self):
        """
        :return: boolean
        """
        return not self.weapon == "hand"

    def have_helmet(self):
        """
        :return: boolean
        """
        return not self.helmet == "head"

    def have_chestplate(self):
        """
        :return: boolean
        """
        return not self.chestplate == "chest"

    def have_legging(self):
        """
        :return: boolean
        """
        return not self.legging == "legs"

    def have_boots(self):
        """
        :return: boolean
        """
        return not self.boots == "feet"

    def change_weapon(self, id_item):
        """
        :param id_item: str
        :return:
        """
        self.weapon = id_item
        self.inventory.pop(self.inventory.index(id_item))

    def change_helmet(self, id_item):
        """
        :param id_item: str
        :return:
        """
        self.helmet = id_item
        self.inventory.pop(self.inventory.index(id_item))

    def change_chestplate(self, id_item):
        """
        :param id_item: str
        :return:
        """
        self.chestplate = id_item
        self.inventory.pop(self.inventory.index(id_item))

    def change_legging(self, id_item):
        """
        :param id_item: str
        :return:
        """
        self.legging = id_item
        self.inventory.pop(self.inventory.index(id_item))

    def change_boots(self, id_item):
        """
        :param id_item: str
        :return:
        """
        self.boots = id_item
        self.inventory.pop(self.inventory.index(id_item))

    def is_alive(self):
        return self.currentlifespan > 0

    def healing(self):
        self.currentlifespan = self.maxlifespan
        self.money -= 5

    def setlevel(self):
        return (self.exppoints // 10)+1

    def levelup(self):
        if self.setlevel() != self.level:
            self.level = self.setlevel()
            self.attack = round(self.attack + 0.3/self.attack, 1)
            self.defense = round(self.defense + 0.3 / self.defense, 1)
            self.maxlifespan = self.maxlifespan + 1
            print("You have just passed level " + str(self.level) + ".")
