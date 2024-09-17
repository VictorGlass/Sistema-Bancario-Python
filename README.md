
## Sistema Bancario Python 🐍🐍

El proyecto **Sistema Bancario Básico** es una aplicación simple de gestión bancaria en Python. 
Permite crear cuentas bancarias, realizar depósitos, retiros, y mostrar información del titular de la cuenta. 
Está diseñado para demostrar el uso de clases y manejo básico de datos en Python.

## Estructura del Proyecto

El proyecto está dividido en dos archivos principales:

1.  **`persona.py`**: Define la clase `Persona` que almacena información personal del titular de la cuenta.
2.  **`banco.py`**: Define la clase `CuentaBancaria`, importa la clase `Persona`, y proporciona un menú interactivo para gestionar las cuentas bancarias.


## Clases

### `Persona`

-   **Atributos**:
    
    -   `nombre`: Nombre del titular.
    -   `edad`: Edad del titular.
    -   `direccion`: Dirección del titular.
    -   `numero_identificacion`: Número de identificación del titular.
-   **Métodos**:
    
    -   `mostrar_informacion()`: Muestra la información del titular.

### `CuentaBancaria`

-   **Atributos**:
    
    -   `titular`: Objeto de la clase `Persona`.
    -   `saldo`: Saldo inicial de la cuenta.
-   **Métodos**:
    
    -   `depositar(monto)`: Deposita un monto en la cuenta.
    -   `retirar(monto)`: Retira un monto de la cuenta.
    -   `mostrar_saldo()`: Muestra el saldo actual de la cuenta.


## Menú Interactivo

El menú permite al usuario realizar las siguientes acciones:

1.  **Crear una nueva cuenta**: Ingrese los datos del titular y el saldo inicial.
2.  **Depositar dinero**: Añade fondos a la cuenta.
3.  **Retirar dinero**: Retira fondos de la cuenta.
4.  **Mostrar saldo**: Muestra el saldo actual de la cuenta.
5.  **Mostrar información de la persona**: Muestra la información del titular de la cuenta.
6.  **Salir**: Termina el programa.


## Como Ejecutar el Programa


-   **Asegúrate de tener ambos archivos (`persona.py` y `banco.py`) en el mismo directorio.**
    
-   **Ejecuta el archivo `banco.py` desde la línea de comandos:**

        python banco.py
-  **Sigue las instrucciones del menú para interactuar con el sistema bancario.**

## Ejemplo de Uso

--- Menú Bancario ---
1. Crear una nueva cuenta
2. Depositar dinero
3. Retirar dinero
4. Mostrar saldo
5. Mostrar información de la persona
6. Salir

Seleccione una opción: 1

Ingrese el nombre: Ana
Ingrese la edad: 30
Ingrese la dirección: 123 Calle Falsa
Ingrese el número de identificación: AB123456
Ingrese el saldo inicial: 500

Cuenta creada con éxito.

--- Menú Bancario ---
1. Crear una nueva cuenta
2. Depositar dinero
3. Retirar dinero
4. Mostrar saldo
5. Mostrar información de la persona
6. Salir

Seleccione una opción: 2

Ingrese el monto a depositar: 200

Se han depositado 200. Nuevo saldo: 700

...

