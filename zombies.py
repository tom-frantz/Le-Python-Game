import random
import Items

def loot_zombies():
    zombie_amount = random.randint(1, 21)  # What amount of zombies there are. Roll is the amount of zombies
    if zombie_amount == 21:
        print('There\'s a lot of dead zombies around . . . Only a few remain behind, do you want to go look for loot?')
    else:
        print('''There seems to be roughly ''' + str(zombie_amount) + ''' or ''' + str(zombie_amount+1) + ''' around, do you want to go look for loot?
( Yes, No )''')
    loot_check = input().lower()
    if loot_check == 'no' or loot_check == 'n':
        return
    else:
        player.inv.append(items.fruit[0])
        print('''Do you want to engage the zombies at a long range or move in closer?
( Range, Melee )''')
        combat_distance = input().lower()

def base_zombies():
    print('Temp Holder')

def travel_zombies():
    print('Temp Holder')

def combat_zombies():
    print('Temp Holder')

