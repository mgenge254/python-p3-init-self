

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed


Rex = Dog("Rex", "Rotweilar" )
print(f"My dog is called {Rex.name} and it's a {Rex.breed}")

Snoopy = Dog("Snoopy")
print(f"My dog is called {Snoopy.name} and it's a {Snoopy.breed}")
        