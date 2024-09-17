
from persona import Persona


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"\nSe han depositado {monto}. Nuevo saldo: {self.saldo}")
        else:
            print("\El monto debe ser positivo.")
    
    def retirar(self, monto):
        if monto > 0:
            if self.saldo >= monto:
                self.saldo -= monto
                print(f"\nSe han retirado {monto}. Nuevo saldo: {self.saldo}")
            else:
                print("\nFondos insuficientes.")
        else:
            print("\nEl monto debe ser positivo")
    
    def mostrar_saldo(self):
        print(f"\nSaldo actual: {self.saldo}")

def mostrar_menu():
    print("\n--- Menú Bancario ---")
    print("1. Crear una nueva cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar saldo")
    print("5. Mostrar información de la persona")
    print("6. Salir") 

def main():
    cuenta = None

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ")

        if opcion == '1':
            #Creamos una nueva cuenta
            nombre = input("\nIngrese el nombre: ")
            edad = int(input("Ingrese la edad: "))
            direccion = input("Ingrese la direccion: ")
            numero_id = input("Ingrese el numero de identificacion: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))

            #Creamos una instancia de Persona y CuentaBancaria.
            persona = Persona(nombre, edad, direccion, numero_id)
            cuenta = CuentaBancaria(titular=persona, saldo_inicial=saldo_inicial)
            print("\nCuenta creada con exito.")
        
        elif opcion == '2':
            #Depositar dinero.
            if cuenta:
                monto = float(input("\nIngrese el monto a depositar: "))
                cuenta.depositar(monto)
            else:
                print("\nPrimero debe crear una cuenta.")
        
        elif opcion == '3':
            #Retirar dinero.
            if cuenta:
                monto = float(input("\nIngrese el monto a retirar: "))
                cuenta.retirar(monto)
            else:
                print("\nPrimero debe crear una cuenta.")
        
        elif opcion == '4':
            #Mostrar saldo
            if cuenta:
                cuenta.mostrar_saldo()
            else:
                print("\nPrimero debe crear una cuenta.")
        
        elif opcion == '5':
            #Mostrar informacion de la persona.
            if cuenta:
                cuenta.titular.mostrar_informacion()
            else:
                print("\nPrimero debe crear una cuenta.")
        
        elif opcion == '6':
            #Salir.
            print("\nGracias por usar el sistema bancario. Adios!")
            break
        else:
            print("\nOpcion no valida. Por favor, seleccione una opcion del 1 al 6.")

if __name__ == '__main__':
    main()