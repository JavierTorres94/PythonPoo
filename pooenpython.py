# Clase padre
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def comer(self):
        print(f"{self.__nombre} está comiendo.")
        
    def dormir(self):
        print(f"{self.__nombre} está durmiendo.")
        
    # Encapsulamiento
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad
    
    # Abstracción
    def hacer_sonido(self):
        pass

# Clase hija
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza
        
    def ladrar(self):
        print("¡Guau, guau!")
        
    # Encapsulamiento
    def get_raza(self):
        return self.__raza
    
    def set_raza(self, nueva_raza):
        self.__raza = nueva_raza
        
    # Abstracción
    def hacer_sonido(self):
        self.ladrar()

# Instancias
animal1 = Animal("Paco", 5)
perro1 = Perro("Fido", 3, "Labrador")

# Llamando a los métodos
animal1.comer()
perro1.comer()
perro1.ladrar()

# Herencia
print(isinstance(animal1, Animal))
print(isinstance(perro1, Animal))

# Encapsulamiento
print(perro1.get_nombre())
perro1.set_nombre("Max")
print(perro1.get_nombre())

# Abstracción
animal1.hacer_sonido()
perro1.hacer_sonido()
