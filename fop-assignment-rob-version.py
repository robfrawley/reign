## FOP Assignment      ##
## by Rob Frawley 2nd  ##
## 2025/08/04          ##

import random

class Fighter:
    def __init__(self, name = "", health = 250, damage = 100, defense = 50, speed = 100, heal_amount = 50, heal_chance = 0.5):
        self.name = name
        self.health_max = health
        self.health = health
        self.damage = damage
        self.defense = defense
        self.speed = speed
        self.heal_amount = heal_amount
        self.heal_chance = heal_chance

    def attack(self, opponent):
        if not self.is_alive():
            return
        
        if opponent.can_outrun(self):
            print(f"~~ {self.name} cannot attack because {opponent.name} outran them!")
            return

        defence = Fighter.calculate_stat_from_range(opponent.defense, 0.25, 1.25)
        damage = max(0, Fighter.calculate_stat_from_range(self.damage) - defence)
        opponent.health -= damage

        print(f"!! {self.name} attacks {opponent.name} for {damage} damage ({opponent.name} defended with {defence})!")

        self.heal()

    def heal(self):
        if random.random() > self.heal_chance:
            print(f"++ {self.name} could not heal!")
            return

        heal_amount = Fighter.calculate_stat_from_range(self.heal_amount)
        self.health = min(self.health + heal_amount, self.health_max)

        print(f"++ {self.name} heals for {heal_amount} health!")

    def can_outrun(self, opponent):
        return Fighter.calculate_stat_from_range(self.speed) > Fighter.calculate_stat_from_range(opponent.speed)

    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"-- Fighter (health={self.health}/{self.health_max}, damage={self.damage}, defense={self.defense}, speed={self.speed}, heal_amount={self.heal_amount}, heal_chance={self.heal_chance}, state={"alive" if self.is_alive() else "dead"}, name={self.name})"

    @staticmethod
    def calculate_stat_from_range(stat, lower_bounds_multiplier = 0.5, upper_bounds_multiplier = 1.5):
        return random.randint(int(stat * lower_bounds_multiplier), int(stat * upper_bounds_multiplier))


class Arena:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def run_match(self):
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            print("## RUNNING MATCH TURN...")

            if random.random() < 0.5:
                Arena.run_match_attacks(self.fighter1, self.fighter2)
            else:
                Arena.run_match_attacks(self.fighter2, self.fighter1)

            print(str(self.fighter1))
            print(str(self.fighter2))

        print(f"<> Winner: {self.fighter1.name if self.fighter1.is_alive() else self.fighter2.name}")

    @staticmethod
    def run_match_attacks(fighter1, fighter2):
        fighter1.attack(fighter2)
        fighter2.attack(fighter1)


def main():
	Fight = Arena(Fighter(input("Enter the name of the 1st fighter: ")), Fighter(input("Enter the name of the 2nd fighter: ")))
	Fight.run_match()


main()