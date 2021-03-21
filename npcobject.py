# E
import json

with open("storage.json") as file:
    data = json.load(file)

class Npc:
    def __init__(self, id):
        self.id = id
