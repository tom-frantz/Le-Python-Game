import BaseBuilding
import looting
import inventory
import pickle

# save game

class GameSave():
    @staticmethod
    def save_game(self):
        with open("savefile_1.txt", "wb") as f:
            pickle.dump([player, level_state], f, protocol=2)

    @staticmethod
    def load_game(self):
        with open("savefile_1.txt", "wb") as f:
            player, level_state = pickle.load(f)


print('Pick a save game:')
print('[savefile_1]')
save_file = input().lower() + ".txt"
if save_file == "savefile_1.txt":
    GameSave.load_game()

# Introduction sequence

print("What would you like to do?")
print("[Base building, Scouting, Supply run, Inventory, Quit]")
menu_input = input().lower()
print("")
while menu_input != 'quit':
    if menu_input == 'b' or menu_input == 'base' or menu_input == 'base building' or menu_input == 'building':
        BaseBuilding.main()
    elif menu_input == 'scouting' or menu_input == 'scout':
        looting.scout()
    elif menu_input == 'supply' or menu_input == 'run' or menu_input == 'supply run':
        looting.supply()
    elif menu_input == 'inv' or menu_input == 'inventory':
        inventory.main()
    print("What would you like to do?")
    print("[Base building, Scouting, Supply run, Quit]")
    menu_input = input().lower()
    print("")
print('Out of menu.')
