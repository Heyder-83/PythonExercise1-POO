# 🐍 Solucion de retos de POO en Python

## 1️⃣ Crea una clase `Fish` con atributos `name`, `age` y `species`. Agrega un método `swim` que imprima un mensaje.

### Solución

```python
import logging

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
```

### Explicación

- Se define la clase `Fish` con los atributos `name`, `age` y `species`.
- El método `swim` imprime un mensaje indicando que el pez está nadando.
- Se muestra cómo crear una instancia y llamar al metodo.

## 2️⃣ Modifica la clase `Dog` para agregar un método `fetch` que reciba el nombre de un objeto y lo imprima como si el perro lo trajera.

### Solución

```python
def fetch(self, item: str):
        """
        Este metodo define como se comporta el perro.
        """
        logging.info(f"{self.name} ha traido un/a {item} y lo tiene en el ocico")

# Ejemplo de uso
    # Trae objeto
    dog1.fetch("Media")
    dog2.fetch("Pelota")
```

### Explicación

- Se añade el método `fetch` a la clase `Dog`.
- El método recibe el nombre de un objeto y muestra un mensaje indicando que el perro lo ha traído.
- Se muestra cómo crear una instancia y llamar

## 3️⃣ Crea una clase `Zoo` que pueda almacenar varios animales (instancias de `Dog`, `Cat`, `Bird`, etc.) en una lista y tenga un método para mostrar todos los animales.

### Solución

```python
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
```

### Explicación

- Se crea la clase `Zoo` con una lista para almacenar animales.
- El método `add_animal` permite agregar cualquier instancia de animal.
- El método `show_animals` recorre la lista y muestra cada animal.
- Se muestra cómo crear el zoológico, agregar animales y mostrarlos.

## 4️⃣ Agrega un método `sleep` a la clase `Cat` que imprima que el gato está durmiendo.

### Solución

```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name}: Zzz...")

# Ejemplo de uso
cat1 = Cat("Milo", 2)
cat2 = Cat("Nina", 4)

cat1.sleep()
cat2.sleep()
```

### Explicación

- Se añade el método `sleep` a la clase `Cat`.
- El método imprime que el gato está durmiendo.
- Se muestra cómo crear instancias y llamar al método para

## 5️⃣ Crea una clase `Parrot` que herede de `Bird` y agregue un método `talk` que imprima una frase personalizada.

### Solución

```python
class Parrot(Bird):
    """
    Clase Parrot hereda de Bird.
    """
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Loro")
        logging.info(f"Se ha creado un loro llamado {self.name}.")

    def talk(self, frase):
        """
        Método propio de Parrot que imprime una frase personalizada.
        """
        logging.info(f"{self.name} dice: {frase}")
        print(f"{self.name}: {frase}")

# Ejemplo de uso
if __name__ == "__main__":
    parrot1 = Parrot("Lola", 3)
    parrot1.talk("¡Hola, soy Lola!")
```

### Explicación

- Se crea la clase `Parrot` heredando de `Bird`.
- Se agrega el método `talk` que recibe una frase y la imprime como si el loro hablara.
- Se muestra cómo crear una instancia y llamar al método con una

## 6️⃣ Modifica la clase `Eagle` para agregar un atributo `altitude` y un método que imprima la altitud actual de vuelo.

### Solución

```python
class Eagle(Bird):
    """
    Clase Eagle hereda de Bird.
    """
    def __init__(self, name: str, age: int, altitude: float):
        super().__init__(name, age, "Águila")
        self.altitude = altitude
        logging.info(f"Se ha creado un águila llamada {self.name}, a {altitude} metros de altura.")

    def show_altitude(self):
        """
        Método propio para mostrar la altitud de eagle.
        """
        logging.info(f"{self.name} está volando a {self.altitude} metros de altura.")
        print(f"{self.name}: ¡Estoy volando a {self.altitude} metros de altura!")

# Ejemplo de uso
if __name__ == "__main__":
    Eagle1 = Eagle("Pablo", 6, 82)
    Eagle1.show_altitude()
```

### Explicación

- Se agrega el atributo `altitude` en el constructor de `Eagle`.
- El método `show_altitude` imprime la altitud actual de vuelo del águila.
- Se muestra cómo crear una instancia y llamar al método para

## 7️⃣ Crea una clase `Owner` que pueda tener uno o más animales y un método para alimentar a todos sus animales.

### Solución

```python
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
```

### Explicación

- Se crea la clase `Owner` con una lista de mascotas.
- El método `add_pet` agrega animales a la lista.
- El método `feed_all` recorre la lista y alimenta a cada mascota.
- Se muestra cómo crear un dueño, agregar mascotas y alimentarlas.

## 9️⃣ Crea una clase `Veterinarian` con un método `checkup` que reciba un animal y le imprima un mensaje de revisión.

### Ejemplo de solución

```python
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
```

### Explicación

- Se crea la clase `Veterinarian` con un método `checkup`.
- El método recibe un animal y muestra un mensaje de revisión.
- Se muestra cómo crear un veterinario

## 🔟 Haz que la clase `Bird` tenga un método `migrate` que imprima que el ave está migrando a otro lugar.

### Ejemplo de solución

```python
    def migrate(self):
        """
        Metodo que representa la migracion del ave.
        """
        logging.info(f"{self.name} está migrando.")
        print(f"{self.name}: Me vole pa' otro lado")

    # Hacemos migrar al ave
    Eagle1.migrate()
    parrot1.migrate()
```

### Explicación

- Se agrega el método `migrate` a la clase `Bird`.
- El método imprime que el ave está migrando a otro lugar.
- Se muestra cómo crear una instancia y llamar al metodo.