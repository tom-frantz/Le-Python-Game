def main():

    import random

    region = input().lower()
    print(''' what region would you like to explore. (Town1,Town2,Town3,Town4,Town5 )''')
    print('You arrive at ' + str(region) + ' safely and begin to scout the area, you see '"(building1,building2,building3")
    Building = input()

    loot = random.choice = ['Food', 'Water', 'Medical supplies', 'Building supplies', 'scrap', 'nothing']
    if loot == 'Food':
        print('you found some food')
    elif loot == 'Water':
        print('You found some water')
    elif loot == 'Medical supplies':
        print('You found some Meds')
    elif loot == 'Building supplies':
        print('You found some building supplies')
    elif loot == 'scrap':
        print('You found some scrap')
    elif loot == 'nothing':
        print('You found nothing')

    zombies = ['yes', 'no']
    if zombies == 'yes':
            print('there are zombies around here, might be some good loot')

    print('Do you want to go in')
    loot_building = input()


main()
