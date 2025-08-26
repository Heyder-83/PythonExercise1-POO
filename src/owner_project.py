import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Owner:
    """
    Clase Owner representa a un dueño que puede tener varios animales.
    """
    def __init__(self, name: str):
        self.name = name
        self.pets = []  # Lista de animales
        logging.info(f"Hola {self.name}.")

    def add_pet(self, pet):
        """
        Agregar una mascota a la lista de pets.
        """
        self.pets.append(pet)
        logging.info(f"{self.name} ahora tiene a {pet.name} como mascota.")

    def feed_all(self):
        """
        Alimenta a todas las mascotas del dueño.
        """
        if not self.pets:
            print(f"{self.name} no tiene mascotas que alimentar.")
            return

        print(f"{self.name} está alimentando a sus mascotas:")
        for pet in self.pets:
            print(f" - {pet.name} está comiendo")
            logging.info(f"{pet.name} ha sido alimentado.")

if __name__ == "__main__":
    from dog_project import Dog
    from cat_project import Cat
    from bird_project import Parrot

    owner1 = Owner("Heyder")

    dog = Dog("Buddy", 2)
    cat = Cat("Whiskers", 3)
    parrot = Parrot("Lola", 1)

    owner1.add_pet(dog)
    owner1.add_pet(cat)
    owner1.add_pet(parrot)

    owner1.feed_all()
