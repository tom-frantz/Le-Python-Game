import random

def main():
    print(''' what region would you like to explore. (Town1,Town2,Town3,Town4,Town5 )''')
    region = input().lower()
    print('You arrive at ' + str(region) + ' safely and begin to scout the area, you see '"(building1,building2,building3")
    Building = input()

    loot = random.choice(['Food', 'Water', 'Medical supplies', 'Building supplies', 'scrap', 'nothing'])
    print('You have found', loot)
    zombies = random.choice(['yes', 'no'])
    if zombies == 'yes':
            print('there are zombies around here, might be some good loot')
    print('Do you want to go in')
    loot_building = input()


main()
