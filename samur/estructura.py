from datetime import datetime

class Elemento:
    def __init__(self, nombre, tipo, tamaño):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño

    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_tamaño(self):
        return self.tamaño

    def aceptar(self, usuario, accion, proxy):
        pass

class Documento(Elemento):
    def __init__(self, nombre, tipo, tamaño, contenido):
        super().__init__(nombre, tipo, tamaño)
        self.contenido = contenido

    def get_contenido(self):
        return self.contenido

    def modificar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)

class Enlace(Elemento):
    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)

class Carpeta(Elemento):
    def __init__(self, nombre):
        super().__init__(nombre, "Carpeta", 0)
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def eliminar_elemento(self, elemento):
        self.elementos.remove(elemento)

    def get_elemento(self, nombre):
        for elemento in self.elementos:
            if elemento.nombre == nombre:
                return elemento

    def get_tamaño(self):
        return sum(elemento.tamaño for elemento in self.elementos)

    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)
        for elemento in self.elementos:
            elemento.aceptar(usuario, accion, proxy)

class ProxyAcceso:
    def __init__(self):
        self.usuario_autorizado = []
        self.registros_acceso = {}

    def agregar_usuario_autorizado(self, usuario):
        self.usuario_autorizado.append(usuario)

    def registrar_acceso(self, documento, accion):
        ahora = datetime.now()
        if documento.nombre not in self.registros_acceso:
            self.registros_acceso[documento.nombre] = []
        self.registros_acceso[documento.nombre].append((accion, ahora))

    def get_registros_acceso(self, documento):
        return self.registros_acceso.get(documento.nombre, [])

    def permitir_acceso(self, usuario, documento, accion):
        if usuario in self.usuario_autorizado:
            self.registrar_acceso(documento, accion)
            return True
        return False
