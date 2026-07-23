class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health

# TODO: Create Superhero instances
sup_batman = SuperHero("Batman", "Intelligence", 100)
sup_superman = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(sup_batman.name)
print(sup_batman.power)
print(sup_batman.health)
print(sup_superman.name)
print(sup_superman.power)
print(sup_superman.health)