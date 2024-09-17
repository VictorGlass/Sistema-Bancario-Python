class Persona:
    def __init__(self, nombre, edad, direccion, numero_id):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numero_id = numero_id
    
    def mostrar_informacion(self):
        print("\nInformacion de la persona: ")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Direccion: {self.direccion}")
        print(f"Numero de identificacion: {self.numero_id}")
