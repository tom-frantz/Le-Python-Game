import random
import sysvars
import zombies
sysvar = sysvars.SystemVariables()

def scout(sysvar):
    print(''' what region would you like to explore:
( Town1, Town2, Town3, Town4, Town5 )''')
    region = input().lower()
    print('''You arrive at ''' + str(region) + ''' safely and begin to scout the area, you see:
( building1, building2, building3 )''')
    Building = input()
    zombies = random.choice(['yes', 'no'])
    if zombies == 'yes':
        zombies.loot_zombies()
    elif zombies == 'no':
        print('Looks clear of zeds, open season.. for everyone')
    loot_building = input()
    loot = random.choice(['fruit', 'veg'])
    if loot == 'fruit':
        loot = random.choice(sysvar.fruit)
        print(loot)
    elif loot == 'veg':
        loot = random.choice(sysvar.vegetables)
        print(loot)

    #loot = random.choice(['Food', 'Water', 'Medical supplies', 'Building supplies', 'scrap', 'nothing'])
    #print('You have found', loot)
    #return loot, inv

scout(sysvar)

