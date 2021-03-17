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
        self.currentplace = "middletown"
        self.ship = None

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
        :param id_item: str
        :return:
        """
        return not self.weapon == "hand"

    def change_weapon(self, id_item):
        """
        :param id_item: str
        :return:
        """
        self.weapon = id_item
        self.inventory.pop(self.inventory.index(id_item))

    def is_alive(self):
        return self.currentlifespan > 0

    def healing(self):
        self.currentlifespan = self.maxlifespan
        self.money -= 5
