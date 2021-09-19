from character import character
import bestiary
import random
import math


class enemy(character):
    def __init__(self):
        super().__init__()
        self.type = 0
        self.floor = 0

    # Increase floor count when we generate enemy and create appropriate enemy
    def generateEnemy(self):
        # Increase Floor Count everytime we spawn an enemy
        self.floor += 1

        # Enemies Level up every 5 floors
        if self.floor % 5 == 0:
            self.level += 1

        self.type = random.randint(1, 2)

        if self.type == 1:
            self.calculateStats('Goblin')
        elif self.type == 2:
            self.calculateStats('Golem')

    def calculateStats(self, key):
        self.name = key

        self.maxHealth = math.floor(bestiary.Bestiary[key]['stats'][0]
                                    * (self.level * bestiary.Bestiary[key]['stats'][1]))

        self.currentHealth = self.maxHealth

        self.strength = math.floor(bestiary.Bestiary[key]['stats'][2]
                                   * (self.level * bestiary.Bestiary[key]['stats'][3]))

        self.defense = math.floor(bestiary.Bestiary[key]['stats'][4]
                                  * (self.level * bestiary.Bestiary[key]['stats'][5]))

    def resetFloor(self):
        self.floor = 0

    def getFloor(self):
        return 'Floor ' + str(self.floor)

