import random
class Goblin:
    def __init__(self):
        self.name = "goblin"
        self.type = "goblin"
        self.hp = 20
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
        self.weapon = ["knife", "sword", "axe"]

    def speak(self):
        speak = "the darknest orc"
        return speak
    
    def attack(self):
        attack_dice = random.randint(1, 6)
        attack_dice += self.power
        if self.weapon == "knife":
            attack_dice *= 0.5
        elif self.weapon == "axe":
            attack_dice *= 1.5
        return attack_dice


        