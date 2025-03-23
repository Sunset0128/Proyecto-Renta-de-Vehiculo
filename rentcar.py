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
            'start_date': self.start_date.strftime('%Y-%m-%d'), 
            'end_date': self.end_date.strftime('%Y-%m-%d'),      
            'total': self.total
        }

    #Modificado por Migue
    def from_dict(data):
        try:
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
            end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
            return Reservation(
            data['id'],
            data['customer_id'],
            data['car_id'],
            data.get('customer_name', ''),  
            data.get('customer_lastname', ''),
            data.get('auto_name', ''),  
            data.get('auto_model', ''),  
            start_date,
            end_date,
            data['total']
        )
        except KeyError as e:
            print(f"Error: Falta la clave {e} en los datos de la reservación.")
        return None  

class Inventario:
    def __init__(self, id, marca, modelo, year, precio, color, disponible=True):
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
        return []
    try:
        with open(FILENAME_DATA_1, 'r') as file:
            data = json.load(file)
            customers = []
            for p in data:
                # Modificado por Migue
                if all(key in p for key in ['id', 'name', 'lastname', 'email', 'phone']):
                    customers.append(Costumer.from_dict(p))
                else:
                    print(f"Cliente inválido omitido: {p}")
            return customers
    except Exception as e:
        print(f"Error al cargar clientes: {e}")
        return []


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
        new_id = max(auto.id for auto in inventario) + 1
    else:
        new_id = 1

    marca = input('Ingrese la marca del auto: ')
    modelo = input('Ingrese el modelo del auto: ')
    year = input('Ingrese el año del auto: ')
    precio = input('Ingrese el precio del auto: ')
    color = input('Ingrese el color del auto: ') 
    disponible = True  #Modificado por Migue, si se esta registrando por defecto el auto debe estar disponible

    inventario.append(Inventario(new_id, marca, modelo, year, precio, color, disponible))

    save_inventario(inventario)
    print('Auto registrado con éxito!')

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


def modify_inventario(inventario):
    print("Iniciando modificación del inventario...")
    auto = search_inventario(inventario)
    
    if not auto:
        print("No se encontró el auto para modificar.")
        return

    print("Auto encontrado, procediendo a la modificación...")
    auto.marca = input('Ingrese la nueva marca del auto: ')
    auto.modelo = input('Ingrese el nuevo modelo del auto: ')
    auto.year = input('Ingrese el nuevo año del auto: ')
    auto.precio = input('Ingrese el nuevo precio del auto: ')
    auto.color = input('Ingrese el nuevo color del auto: ')
    
    disponible_input = input('¿Está el auto disponible? (s/n): ').lower()
    auto.disponible = True if disponible_input == 's' else False

    save_inventario(inventario)
    print('Auto modificado con éxito!')

def add_reservation(reservations):
    fecha = date.today()
    customers = load_data()
    inventario = load_inventario()
    
    if not customers:
        print('No hay clientes registrados')
        return
    
    show_customers(customers)

    customer_id = int(input('Ingrese el id del cliente: '))
    customer = next((c for c in customers if c.id == customer_id), None)
    if not customer:
        print('Cliente no encontrado')
        return

    if not inventario:
        print('No hay autos registrados')
        return
    
    show_inventario(inventario)

    auto_id = int(input('Ingrese el id del auto: '))
    auto = next((a for a in inventario if a.id == auto_id), None)
    if not auto:
        print('Auto no encontrado')
        return
    if not auto.disponible:
        print('El auto no está disponible para alquilar.')
        return

    end_date = input('Ingrese la fecha de fin de la reservacion(YYYY-MM-DD): ')
    start_date = datetime.strptime(str(fecha), '%Y-%m-%d')
    end_date = datetime.strptime(str(end_date), '%Y-%m-%d')
    dias = (end_date - start_date).days
    total = dias * int(auto.precio)

    new_id = max((r.id for r in reservations), default=0) + 1
    reservations.append(Reservation(new_id, customer.id, auto.id, customer.name, customer.lastname, auto.marca, auto.modelo, start_date, end_date, total))
    
    auto.disponible = False
    save_inventario(inventario)  
    save_reservation(reservations)
    print('Reservacion registrada con exito!')

#Modificado por Migue
def return_car(reservations):
    if not reservations:
        print('\nNo hay reservaciones activas')
        return
    
    print('\n=== DEVOLUCIÓN DE VEHÍCULO ===')
    show_reservation(reservations)
    
    try:
        reservation_id = int(input('\nIngrese el ID de la reservación a devolver: '))
        reservation = next((r for r in reservations if r.id == reservation_id), None)
        
        if reservation:
            print(f'\nDatos de la reservación:')
            print(f'Cliente: {reservation.customer_name} {reservation.customer_lastname}')
            print(f'Vehículo: {reservation.auto_name} {reservation.auto_model}')
            print(f'Total pagado: ${reservation.total:,}')
            
            confirmar = input('\n¿Confirmar devolución? (s/n): ').lower()
            if confirmar == 's':
                
                print('\nVehículo devuelto exitosamente!')
            else:
                print('\nDevolución cancelada')
        else:
            print('\nReservación no encontrada')
            
    except ValueError:
        print('\nError: Debe ingresar un número válido para el ID')

