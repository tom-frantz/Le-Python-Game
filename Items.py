class ItemLists(object):
    def __init__(self):
        self.fruit = ['Apples', 'Cherries', 'Grapes', 'Peach', 'Pears', 'Plums']
        self.vegetables = ['Beans', 'Broccoli', 'Cabbage', 'Carrots', 'Corn', 'Lettuce', 'Potatoes', 'Zucchini']
        self.canned_food = ['Canned Artichokes', 'Canned beans', 'Canned fruit salad', 'Canned peaches', 'Canned pineapples', 'Canned plums', 'Canned mushrooms', 'Canned Spaghetti', 'Canned Soup', 'Spam', 'Tomato paste']
        self.dry_food = ['Almonds', 'Cashews', 'Macadamias', 'Pasta', 'Peanuts']
        self.base_craft = ['Metal sheets']
        self.weapon_craft = ['Pistol parts', 'Shotgun parts', 'Assault rifle parts', 'Sniper parts']
        self.crafting_misc = ['Components', 'Electronic parts', 'Parts', 'Scrap metal']
        self.luxuries = ['Batteries', 'Gems', 'Jewelry', 'Money', 'Toilet Paper']
        self.damon = ['Damon']


class PlaceLists(object):
    def __init__(self):
        self.Towns = ['Romsey', 'Woodend', 'Sunbury']
        self.Buildings = ['Cop shop', 'Hospital', 'Residence']


class Item(object):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super(Weapon, self).__init__(name, description, value)
        self.damage = damage