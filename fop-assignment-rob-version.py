## FOP Assignment      ##
## by Rob Frawley 2nd  ##
## 2025/08/04          ##

import random

class Fighter:
    def __init__(self, name = "", health = 250, damage = 100, defense = 25, speed = 100, heal_ability = 50, heal_chance = 0.75):
        self.name = name
        self.health_max = health
        self.health = health
        self.damage = damage
        self.defense = defense
        self.speed = speed
        self.heal_ability = heal_ability
        self.heal_chance = heal_chance

    def attack(self, opponent):
        if not self.is_alive():
            return

        damage = Fighter.calculate_stat_from_range(self.damage) - opponent.defense

        if damage < 0:
            damage = 0

        opponent.health -= damage

        print(f"!! {self.name} attacks {opponent.name} for {damage} damage!")

        opponent.heal()

    def heal(self):
        if random.random() > self.heal_chance:
            print(f"-- {self.name} could not heal.")
            return

        heal_amount = Fighter.calculate_stat_from_range(self.heal_ability)

        self.health += heal_amount

        if self.health > self.health_max:
            self.health = self.health_max

        print(f"++ {self.name} heals for {heal_amount} health!")

    def can_outrun(self, opponent):
        return Fighter.calculate_stat_from_range(self.speed) > Fighter.calculate_stat_from_range(opponent.speed)

    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"-- Fighter (name={self.name}, health={self.health}, damage={self.damage}, defense={self.defense}, speed={self.speed}, state={"alive" if self.is_alive() else "dead"})"

    @staticmethod
    def calculate_stat_from_range(stat, low_bounds_divisor = 2, high_bounds_multiplier = 1.5):
        return random.randint(int(stat / low_bounds_divisor), int(stat * high_bounds_multiplier))


class Arena:
    def __init__(self, contestant1, contestant2):
        self.contestant1 = contestant1
        self.contestant2 = contestant2

    def run_match(self):
        while self.contestant1.is_alive() and self.contestant2.is_alive():
            print("## RUNNING MATCH TURN...")

            if self.contestant1.can_outrun(self.contestant2):
                print(f"~~ {self.contestant1.name} can outrun {self.contestant2.name} ({self.contestant1.name} attacks first).")
                self.contestant1.attack(self.contestant2)
                self.contestant2.attack(self.contestant1)
            else:
                print(f"~~ {self.contestant2.name} can outrun {self.contestant1.name} ({self.contestant2.name} attacks first).")
                self.contestant2.attack(self.contestant1)
                self.contestant1.attack(self.contestant2)

            print(str(self.contestant1))
            print(str(self.contestant2))

        print(f"<> Winner: {self.contestant1.name if self.contestant1.is_alive() else self.contestant2.name}")


def main():
	Fight = Arena(Fighter(input("Enter the name of the 1st fighter: ")), Fighter(input("Enter the name of the 2nd fighter: ")))
	Fight.run_match()


main()