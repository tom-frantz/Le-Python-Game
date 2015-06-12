import random

def loot_zombies():
    zombie_amount = random.randint(1, 21)  # What amount of zombies there are. Roll is the amount of zombies
    if zombie_amount == 21:
        print('There\'s a lot of dead zombies around . . . Only a few remain behind, do you want to go look for loot?')
    else:
        print('There seems to be ' + str(zombie_amount) + ' around, do you want to go look for loot?')
    loot_check = input().lower()
    if loot_check == 'no' or loot_check == 'n':
        return
    else:
        print('')

def base_zombies():
    print('Temp Holder')

def travel_zombies():
    print('Temp Holder')

def combat_zombies():
    print('Temp Holder')
