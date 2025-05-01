class Superhero:
    def __init__(self, name, power, secret_identity):
        self.name = name
        self.power = power
        self.__secret_identity = secret_identity  

    def use_power(self):
        print(f"{self.name} uses {self.power}! 💥")

    def introduce(self):
        print(f"I'm {self.name}, defender of justice!")

    def reveal_secret(self):
        print(f"My real identity is {self.__secret_identity}")

# Inheritance example
class Avenger(Superhero):
    def __init__(self, name, power, secret_identity, team):
        super().__init__(name, power, secret_identity)
        self.team = team

    # Polymorphism - overriding introduce method
    def introduce(self):
        print(f"I'm {self.name} from the {self.team} Avengers!")

# Create objects
spidey = Superhero("Spider-Man", "web-slinging", "Peter Parker")
iron_man = Avenger("Iron Man", "tech armor", "Tony Stark", "Original")
