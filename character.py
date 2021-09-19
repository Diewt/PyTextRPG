import random
import math

class character:
    def __init__(self):
        self.name = ''
        self.maxHealth = 0
        self.currentHealth = 0
        self.strength = 0
        self.defense = 0
        self.level = 1
        self.exp = 0

    # Attack calculation function that randomizes the damage between 2 ranges
    def attackDamage(self):
        min = math.floor(self.strength * 0.8)
        max = math.floor(self.strength * 1.2)

        damage = random.randint(min, max)
        return damage

    # Taking Damage functions
    def takeDamage(self, damage):
        min = math.floor(self.defense * 0.8)
        max = math.floor(self.defense * 1.2)

        reduction = random.randint(min, max)
        damage -= reduction

        if damage < 0:
            damage = 1

        self.currentHealth -= damage

    # Healing functions
    def healHealth(self, healing):
        if (self.currentHealth + healing) > self.maxHealth:
            self.currentHealth = self.maxHealth
        else:
            self.currentHealth += healing

    # Check if character is dead
    def isDead(self):
        if self.currentHealth <= 0:
            return True
        else:
            return False

    # Setter and Getter functions
    # These really aren't needed in python since there aren't any real private variables in python classes
    # However, These are currently being used to practice encapsulation as getters and setters are used in other
    # languages such as C++
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMaxHealth(self, value):
        self.maxHealth = value

    def getMaxHealth(self):
        return self.maxHealth

    def setCurrentHealth(self, value):
        self.currentHealth = value

    def getCurrentHealth(self):
        return self.currentHealth

    def setStrength(self, value):
        self.strength = value

    def getStrength(self):
        return self.strength

    def setDefense(self, value):
        self.defense = value

    def getDefense(self):
        return self.defense

    def getLevel(self):
        return 'LV: ' + str(self.level)
