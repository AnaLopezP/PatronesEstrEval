class Usuario():
    def __init__(self, nombre, direccion, usuario, contraseña, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.usuario = usuario
        self.contraseña = contraseña
        self.telefono = telefono
        self.email = email
        self.ordenes = []
        
usuarios = []