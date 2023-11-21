import csv
import os
class Usuario():
    def __init__(self, nombre, direccion, usuario, contraseña, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.usuario = usuario
        self.contraseña = contraseña
        self.telefono = telefono
        self.email = email
        self.ordenes = []

    def registrar_usuario(usuario):
        # Nombre del archivo CSV
        archivo_csv = 'usuarios.csv'

        # Verificar si el archivo CSV existe
        file_exists = os.path.isfile(archivo_csv)

        with open(archivo_csv, mode='a', newline='') as file:
            fieldnames = ['nombre', 'direccion', 'usuario', 'contraseña', 'telefono', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()  # Escribir encabezados solo si el archivo no existe

            # Escribir datos del usuario en el archivo CSV
            writer.writerow({
                'nombre': usuario.nombre,
                'direccion': usuario.direccion,
                'usuario': usuario.usuario,
                'contraseña': usuario.contraseña,
                'telefono': usuario.telefono,
                'email': usuario.email
            })

    def iniciar_sesion(nombre_usuario, contraseña):
        # Nombre del archivo CSV
        archivo_csv = 'usuarios.csv'

        with open(archivo_csv, mode='r') as file:
            reader = csv.DictReader(file)

            # Verificar las credenciales del usuario
            for row in reader:
                if row['usuario'] == nombre_usuario and row['contraseña'] == contraseña:
                    return True

        return False

            