#Modificado por Migue
def show_reservation(reservations):
    if not reservations:
        print('No hay reservaciones registradas')
        return
    
    print('\n=== LISTA DE RESERVACIONES ===')
    for reservation in reservations:
        print(f"""
        Reservación ID: {reservation.id}
        Cliente: {reservation.customer_name} {reservation.customer_lastname} (ID: {reservation.customer_id})
        Vehículo: {reservation.auto_name} {reservation.auto_model} (ID: {reservation.car_id})
        Fecha Inicio: {reservation.start_date.strftime('%Y-%m-%d')}
        Fecha Entrega: {reservation.end_date.strftime('%Y-%m-%d')}
        Total: ${reservation.total:,}
        ------------------------------------------""")

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

#Modificado por Migue 22/3/2025
def modify_reservation(reservations):
    show_reservation(reservations)
    reservation_id = int(input('Ingrese el ID de la reservación a modificar: '))
    reservation = next((r for r in reservations if r.id == reservation_id), None)
    
    if not reservation:
        print('Reservación no encontrada')
        return

    reservation.customer_id = input('Ingrese el nuevo id del cliente: ')
    reservation.car_id = input('Ingrese el nuevo id del auto: ')
    
    new_start_date = input('Ingrese la nueva fecha de inicio de la reservación (YYYY-MM-DD): ')
    new_end_date = input('Ingrese la nueva fecha de fin de la reservación (YYYY-MM-DD): ')
    
    try:
        reservation.start_date = datetime.strptime(new_start_date, '%Y-%m-%d')
        reservation.end_date = datetime.strptime(new_end_date, '%Y-%m-%d')
        
        
        dias = (reservation.end_date - reservation.start_date).days
        reservation.total = dias * int(reservation.total / (reservation.end_date - reservation.start_date).days)  # Assuming the total was calculated based on days
        
    except ValueError:
        print('Error: Formato de fecha inválido. Asegúrese de usar el formato YYYY-MM-DD.')
        return

    print('Reservación modificada con éxito!')

def reporte(reservations):
    if not reservations:
        print('No hay reservaciones registradas')
        return
    total_de_reservaciones = len(reservations)
    total_de_ingresos = sum(reservation.total for reservation in reservations)
    print('=================REPORTES DE RESERVACIONES=================')
    print(f'Total de reservaciones: {total_de_reservaciones}')
    print(f'Total de ingresos: ${total_de_ingresos}')
        
def menu_principal():
    while True:
        print('Menu principal')
        print('1. Menu de clientes')
        print('2. Menu de inventario')
        print("3. Menu de reservaciones")
        print('4. Salir')
        option = input('Ingrese una opcion: ')
        os.system('cls')
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
        os.system('cls')  #Modificado por Migue

        if option == '1':
            add_customer(customers)
        elif option == '2':
            search_customer(customers)
        elif option == '3':
            modify_customer(customers)
        elif option == '4':
            show_customers(customers)  
        elif option == '5':
            break
        else:
            print('Opcion invalida')

# Modificado por Migue
def menu_reservation():
    reservations = load_reservation()
    while True:
        
        print('Menu de reservaciones')
        print('1. Realizar reservacion')
        print('2. Buscar reservacion')
        print('3. Modificar reservacion')
        print('4. Devolver auto')
        print('5. Reporte de reservaciones')
        print('6. Regresar')
        option = input('Ingrese una opcion: ')
        os.system('cls')
        if option == '1':
            add_reservation(reservations)
            
        elif option == '2':
            search_reservation(reservations)
            
        elif option == '3':
              # Modificado por Migue
            modify_reservation(reservations)
        elif option == '4':
            return_car(reservations)
        elif option == '5':
            reporte(reservations)
        elif option == '6':
            break
        else:
            print('Opcion invalida')

#Modificado por Migue
def menu_inventory():
    inventario = load_inventario()  
    while True:
        print('Menu de inventario')
        print('1. Registrar auto')
        print('2. Buscar auto')
        print('3. Modificar auto')
        print('4. Regresar')
        option = input('Ingrese una opcion: ')
        os.system('cls')  

        if option == '1':
            add_inventario(inventario)  
        elif option == '2':
            search_inventario(inventario)  
        elif option == '3':
            modify_inventario(inventario)  
        elif option == '4':
            break
        else:
            print('Opcion invalida')
menu_principal()