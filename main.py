import base_building
import scouting
import supply_run

temp2 = True
while temp2 == True:
    menu_input = input('What would you like to do. ( Base building, Scouting, Supply run) ').lower()
    if menu_input == 'b' or menu_input == 'base' or menu_input == 'base building' or menu_input == 'building':
        base_building.main()
    elif menu_input == 'scouting' or menu_input == 'scout':
        scouting.main()
    elif menu_input == 'supply' or menu_input == 'run' or menu_input == 'supply run':
        supply_run.main()
    else:
        print('Plox redo bb')