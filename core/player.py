import random
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)
        self.profession = random.choice(["warrior", "doctor"])
        self.details = [self.name, self.profession, self.hp, self.speed, self.power, self.armor_rating]
    
    def speak(self):
        speak = f"{self.name}"
        return speak

    def attack(self):
        attack_dice = random.randint(1, 6)
        attack_dice += self.power
        return attack_dice