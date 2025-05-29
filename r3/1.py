class Banana:
    """Representa una banana individual."""
    def eat(self):
        """Simula el acto de comer una banana."""
        print("Comiendo una banana...")

class Person:
    """Representa a una persona que puede tener y comer bananas."""
    def __init__(self):
        """Inicializa una nueva instancia de Persona con cero bananas."""
        print("Persona inicializada.")
        self.banana_count = 0 # Inicializar contador de bananas
        self.no_bananas() # Verificar si no hay bananas al inicio

    def add_banana(self):
        """Añade una banana al contador de la persona."""
        print("Banana agregada.")
        self.banana_count += 1 # Incrementar contador

    def eat_bananas(self):
        """Come todas las bananas que la persona tiene actualmente."""
        
        # Verifica si hay bananas disponibles
        if self.no_bananas():
            return # No hace nada si no hay bananas
        
        print(f"Comiendo {self.banana_count} bananas.")

        # Bucle para comer todas las bananas
        for _ in range(self.banana_count):
            Banana().eat() # Simular comer una banana
            self.banana_count -= 1

    def no_bananas(self):
        """Verifica si la persona no tiene bananas.

        Imprime un mensaje si no hay bananas.

        Retorna:
            bool: True si no hay bananas, False en caso contrario.
        """
        print(f"Verificando si no hay bananas.")
        if self.banana_count == 0:
            print("No quedan bananas.") # Imprimir mensaje si no hay bananas
            return True
        else:
            return False
        

if __name__ == "__main__":
    # Este bloque se ejecuta cuando el script se corre directamente.
    print("Iniciando ejecución principal.")

    # Crear una instancia de Persona
    person = Person() # Esto llama a Person.__init__

    # Simula añadir 10 bananas, como se muestra en el gráfico.
    for _ in range(10):
        person.add_banana()

    # Simula comer todas las bananas que la persona tiene.
    person.eat_bananas()

    print("Ejecución principal finalizada.")