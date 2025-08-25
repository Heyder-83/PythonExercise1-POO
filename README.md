# 🐍 Solucion de retos de POO en Python

## 1️⃣ Crea una clase `Fish` con atributos `name`, `age` y `species`. Agrega un método `swim` que imprima un mensaje.

### Ejemplo de solución

```python
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
```

### Explicación

- Se define la clase `Fish` con los atributos `name`, `age` y `species`.
- El método `swim` imprime un mensaje indicando que el pez está nadando.
- Se muestra cómo crear una instancia y llamar al metodo.

