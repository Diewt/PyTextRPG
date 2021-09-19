from character import character


class player(character):
    def __init__(self):
        super().__init__()
        self.inventory = []
        self.equipment = []

    # function to set off the player's initial stats and empty the inventory
    def startingStats(self):
        self.level = 1
        self.currentHealth = 10
        self.maxHealth = 10
        self.strength = 5
        self.inventory.clear()

    def inputName(self):
        while True:
            name = input('Before you head off, what is your name traveler? \n')
            if len(name) > 20:
                print('Error Name is too long, please enter a shorter name')
            else:
                self.name = name
                break

    def displayStats(self):
        print('<=================================================================>')
        print(self.name + ' LV: ' + str(self.level))
        print('Health: ' + str(self.currentHealth) + '/' + str(self.maxHealth))
        print('Strength: ' + str(self.strength))
        print('<=================================================================>')

