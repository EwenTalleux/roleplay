# <
import main
import fight
import shops
import place
import os
import npcobject


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def ask_name():
    """
    :return:
    """
    print("What's your name ? ")
    return main.user_type_text()


def nameuser():
    """
    :return:
    """
    while True:
        choice_player = main.user_type_text()
        if choice_player == "1":
            return "Hair"
        elif choice_player == "2":
            return ask_name()
        else:
            print('Invalid option, please type one of the options above.')


def check_if_healingpotion_in_inventory():
    """
    :return:
    """
    while True:
        if 'healing_potion' in main.player.inventory:
            return
        else:
            print("You didn't buy anything. Go back in the shop and buy something.")
            shops.shop('middletown', 'shop1')


print("Oh ! Hey, you !")
print("You're Hair right ?")
print()
print('____________________')
print('|                  |')
print('|     1 - Yes      |')
print('|     2 - No       |')
print('|__________________|')
name = nameuser()
cls()
print("Oh great ! Hello " + name + " !")
print("Humm... Tell me please. What are you ?")
print("You're a ...")
gender = main.user_type_text()
cls()
print("Ah yes, of course ! You're a " + gender + " !")
main.player.name = name
main.player.gender = gender
print("I gave you some money. Go make some shopping. You need stuff to fight wildness monsters.")
main.player.money = main.player.money + 15
print("You just earned 15 coins.")
shops.shop('hilltown', 'shop1')
cls()
check_if_healingpotion_in_inventory()
print("Great ! Now let's fight some monsters !")
print("Oh look ! There's a very big and angry fish there. Go kick this bitch's ass !")
if fight.battle('mob_fish', 3):
    print("You're doing great job ! You're ready for your great adventure " + main.player.name + ".")
else:
    print("Well... You still have some progress to make...")
print("Remember you can check your inventory whenever you want in the menu by typing '!menu'.")
print("Now go talk to the Town Mayor, he has something for you.")
main.player.healing()
main.player.money = main.player.money + 5
place.choice_direction_menu()
print("Great ! You have finally returned the letter to the Town Mayor of Valleytown !")
print()
print("Game Over")
print("Thanks for playing the Baldead demo 0.0.3")
print("")
print("Type '!exit' to exit.")
main.is_command(main.user_type_text())
