import os
import json
import random
from datetime import date



FILENAME_DATA_1 = 'customer.json'
Filename_DATA_2 = 'car_inventory.json'
filename_DDATA_3 = 'reservation.json'

class Costumer:
    def __init__(self, id, name, lastname, email, phone):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
    


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
            'phone': self.phone

        }
    def from_dict(data):
        return Costumer(data['id'], data['name'], data['lastname'], data['email'], data['phone'])
    

class Reservation:
    def __init__(self, id, customer_id, car_id, start_date, end_date, total):
        self.id = id
        self.customer_id = customer_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.total = total

        def to_dict(self):
            return {
                'id': self.id,
                'customer_id': self.customer_id,
                'car_id': self.car_id,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'total': self.total
            }
        def from_dict(data):
            return Reservation(data['id'], data['customer_id'], data['car_id'], data['start_date'], data['end_date'], data['total'])

class Inventario:
    def __init__(self, id, marca, modelo, year, precio, disponible):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.precio = precio
        self.disponible = disponible
    



    def to_dict(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'year': self.year,
            'precio': self.precio,
            'disponible': self.disponible
            

        }
    def from_dict(data):

        return Inventario(data['id'], data['marca'], data['modelo'], data['year'], data['precio'], data['disponible'])



def load_data():
    if not os.path.exists(FILENAME_DATA_1):
        with open(FILENAME_DATA_1, 'w') as file:
            json.dump([], file)
        return []

    with open(FILENAME_DATA_1, 'r') as file:
        return [Costumer.from_dict(p) for p in json.load(file)]

def load_reservation():
    if not os.path.exists(filename_DDATA_3):
        with open(filename_DDATA_3, 'w') as file:
            json.dump([], file)
        return []
    with open(filename_DDATA_3, 'r') as file:
        return [Reservation.from_dict(p) for p in json.load(file)]
    
def save_reservation(data):
    with open(filename_DDATA_3, 'w') as file:
        json.dump([p.to_dict() for p in data], file, indent=2)


def save_data(data):

    with open(FILENAME_DATA_1, 'w') as file:
        json.dump([p.to_dict() for p in data], file, indent=2)


def load_inventario():
    if not os.path.exists(Filename_DATA_2):
        with open(Filename_DATA_2, 'w') as file:
            json.dump([], file)
        return []

    with open(Filename_DATA_2, 'r') as file:
        return [Inventario.from_dict(p) for p in json.load(file)]

def save_inventario(data):
    with open(Filename_DATA_2, 'w') as file:
        json.dump([p.to_dict() for p in data], file, indent=2)


def add_customer(customers):
    
    if customers:
        new_id = max(customer.id for customer in customers) + 1
    else:
        new_id = 1
    name = input('Ingrese el nombre del cliente: ')
    lastname = input('Ingrese el apellido del cliente: ')
    email = input('Ingrese el email del cliente: ') 
    phone = input('Ingrese el telefono del cliente: ')
    customers.append(Costumer(new_id, name, lastname, email, phone))

    save_data(customers)
    print('Cliente registrado con exito!')

def show_customers():
    customers = load_data() 
    if not customers:
        print('No hay clientes registrados')
        return
    print('Lista de clientes:')
    for customer in customers:
        print(f'{customer.id} - {customer.name} {customer.lastname} - {customer.email} - {customer.phone}') 


def search_customer():
    customers = load_data()
    if not customers:
        print('No hay clientes registrados')
        return
    print('Lista de clientes:')
    for customer in customers:
        print(f'{customer.id} - {customer.name} {customer.lastname} - {customer.email} - {customer.phone}')

    costumer_id = int(input('Ingrese el id del cliente: '))
    for customer in customers:
        if customer.id == costumer_id:
            print(f'{customer.id} - {customer.name} {customer.lastname} - {customer.email} - {customer.phone}')
            return customer

    print('Cliente no encontrado')

def modify_customer():
    customer = search_customer()
    if not customer:
        return
    customer.name = input('Ingrese el nuevo nombre del cliente: ')
    customer.lastname = input('Ingrese el nuevo apellido del cliente: ')
    customer.email = input('Ingrese el nuevo email del cliente: ')
    customer.phone = input('Ingrese el nuevo telefono del cliente: ')


def add_inventario(marca, modelo, year, precio, disponible):
    inventario = load_inventario()
    if inventario:
        new_id = max(inventario.id for inventario in inventario) + 1
    else:
        new_id = 1
    marca = input('Ingrese la marca del auto: ')
    modelo = input('Ingrese el modelo del auto: ')
    year = input('Ingrese el año del auto: ')
    precio = input('Ingrese el precio del auto: ')
    disponible = input('Ingrese si el auto esta disponible: ')
    inventario.append(Inventario(new_id, marca, modelo, year, precio, disponible))

    save_inventario(inventario)
    print('Auto registrado con exito!')

def menu_principal():
    while True:
        print('Menu principal')
        print('1. Menu de clientes')
        print('2. Menu de inventario')
        print('3. Salir')
        option = input('Ingrese una opcion: ')
        

        

        if option == '1':
            
            menu_customers()

        elif option == '2':
            
            menu_inventory()

       
        elif option == '3':
            print('Gracias por usar el sistema')
            break

        else:
            print('Opcion invalida')
    

def menu_customers():
    customers = load_data()
    while True:
        print('Menu de clientes')
        print('1. Registrar cliente')
        print('2. Buscar cliente')
        print('3. Modificar cliente')
        print('4. Mostrar clientes')
        print('5. Regresar')
        option = input('Ingrese una opcion: ')
        os.system('cls')

        if option == '1':
            add_customer(customers)
        elif option == '2':
            search_customer()
        elif option == '3':
            modify_customer()
        elif option == '4':
            show_customers()
        elif option == '5':
            
            break
        else:
            print('Opcion invalida')

def menu_inventory():
    while True:
        print('Menu de inventario') 
        print('1. Registrar auto')
        print('2. Buscar auto')
        print('3. Modificar auto') 
        print('4. Regresar')
        option = input('Ingrese una opcion: ')
        os.system('cls')
        
        if option == '1':
            add_inventario()
        elif option == '2':
            search_inventario()
        elif option == '3':
            modify_inventario()
        elif option == '4':
            1
            break
        else:
            print('Opcion invalida')


menu_principal()
        