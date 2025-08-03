
def show_options():
    print('''\n*****************************
***** ELIGE UNA OPCION: *****\n
    1. Agregar contacto.
    2. Mostrar contacto.
    3. Eliminar contacto.
    4. Buscar contacto.
    5. Salir
\n*****************************
*****************************''')
    

contact_list = []

def add_contact():
    name = input('Nombre: ')
    phone = input('Telefono: ')

    new_contact = {
        'name' : name,
        'phone' : phone
    }
    contact_list.append(new_contact)
    print('\nContacto creado\n')

def show_contact():

    if not contact_list:
        print('\nNo hay ningun contacto')
    else:
        print('Contactos guardados:')
        for index, contact in enumerate(contact_list, 1):
            print(f"\n{index}. {contact['name']} - {contact['phone']}")
            
 
def delete_contact():

    delete = input('\nNombre a eliminar: ')

    for contact in contact_list:
        if delete.lower() == contact['name'].lower():
            contact_list.remove(contact)
            print('Contacto eliminado')
            return
    print('\nContacto no encontrado')

def search_contact():

    search = input('\nBuscar contacto: ')
    results = [contact for contact in contact_list if search.lower() in contact['name'].lower()]

    if not results:
        print('\nNo hay nada socio')
    else:
        for contact in results:
            print(f"\nNombre: {contact['name']}")



while True:

    show_options()
    
    input_user = input('\nElige una opción: ')

    if input_user == '1':
        add_contact()
    elif input_user == '2':
        show_contact()
    elif input_user == '3':
        delete_contact()
    elif input_user == '4':
        search_contact()
    elif input_user == '5':
        print('Hasta la proxima!!')
        break
    else:
        print('Opcion no valida')