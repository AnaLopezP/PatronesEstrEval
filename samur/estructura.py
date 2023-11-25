from datetime import datetime

#la clase elemento es la padre y principal
class Elemento:
    #constructor. cada elemento tiene un nombre, tipo y tamaño
    def __init__(self, nombre, tipo, tamaño):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño

    #getters
    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_tamaño(self):
        return self.tamaño

    #metodo para aceptar un usuario, que hará una acción, mediante un proxy
    def aceptar(self, usuario, accion, proxy):
        pass

#uno de los tipos de elementos. por tanto, hereda de elemento
class Documento(Elemento):
    #a parte de los atributos de elemento, tiene un contenido
    def __init__(self, nombre, tipo, tamaño, contenido):
        super().__init__(nombre, tipo, tamaño)
        self.contenido = contenido

    #getter de contenido
    def get_contenido(self):
        return self.contenido

    #función para modificar el contenido del documento
    def modificar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    #función concreta de aceptar el usuario al documento
    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)

#al enlace no se le añade nada más, simplemente hacemos una función para acceder a el, como en el resto de hijos
class Enlace(Elemento):
    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)

class Carpeta(Elemento):
    #una carpeta está formada de elementos, que puede ser cualquiera de los tipos anteriores
    def __init__(self, nombre):
        super().__init__(nombre, "Carpeta", 0)
        self.elementos = []

    #funciones básicas de una carperta
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

    #función para permitir al usuario acceder a la carpeta y a sus elementos
    def aceptar(self, usuario, accion, proxy):
        proxy.permitir_acceso(usuario, self, accion)
        for elemento in self.elementos:
            elemento.aceptar(usuario, accion, proxy)

#clase interfaz del proxy
class InterfazServicio:
    #no tiene constructor, ya que es una interfgaz
    def permitir_acceso(self, usuario, elemento, accion):
        pass
    
    def get_registros_acceso(self, elemento):
        pass
    
    def agregar_usuario_autorizado(self, usuario):
        pass
    
    def registrar_acceso(self, elemento, accion):
        pass
    
 #clase proxy para controlar el acceso a los elementos   
class Proxy(InterfazServicio):
    #tenemos una lista con los usuarios autorizados a entrar, y un diccionario con los registros de acceso, que guarda el usuario y la fecha
    def __init__(self):
        self.usuario_autorizado = []
        self.registros_acceso = {}

    #función para añadir un usuario autorizado
    def agregar_usuario_autorizado(self, usuario):
        self.usuario_autorizado.append(usuario)

    #función para añadir un registro de acceso a un elemento
    def registrar_acceso(self, documento, accion):
        ahora = datetime.now()
        if documento.nombre not in self.registros_acceso:
            self.registros_acceso[documento.nombre] = []
        self.registros_acceso[documento.nombre].append((accion, ahora))

    #getter
    def get_registros_acceso(self, documento):
        return self.registros_acceso.get(documento.nombre, [])

    #función para permitir el acceso a un usuario a un elemento. si el usuario está en la lista de autorizados, se registra el acceso. si no, return false
    def permitir_acceso(self, usuario, documento, accion):
        if usuario in self.usuario_autorizado:
            self.registrar_acceso(documento, accion)
            return True
        return False
