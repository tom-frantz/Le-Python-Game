import random
import Items
import zombies
places = Items.PlaceLists()
buildings = Items.BuildingLoots()
items = Items.ItemLists()


def scout():
    # Place check

    print("Which town would you like to go into?")
    print(places.towns)
    town_choice = input().lower() + "_buildings"
    print("")

    # Building check

    print("Which building would you like to go into?")
    print(getattr(places, town_choice))  # I'll explain getattr in person or over skype call, is slight confusing
    building_choice = input().lower()
    print("")

    # Zombie check ( To be done later, gonna get this running first )
    # loot determination and add to inv

    loot_catagory = random.choice(getattr(buildings, building_choice))
    loot = random.choice(getattr(items, loot_catagory))
    print("You found some", loot.lower() + ".")