from os import system

class Persona: 

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} | Cuenta: {self.numero_cuenta} | Balance: {self.balance}".title().strip()
    
    def depositar(self):
        dinero_cliente = int(input(f"¿Cuanto dinero quieres agregar a tu cuenta? Balance actual: {self.balance}\n"))
        operacion = dinero_cliente + self.balance
        self.balance = operacion
        print(f"Has depositado {dinero_cliente}. Tu nuevo balance es {operacion}")

    def retirar(self):
        retiro_cliente = int(input(f"¿Cuanto dinero quieres retirar? Balance actual: {self.balance} \n"))
        if retiro_cliente <= self.balance:
            operacion = self.balance - retiro_cliente
            self.balance = operacion
            print(f"Has retirado {retiro_cliente}. Tu nuevo balance es {operacion}")
        else: 
            print(f"No puedes retirar {retiro_cliente}. Tu balance es {self.balance}")
            input("Presiona Enter para regresar al menu")
    

def menu(cliente): 

    while(True):
        system("cls")
        print(cliente.__str__())
        

        eleccion = input("""Escribe que accion quieres realizar:\n
Opcion 1: Retirar
Opcion 2: Depositar
Opcion 3: Salir\n""")
        eleccion = eleccion.lower()

        if eleccion == "salir":
            break

        elif eleccion == "retirar":
            cliente.retirar()

        elif eleccion == "depositar":
            cliente.depositar()
            

menu(Cliente("miguel", "fuentes", 202301585,))