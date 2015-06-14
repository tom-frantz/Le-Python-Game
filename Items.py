class ItemLists(object):  # Used for determining loots VIA loot types
    def __init__(self):
        # Food
        self.fruit = ['Apples', 'Cherries', 'Grapes', 'Peach', 'Pears', 'Plums']
        self.vegetables = ['Beans', 'Broccoli', 'Cabbage', 'Carrots', 'Corn', 'Lettuce', 'Potatoes', 'Zucchini']
        self.canned_food = ['Canned Artichokes', 'Canned beans', 'Canned fruit salad', 'Canned peaches', 'Canned pineapples', 'Canned plums', 'Canned mushrooms', 'Canned Spaghetti', 'Canned Soup', 'Spam', 'Tomato paste']
        self.dry_food = ['Almonds', 'Cashews', 'Macadamias', 'Pasta', 'Peanuts']

        # Crafting
        self.base_craft = ['Metal sheets']
        self.crafting_misc = ['Components', 'Electronic parts', 'Parts', 'Scrap metal']
        self.weapon_craft = ['Pistol parts', 'Shotgun parts', 'Assault rifle parts', 'Sniper parts']


        # Misc
        self.luxuries = ['Batteries', 'Gems', 'Jewelry', 'Money', 'Toilet Paper']
        self.medicine = ["Bandage", "Pills", "Morphine"]
        self.damon = ['Damon']


class PlaceLists(object):  # Used for determining places
    def __init__(self):
        self.towns = ['Romsey', 'Woodend', 'Sunbury']
        self.romsey_buildings = ['Cop shop', 'Hospital', 'Residence']
        self.woodend_buildings = ['Cop shop', 'Hospital', 'Residence']
        self.sunbury_buildings = ['Cop shop', 'Hospital', 'Residence']


class BuildingLoots(object):  # Used for determining loots in buildings
    def __init__(self):
        self.hospital = ["medicine", "canned_food", "dry_food", ]


class Item(object):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super(Weapon, self).__init__(name, description, value)
        self.damage = damage