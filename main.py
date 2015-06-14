import base_building
import looting
import inventory

print("What would you like to do?")
print("[Base building, Scouting, Supply run, Inventory, Quit]")
menu_input = input().lower()
print("")
while menu_input != 'quit':
    if menu_input == 'b' or menu_input == 'base' or menu_input == 'base building' or menu_input == 'building':
        base_building.main()
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
