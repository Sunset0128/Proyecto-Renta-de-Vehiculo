import os
import json
import random
from datetime import date, datetime

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
    def __init__(self, id, customer_id, car_id, customer_name, customer_lastname, auto_name, auto_model, start_date, end_date, total):
        self.id = id
        self.customer_id = customer_id
        self.car_id = car_id
        self.customer_name = customer_name
        self.customer_lastname = customer_lastname
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.start_date = start_date
        self.end_date = end_date
        self.total = total

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'car_id': self.car_id,
            'customer_name': self.customer_name,
            'customer_lastname': self.customer_lastname,
            'start_date': str(self.start_date),
            'end_date': self.end_date,
            'total': self.total
        }

    def from_dict(data):
         return Reservation(data['id'], data['customer_id'], data['car_id'], data['customer_name'],data['customer_lastname'], data['start_date'], data['end_date'],
                               data['total'])


class Inventario:
    def __init__(self, id, marca, modelo, year, precio, color, disponible):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.precio = precio
        self.color = color
        self.disponible = disponible

    def to_dict(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'year': self.year,
            'precio': self.precio,
            'color': self.color,
            'disponible': self.disponible

        }

    def from_dict(data):
        return Inventario(data['id'], data['marca'], data['modelo'], data['year'], data['precio'], data['color'], data['disponible'])


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


def show_customers(customers):

    if not customers:
        print('No hay clientes registrados')
        return
    print('Lista de clientes:')
    for customer in customers:
        print(f'{customer.id} - {customer.name} {customer.lastname} - {customer.email} - {customer.phone}')


def search_customer(customers):

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


def modify_customer(customers):
    customer = search_customer(customers)
    if not customer:
        return
    customer.name = input('Ingrese el nuevo nombre del cliente: ')
    customer.lastname = input('Ingrese el nuevo apellido del cliente: ')
    customer.email = input('Ingrese el nuevo email del cliente: ')
    customer.phone = input('Ingrese el nuevo telefono del cliente: ')


def add_inventario(inventario):

    if inventario:
        new_id = max(inventario.id for inventario in inventario) + 1
    else:
        new_id = 1
    marca = input('Ingrese la marca del auto: ')
    modelo = input('Ingrese el modelo del auto: ')
    year = input('Ingrese el año del auto: ')
    precio = input('Ingrese el precio del auto: ')
    color = input('Ingrese el color del auto:' )
    disponible = input('Ingrese si el auto esta disponible: ')
    inventario.append(Inventario(new_id, marca, modelo, year, precio, disponible))

    save_inventario(inventario)
    print('Auto registrado con exito!')


def show_inventario(inventario):

    if not inventario:
        print('No hay autos registrados')
        return
    print('Lista de autos:')
    for auto in inventario:
        print(f'{auto.id} - {auto.marca} {auto.modelo} - {auto.year} - {auto.precio} - {auto.color} - {auto.disponible}')


def search_inventario(inventario):

    if not inventario:
        print('No hay autos registrados')
        return
    print('Lista de autos:')
    for auto in inventario:
        print(f'{auto.id} - {auto.marca} {auto.modelo} - {auto.year} - {auto.precio} - {auto.color} - {auto.disponible}')

    auto_id = int(input('Ingrese el id del auto: '))
    for auto in inventario:
        if auto.id == auto_id:
            print(f'{auto.id} - {auto.marca} {auto.modelo} - {auto.year} - {auto.precio} - {auto.color} - {auto.disponible}')
            return auto

    print('Auto no encontrado')


def modify_inventario():
    auto = search_inventario()
    if not auto:
        return
    auto.marca = input('Ingrese la nueva marca del auto: ')
    auto.modelo = input('Ingrese el nuevo modelo del auto: ')
    auto.year = input('Ingrese el nuevo año del auto: ')
    auto.precio = input('Ingrese el nuevo precio del auto: ')
    auto.color = input('Ingrese el color del auto: ')
    auto.disponible = input('Ingrese si el auto esta disponible: ')


