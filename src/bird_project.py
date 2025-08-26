"""
Proyecto: Ejemplo de herencia en POO con aves.
Este archivo define la clase Bird y la clase Eagle que hereda de Bird.
Incluye logging y comentarios explicativos sobre herencia.
"""
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Bird:
    """
    Clase base Bird representa el concepto general de un ave.
    En POO, una clase base puede ser heredada por otras clases más específicas.
    """
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        logging.info(f"Se ha creado un ave de especie {self.species} llamada {self.name} de {self.age} años.")


    def __str__(self):
        return f"Ave: {self.name}, {self.age} años, especie {self.species}"


    def sing(self):
        """
        Método que representa el canto del ave.
        """
        logging.info(f"{self.name} está cantando.")
        print(f"{self.name}: ¡Pío pío!")


    def birthday(self):
        self.age += 1
        logging.info(f"{self.name} ahora tiene {self.age} años.")
    
    def migrate(self):
        """
        Metodo que representa la migracion del ave.
        """
        logging.info(f"{self.name} está migrando.")
        print(f"{self.name}: Me vole pa' otro lado")

# Ejemplo de herencia: Eagle hereda de Bird
class Eagle(Bird):
    """
    Clase Eagle hereda de Bird.
    En POO, la herencia permite que una clase hija obtenga atributos y métodos de la clase padre.
    """
    def __init__(self, name: str, age: int, altitude: float):
        # Llama al constructor de Bird con especie fija "Águila"
        super().__init__(name, age, "Águila")
        self.altitude = altitude
        logging.info(f"Se ha creado un águila llamada {self.name}, a {altitude} metros de altura.")

    def fly(self):
        """
        Método propio de Eagle, además de los heredados de Bird.
        """
        logging.info(f"{self.name} está volando alto.")
        print(f"{self.name}: ¡Estoy volando alto!")
    
    def show_altitude(self):
        """
        Método propio para mostrar la altitud de eagle.
        """
        logging.info(f"{self.name} está volando a {self.altitude} metros de altura.")
        print(f"{self.name}: ¡Estoy volando a {self.altitude} metros de altura!")

class Parrot(Bird):
    """
    Clase Parrot hereda de Bird.
    """
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Loro")
        logging.info(f"Se ha creado un loro llamado {self.name}.")

    def speak(self):
        """
        Método propio de Parrot.
        """
        logging.info(f"{self.name} está hablando.")
        print(f"{self.name}: ¿Quiere cacao?")

if __name__ == "__main__":

    # Creamos una instancia de Eagle
    Eagle1 = Eagle("Pablo", 6, 82)

    # Llamamos al metodo de bird aplicandolo en Eagle1
    Eagle1.birthday()

    # Creamos una instancia de Parrot
    parrot1 = Parrot("Lola", 3)
    parrot1.speak()

    # Llamamos al metodo que muestra la altitud del ave
    Eagle1.show_altitude()

    # Hacemos migrar al ave
    Eagle1.migrate()
    parrot1.migrate()