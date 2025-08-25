from dog_project import Dog
from cat_project import Cat
from bird_project import Bird
from fish_project import Fish


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(animal)


if __name__ == "__main__":
    zoo = Zoo()
    dog = Dog("Buddy", 2)
    cat = Cat("Whiskers", 3)
    bird = Bird("Tweety", 1, "Canario")
    fish = Fish("Nemo", 1, "Beta")

    zoo.add_animal(dog)
    zoo.add_animal(cat)
    zoo.add_animal(bird)
    zoo.add_animal(fish)

    zoo.show_animals()