def add_reservation(reservation):
    fecha = date.today()
    customers = load_data()
    inventario = load_inventario()
    if not customers:
        print('No hay clientes registrados')
        return
    else:
    
        show_customers(customers)

    customer_id = int(input('Ingrese el id del cliente: '))
    for customer in customers:
        if customer_id != customer.id:
            print('Cliente no encontrado')
            add_customer(customers)
        else:
            customer_name = customer.name
            customer_lastname = customer.lastname

    
    if not inventario:
        print('No hay autos registrados')
    else:
        show_inventario(inventario)
    
    auto_id = int(input('Ingrese el id del auto: '))
    for auto in inventario:
        if auto_id != auto.id:
            print('Auto no encontrado')
            return
        else:
            auto_name = auto.marca
            auto_model = auto.modelo
    
    start_date = fecha
    end_date = input('Ingrese la fecha de fin de la reservacion(YYYY-MM-DD): ')
    start_date = datetime.strptime(str(start_date), '%Y-%m-%d')
    end_date = datetime.strptime(str(end_date), '%Y-%m-%d')
    dias = end_date - start_date
    dias = dias.days
    total = dias * int(auto.precio)
    
    reservation = load_reservation()
    if reservation:
        new_id = max(reservation.id for reservation in reservation) + 1
    else:
        new_id = 1
    reservation.append(Reservation(new_id, customer.id, auto.id, customer_name, customer_lastname,auto_name, auto_model, start_date, end_date, total))
    save_reservation(reservation)
    print('Reservacion registrada con exito!')

def show_reservation(reservations):
    
    if not reservations:
        print('No hay reservaciones registradas')
        return
    print('Lista de reservaciones:')
    for reservation in reservations:
        print(
            f'Reservacion id: {reservation.id} - Cliente Id: {reservation.customer_id} - Auto Id: {reservation.car_id} - Fecha Inicio: {reservation.start_date} - Fecha Entrega: {reservation.end_date} - Total: {reservation.total}')


def search_reservation(reservations):
    
    if not reservations:
        print('No hay reservaciones registradas')
        return
    print('Lista de reservaciones:')
    for reservation in reservations:
        print(
            f'Reservacion id: {reservation.id}\n - Cliente Id: {reservation.customer_id}\n - Auto Id: {reservation.car_id}\n - Nombre del CLiente: {reservation.customer_name}\n - Apellido: {reservation.customer_lastname}\n - Fecha Inicio: {reservation.start_date}\n - Fecha Entrega: {reservation.end_date}\n - Total: {reservation.total}')

    reservation_id = int(input('Ingrese el id de la reservacion: '))
    for reservation in reservations:
        if reservation.id == reservation_id:
            print(
                f'{reservation.id} - {reservation.customer_id} {reservation.car_id} - {reservation.start_date} - {reservation.end_date} - {reservation.total}')
            return reservations


def modify_reservation(reservations):
    show_reservation(reservations)
    reservations = search_reservation(reservations)
    if not reservations:
        return
    reservations.customer_id = input('Ingrese el nuevo id del cliente: ')
    reservations.car_id = input('Ingrese el nuevo id del auto: ')
    reservations.start_date = input('Ingrese la nueva fecha de inicio de la reservacion: ')
    reservations.end_date = input('Ingrese la nueva fecha de fin de la reservacion: ')
    reservations.total = input('Ingrese el nuevo total de la reservacion: ')



def menu_principal():
    while True:
        print('Menu principal')
        print('1. Menu de clientes')
        print('2. Menu de inventario')
        print("3. Menu de reservaciones")
        print('4. Salir')
        option = input('Ingrese una opcion: ')

        if option == '1':

            menu_customers()

        elif option == '2':

            menu_inventory()

        elif option == '3':
            menu_reservation()


        elif option == '4':
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


def menu_reservation():
    reservations = load_reservation()
    while True:
        print('Menu de reservaciones')
        print('1. Realizar reservacion')
        print('2. Buscar reservacion')
        print('3. Modificar reservacion')
        print('4. Regresar')
        option = input('Ingrese una opcion: ')
        os.system('cls')

        if option == '1':
            add_reservation(reservations)
        elif option == '2':
            search_reservation(reservations)
        elif option == '3':
            modify_reservation(reservations)
        elif option == '4':
            break


def menu_inventory():
    invetario = load_inventario()
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
