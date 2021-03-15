import random
import json

with open("storage.json") as file:
    data = json.load(file)


class Mob:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.currentlifespan = data['mobs'][name]['life'] * level
        self.maxlifespan = data['mobs'][name]['life'] * level
        self.strength = data['mobs'][name]['strength'] * level
        self.loots = []
        self.exp = self.currentlifespan + self.strength
        self.persistenteffect = []

    def set_looting(self):
        """
        :return:
        """
        for item in data['mobs'][self.name]['loots']:
            chances = random.randint(0, 100)
            if chances <= data['mobs'][self.name]['loots'][item]:
                self.loots.append(item)
