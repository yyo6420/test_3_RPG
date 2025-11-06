import random
class Orc:
    def __init__(self):
        self.name = "orc"
        self.type = "orc"
        self.hp = 50
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
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

