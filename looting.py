import random
import sysvars
import zombies
sysvar = sysvars.SystemVariables()

def scout(sysvar):
    print(''' what region would you like to explore:
( Town1, Town2, Town3, Town4, Town5 )''')
    region = input().lower()
    print('You arrive at  + str(region)' + 'safely and begin to scout the area, you see' + random.choice[])
    Building = input()
    enemy_zombies = random.choice(['yes', 'no'])
    if enemy_zombies == 'yes':
        enemy_zombies.loot_zombies()
    elif enemy_zombies == 'no':
        print('Looks clear of zeds, open season.. for everyone')
    loot_building = input()
    loot = random.choice(['fruit', 'veg'])
    if loot == 'fruit':
        loot = random.choice(sysvar.fruit)
        print(loot)
    elif loot == 'veg':
        loot = random.choice(sysvar.vegetables)
        print(loot)

    # loot = random.choice(['Food', 'Water', 'Medical supplies', 'Building supplies', 'scrap', 'nothing'])
    # print('You have found', loot)
    # return loot, inv

scout(sysvar)

