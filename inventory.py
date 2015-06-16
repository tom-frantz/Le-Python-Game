import Items


class Inventory(object):
    def __init__(self):
        self.inventory = []

    def main(self):
        print("What would you like to do")
        print("[Management, Drop an item]")
        inv_choice = input().lower()
        print("")
        if inv_choice == "management" or inv_choice == "manage":
            print("You are in possession of:")
            self.print_list()
        else:
            self.minus_inventory()


    def add_inventory(self, item):
        self.inventory.append(item)

    def minus_inventory(self):
        print("What would you like to drop?")
        print("[Type the item name]")
        self.print_list()
        inv_choice = input().lower()
        print("")
        self.inventory.remove(inv_choice)
        print("You have removed:")
        print("[%s]" % inv_choice.capitalize())
        print("Your new inventory is:")
        self.print_list()

    def print_list(self):
        x = 1
        for i in range(len(self.inventory)):
            print("%s: %s" % (str(x), str(self.inventory[i:i+1])))
            x += 1

player_inv = Inventory()
player_inv.add_inventory("apple")
player_inv.add_inventory("gun")
player_inv.add_inventory("tank")
player_inv.main()