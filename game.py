from core.player import Player
from core.orc import Orc 
from core.goblin import Goblin
import random

def create_player():
    name = input("enter any name:")
    print(f"welcome {name}")
    player = Player(name)
    if player.profession == "warrior":
        player.power *= 2 
    else:
        player.hp +=10
    print(player.details)
    return player

def choose_random_monster():
    random_monster = random.choice([Orc(), Goblin])
    return random_monster

def dice(sides):
    dice = random.randint(1,sides)
    return dice

def battle(player, monster):
    while player.hp > 0 and monster.hp > 0:
        player_first_dice = dice(6)
        moster_first_dice = dice(6)
        attacker = None
        attacked = None

        if player_first_dice > moster_first_dice:
            attacker = player
            attacked = monster
        else: 
            attacker = monster
            attacked = player
        print(f"the attacke now is {attacker.speak()}")
        if attacker == player:
            input("press on any key when you ready to attcak...")
        attacker_dice = random.randint(1, 20)
        attacker_dice += attacker.speed
        if attacker_dice > attacked.armor_rating:
            attack = attacker.attack()
            attacked.hp -= attack
            if attacker == player:
                print("you hit the monster, good job :)")
            else:
                print("the monster hit you :(")
            attacker,attacked = attacked,attacker
        else:
            if attacker == player:
                print("oh on, you mised :(")
            else:
                print("the monster mised you, what a lock")
            attacker,attacked = attacked,attacker
        if player.hp == 0:
            return "win"
    return "lots"
        
        
class Game:
    def start():
        def show_menu():
            choose =input ("press: \n s = strat \n e = exit \n choose one option:")
            return choose
        if show_menu() == "s":
            player =  create_player()
            monster = choose_random_monster()
            loop_battle = battle(player, monster)
            if loop_battle == "win":
                print("congratulation, you win 🎉")
            else:
                print("sorry you lost :(")
        elif show_menu() == "e":
            make_sure = input("i thought you were brave \n are you sure you want to go out(y/n)?")
            if make_sure == "y":
                print("Ha Ha, coward get out of here")
            else:
                print("invalid press")
                show_menu()