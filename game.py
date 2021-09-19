from player import player
from enemy import enemy
from textColor import textColor
import time


# Main Menu, the first text the player should see
def mainMenu():
    while True:
        choice = input("Text RPG - Please Enter an Option Corresponding to the Number on the Left"
                       '\n1: New Game'
                       '\n2: Quit'
                       '\n')

        if choice == '1':
            game()
            break
        elif choice == '2':
            break
        else:
            invalidSelection()


def invalidSelection():
    print('<==============================================>'
          '\nInvalid choice please input a valid Option'
          '\n<==============================================>')
    time.sleep(0.5)


# Gameplay loop
def game():
    hero = player()
    foe = enemy()

    hero.inputName()

    hero.startingStats()
    foe.generateEnemy()

    while True:
        printHealthValues(hero, foe)
        action = input("What will you do:"
                       "\n1: Attack "
                       "\n2: Stats "
                       "\n3: Run "
                       "\n")

        if action == '1':
            if attack(hero, foe):
                break
        elif action == '2':
            hero.displayStats()
        elif action == '3':
            time.sleep(0.5)
            print('You ran away and lived a happy life')
            break
        else:
            time.sleep(0.5)
            invalidSelection()


# function that prints out the health of the current combatants
def printHealthValues(hero, foe):
    heroHp = 'HP: ' + str(hero.getCurrentHealth()) + '/' + str(hero.getMaxHealth())
    foeHP = 'HP: ' + str(foe.getCurrentHealth()) + '/' + str(foe.getMaxHealth())

    print('<=================================================================>')
    print(f'{foe.getFloor():>28}')
    print(f'{textColor.green}'
          f'{hero.getName():<41}'
          f'{foe.getName():<30}'
          f'{textColor.ENDC}')
    print(f'{hero.getLevel():<41}'
          f'{foe.getLevel():<30}')
    print(f'{textColor.red}'
          f'{heroHp:<40} '
          f'{foeHP:<30} '
          f'{textColor.ENDC}')
    print('<=================================================================>')


# function that handles the attack action
def attack(hero, foe):
    damage = hero.attackDamage()
    print('You attacked the enemy for '
          + str(damage)
          + ' damage')

    foe.takeDamage(damage)
    if foe.isDead():
        time.sleep(0.5)
        print('You have killed the '
              + foe.getName())
        foe.generateEnemy()
        return False
    else:
        damage = foe.attackDamage()
        time.sleep(0.5)
        print('The '
              + foe.getName()
              + ' attacks you for '
              + str(damage))
        hero.takeDamage(damage)
        if hero.isDead():
            print('You have been killed by the '
                  + foe.getName())
            return True
