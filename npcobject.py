# E
import main
import json

with open("storage.json") as file:
    data = json.load(file)


class Npc:
    def __init__(self, idnpc):
        self.idnpc = idnpc

    def start(self):
        for fonction in data["npcs"][self.idnpc]["fonctions_order"]:
            eval("self."+fonction)()

    def display_name(self):
        name = data["npcs"][self.idnpc]["name"]
        lenght = len(name) + 6
        for _ in range(lenght):
            print('_', end='')
        print()
        print("|", end='')
        for _ in range(lenght - 2):
            print(' ', end='')
        print("|")
        print("|  " + name + "  |")
        print("|", end='')
        for _ in range(lenght - 2):
            print('_', end='')
        print("|")
        print()

    def ask_text(self):
        print(data["npcs"][self.idnpc]["name"] + " : ", end='')
        print(data["npcs"][self.idnpc]["texts"]["askfor"])

    def give_item(self):
        main.player.add_inventory(data["npcs"][self.idnpc]["giveitem"])

    def check_for(self):
        tocheck = [test for test in data["npcs"][self.idnpc]["checkfor"].keys()]
        for test in tocheck:
            if test == "not_item":
                return data["npcs"][self.idnpc]["checkfor"]["not_item"] not in main.player.inventory
            elif test == "item":
                return data["npcs"][self.idnpc]["checkfor"]["item"] in main.player.inventory
            elif test == "level":
                return data["npcs"][self.idnpc]["checkfor"]["level"] <= main.player.level
            elif test == "health":
                return data["npcs"][self.idnpc]["checkfor"]["health"] <= main.player.currentlifespan

    def checkerror_text(self):
        print(data["npcs"][self.idnpc]["name"] + " : ", end='')
        print(data["npcs"][self.idnpc]["texts"]["checkerror"])

    def check_item_given_to_player(self):
        if data["npcs"][self.idnpc]["giveitem"] not in main.player.inventory and \
                data["npcs"][self.idnpc]["giveitem"] not in main.player.items_given:
            self.ask_text()
            self.give_item()
        elif self.check_for():
            self.end_mission_text()
            self.rewards()
        else:
            self.checkerror_text()

    def end_mission_text(self):
        print(data["npcs"][self.idnpc]["name"] + " : ", end='')
        print(data["npcs"][self.idnpc]["texts"]["end_mission"])

    def rewards(self):
        if self.idnpc not in main.player.mission_ncp_end:
            items = [item for item in data["npcs"][self.idnpc]["rewards"]["items"]]
            if len(items) == 0:
                pass
            elif len(items) == 1:
                print("You received : " + main.data["items"][items[0]]["name"])
            else:
                print("You received ", end="")
                for item_index in range(len(items) - 2):
                    print(main.data["items"][items[item_index]]["name"])
                    print(", ", end="")
                print(main.data["items"][items[-2]]["name"] + " and " + main.data["items"][items[-1]]["name"] + ".")
            if data["npcs"][self.idnpc]["rewards"]["money"] != 0:
                print("You just earned " + str(data["npcs"][self.idnpc]["rewards"]["money"]) + " coins.")
                main.player.money += data["npcs"][self.idnpc]["rewards"]["money"]
            main.player.mission_ncp_end.append(self.idnpc)
        else:
            return
