import estructura as es
if __name__ == "__main__":
    # Crear instancias
    documento1 = es.Documento("Informe1", "Texto", 1024, "Contenido confidencial...")
    enlace1 = es.Enlace("Enlace1", "Enlace", 0)
    carpeta1 = es.Carpeta("Carpeta1")

    # Agregar elementos a la carpeta
    carpeta1.agregar_elemento(documento1)
    carpeta1.agregar_elemento(enlace1)
    print("Elementos de la carpeta:")
    for i in range(len(carpeta1.elementos)):
        print(carpeta1.elementos[i].nombre)

    # Crear un proxy de acceso
    proxy_acceso = es.Proxy()
    proxy_acceso.agregar_usuario_autorizado("usuario1")

    # Intentar acceder al documento con el proxy
    print("\n")
    print("Intentando acceder al documento con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", documento1, "lectura")
    print("Intentando acceder al documento con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", documento1, "lectura")
    
    #intentar acceder a la carpeta con el proxy
    print("\n")
    print("Intentando acceder a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", carpeta1, "lectura")
    print("Intentando acceder a la carpeta con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", carpeta1, "lectura")
    
    #intentar acceder al enlace con el proxy
    print("\n")
    print("Intentando acceder al enlace con el proxy...")
    proxy_acceso.permitir_acceso("usuario1", enlace1, "lectura")
    print("Intentando acceder al enlace con el proxy...")
    proxy_acceso.permitir_acceso("usuario2", enlace1, "lectura")
    
    #eliminar un elemento de la carpeta:
    print("\n")
    print("elementos restantes de la carpeta: ")
    carpeta1.eliminar_elemento(enlace1)
    for i in range(len(carpeta1.elementos)):
        print(carpeta1.elementos[i].nombre)