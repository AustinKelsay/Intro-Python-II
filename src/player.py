from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []
    def move(self, direction):
        if hasattr(self.location, f'{direction}_to'):
            self.location = getattr(self.location, f'{direction}_to')
        else:
            print("You can't go that direction")

    def takeItem(self, item):
        self.inventory.append(item)
        print(f'Inventory: {self.inventory}')

    def dropItem(self, item):
        self.inventory.remove(item)
        print(f'Inventory: {self.inventory}')
