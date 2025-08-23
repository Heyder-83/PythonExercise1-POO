"""
Proyecto: Creación de pez usando Programación Orientada a Objetos (POO)
"""
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Fish:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        logging.info(f"Ha ingresado un pez llamado {self.name} de {self.age} años y de la especie {self.species}")

    def swim(self):
        logging.info(f"{self.name} esta nadando")
        print(f"{self.name}: *nadando glu glu glu*")

if __name__ == "__main__":
    fish1 = Fish("Juan", 2, "Beta")

    fish1.swim()

