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