import estructura as es
if __name__ == "__main__":
    # Crear instancias
    documento1 = es.Documento("Informe1", "Texto", 1024, "Contenido confidencial...")
    enlace1 = es.Enlace("Enlace1", "Enlace", 0)
    carpeta1 = es.Carpeta("Carpeta1")

    # Agregar elementos a la carpeta
    carpeta1.agregar_elemento(documento1)
    carpeta1.agregar_elemento(enlace1)

    # Crear un proxy de acceso
    proxy_acceso = es.Proxy()
    proxy_acceso.agregar_usuario_autorizado("usuario1")

    # Intentar acceder al documento con el proxy
    if proxy_acceso.permitir_acceso("usuario1", documento1, "lectura"):
        registros = proxy_acceso.obtener_registros_acceso(documento1)
        print(f"Acceso permitido. Registros: {registros}")
    else:
        print("Acceso denegado.")