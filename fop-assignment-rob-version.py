## FOP Assignment      ##
## by Rob Frawley 2nd  ##
## 2025/08/04          ##

import random

class Fighter:
    def __init__(self, name = "", hp = 250, pwr = 100, defense = 25, speed = 100):
        self.name = name
        self.hp = hp
        self.pwr = pwr
        self.defense = defense
        self.speed = speed
	
    def attack(self, opponent):
        if not self.is_alive():
            return

        print("=========================") 
        print(f"{self.name.upper()}'S TURN!")
        print("=========================")

        damage = random.randint(int(self.pwr / 2), self.pwr) - opponent.defense

        if damage < 0:
            damage = 0

        opponent.hp -= damage

        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        self.write_stats()
        opponent.write_stats()

    def can_outrun(self, opponent):
        return random.randint(int(self.speed / 2), int(self.speed * 2)) > random.randint(int(opponent.speed / 2), int(opponent.speed * 2))

    def is_alive(self):
        return self.hp > 0
    
    def write_stats(self):
        print(f"Name: {self.name} / HP: {self.hp} / Power: {self.pwr} / Defense: {self.defense} / Speed: {self.speed}")
	
	
class Arena:
    def __init__(self, contestant1, contestant2):
        self.contestant1 = contestant1
        self.contestant2 = contestant2
		
    def run_match(self):
        print("===========ARENA============")
        print("============================")

        while self.contestant1.is_alive() and self.contestant2.is_alive():
            if self.contestant1.can_outrun(self.contestant2):
                print(f"{self.contestant1.name} can outrun {self.contestant2.name}.")
                self.contestant2.attack(self.contestant1)
                self.contestant1.attack(self.contestant2)
            else:
                print(f"{self.contestant1.name} cannot outrun {self.contestant2.name}.")
                print(f"{self.contestant2.name} attacks first!")
                self.contestant2.attack(self.contestant1)
                self.contestant1.attack(self.contestant2)

        print(f"{self.contestant1.name} is {'alive' if self.contestant1.is_alive() else 'dead'}!")
        print(f"{self.contestant2.name} is {'alive' if self.contestant2.is_alive() else 'dead'}!")


def main():
	fighter1 = Fighter(input("Enter the name of the first fighter: "))
	fighter2 = Fighter(input("Enter the name of the second fighter: "))

	
	Fight = Arena(fighter1, fighter2)
	Fight.run_match()
	
	
main()