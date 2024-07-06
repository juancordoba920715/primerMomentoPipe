
usuarios = []
prestamos = []

def agregar_usuario(nombre):
    usuario = {
        'nombre': nombre,
        'prestamos': []
    }
    usuarios.append(usuario)
    print(f"Usuario '{nombre}' agregado.")

def listar_usuarios():
    print("Usuarios:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario['nombre']}")

def agregar_prestamo(usuario_nombre, cantidad, descripcion):
    for usuario in usuarios:
        if usuario['nombre'] == usuario_nombre:
            prestamo = {
                'cantidad': cantidad,
                'descripcion': descripcion
            }
            usuario['prestamos'].append(prestamo)
            prestamos.append(prestamo)
            print(f"Préstamo de {cantidad} para '{descripcion}' agregado a usuario '{usuario_nombre}'.")
            return
    print(f"Usuario '{usuario_nombre}' no encontrado.")

def listar_prestamos():
    print("Préstamos:")
    for i, prestamo in enumerate(prestamos, start=1):
        print(f"{i}. {prestamo['cantidad']} - {prestamo['descripcion']}")

def listar_prestamos_usuario(usuario_nombre):
    for usuario in usuarios:
        if usuario['nombre'] == usuario_nombre:
            print(f"Préstamos de '{usuario_nombre}':")
            for i, prestamo in enumerate(usuario['prestamos'], start=1):
                print(f"{i}. {prestamo['cantidad']} - {prestamo['descripcion']}")
            return
    print(f"Usuario '{usuario_nombre}' no encontrado.")

def menu():
    while True:
        print("\n1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Agregar préstamo")
        print("4. Listar préstamos")
        print("5. Listar préstamos de un usuario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del usuario: ")
            agregar_usuario(nombre)
        elif opcion == '2':
            listar_usuarios()
        elif opcion == '3':
            usuario_nombre = input("Ingrese el nombre del usuario: ")
            cantidad = input("Ingrese la cantidad del préstamo: ")
            descripcion = input("Ingrese la descripción del préstamo: ")
            agregar_prestamo(usuario_nombre, cantidad, descripcion)
        elif opcion == '4':
            listar_prestamos()
        elif opcion == '5':
            usuario_nombre = input("Ingrese el nombre del usuario: ")
            listar_prestamos_usuario(usuario_nombre)
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()