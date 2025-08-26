import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Veterinarian:
    """
    Clase Veterinarian representa a un veterinario que puede hacer chequeos a los animales.
    """
    def __init__(self, name: str):
        self.name = name
        logging.info(f"El veterinario {self.name} se ha registrado.")

    def checkup(self, animal):
        """
        Revisa al animal.
        """
        print(f"El veterinario {self.name} está revisando a {animal.name}.")
        logging.info(f"{animal.name} ha sido revisado por {self.name}.")

if __name__ == "__main__":
    from dog_project import Dog
    from cat_project import Cat

    vet = Veterinarian("Dr. Juan")

    dog = Dog("Rex", 4)
    cat = Cat("Misu", 2)

    vet.checkup(dog)
    vet.checkup(cat)
