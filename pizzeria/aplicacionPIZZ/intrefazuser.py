'''Este archivo contiene la inicializacion de la aplicacion y la lógica común que necesita para funcionar.
Aquí inicializo instancias de clases, configuro bases de datos, etc.'''
import sys
sys.path.append('C:/Users/Usuario/Documents/GITHUB2/PatronesEstrEval/pizzeria')
from flask import Flask, request, render_template, flash
import os
import Pizzeria_builder.pizzeria_AnaLaRana as l
import Pizzeria_builder.cliente as c
import Pizzeria_builder.pizzeria_menus as m
import random

import csv

precios = {
    "pan de ajo": 3.0,
    "palitos de queso": 2.50,
    "bruschetta": 4.75,
    "aros de cebolla": 3.0,
    "patatas queso bacon": 4.0,
    "deditos pollo": 2.50,
    "provolone": 4.75,
    "ensalada caprese": 5.0,
    "ensalada mixta": 5.0,
    "mix entrantes": 6.50,
    "margarita": 6.0,
    "cuatroquesos": 7.0,
    "barbacoa": 7.0,
    "carbonara": 7.0,
    "pepperoni": 7.0,
    "hawaiana": 7.0,
    "4estaciones": 7.0,
    "especialdelchef": 8.0,
    "vegetariana": 7.0,
    "suprema": 8.0,
    "Sin bebida": 0.0,
    "cocacola": 1.50,
    "Agua": 1.0,
    "fantanaranja": 1.50,
    "fantalimon": 1.50,
    "nestea": 1.50,
    "sprite": 1.50,
    "cerveza": 2.50,
    "vino": 3.0,
    "Sorprendame": 2.0,
    "Sin postre": 0.0,
    "Tarta de queso": 2.0,
    "Tarta de chocolate": 2.0,
    "Tarta de limon": 2.0,
    "Tarta de manzana": 2.0,
    "Helado": 1.50,
    "Tarta de fresa": 2.0,
    "Fruta": 1.50,
    "Sorprendame": 2.50,
}

# Nombre del archivo CSV
archivo_csv = 'precios.csv'

# Escribir el diccionario en el archivo CSV
with open(archivo_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    # Escribir la cabecera
    writer.writerow(['producto', 'precio'])
    # Escribir los datos
    for producto, precio in precios.items():
        writer.writerow([producto, precio])

print(f"El archivo CSV '{archivo_csv}' ha sido creado con éxito.")


app = Flask(__name__)

def generar_id():
    return ''.join(str(random.randint(0, 9)) for _ in range(8))


pizza_builder = l.Pizza()
director = l.PizzaDirector(pizza_builder)

combos_builder = m.Menu()
director_combo = m.MenuDirector(combos_builder)

@app.route('/registrar_usuario')
def registrar_usuario():
    return render_template('registro.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/pizzacreativa', methods=['POST', 'GET'])
def pizzacreativa():
    return render_template('creatupizza.html')

@app.route('/pizzamenu', methods=['POST', 'GET'])
def pizzamenu():
    return render_template('pizzamenu.html')

@app.route('/combosALA', methods=['POST', 'GET'])
def combosALA():
    return render_template('combosALA.html')

@app.route('/form', methods=['POST'])
def manejar_formulario():
    #recojo los datos del formulario del html
    print(request.get_data())
    masa = request.form.get("masa")
    salsa = request.form.get("salsa")
    ingredientes = [request.form.get("ingredientes_jamon"),request.form.get("ingredientes_queso"), request.form.get("ingredientes_cebolla"),
                    request.form.get("ingredientes_aceitunas"), request.form.get("ingredientes_champis"), request.form.get("ingredientes_pimiento"),
                    request.form.get("ingredientes_pollo"), request.form.get("ingredientes_atun"), request.form.get("ingredientes_bacon"),
                    request.form.get("ingredientes_carne"), request.form.get("ingredientes_salami"), request.form.get("ingredientes_pepperoni"),
                    request.form.get("ingredientes_chorizo"), request.form.get("ingredientes_amchoas"), request.form.get("ingredientes_maiz"),
                    request.form.get("ingredientes_piña"), request.form.get("ingredientes_rucula"), request.form.get("ingredientes_albahaca"),
                    request.form.get("ingredientes_oregano"), request.form.get("ingredientes_perejil"), request.form.get("ingredientes_pimientopicante")]
    
    for i in range(len(ingredientes)):
        if ingredientes[i] == None:
            ingredientes[i] = ""
            
    tecnica = request.form.get("tecnica")
    presentacion = request.form.get("presentacion")
    extra = request.form.get("extra")
    bebida = request.form.get("bebida")
    postre = request.form.get("postre")
    
    #paso los datos al director para que cree la pizza
    director._builder.crear_masa(masa)
    director._builder.crear_salsa(salsa)
    director._builder.crear_ingredientes(ingredientes)
    director._builder.crear_tecnica(tecnica)
    director._builder.crear_presentacion(presentacion)
    director._builder.crear_extra(extra)
    director._builder.crear_bebida(bebida)
    director._builder.crear_postre(postre)
    
    director.crear_pizza(masa, salsa, ingredientes, tecnica, presentacion, extra, bebida, postre)
    
    csv_builder = l.CSV_Builder()
    if not os.path.isfile('pizza.csv'):
            csv_builder.crear_csv()
    csv_builder.añadir_pizza(masa, salsa, ingredientes, tecnica, presentacion, extra, bebida, postre)
    
    mensaje = "Pedido realizado con éxito. Su total es de 12.99€"
    flash(mensaje, "success")
    return render_template("pedidorealizado.html", mensaje = mensaje)
    
@app.route('/registro', methods=['POST', 'GET'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        direccion = request.form.get("direccion")

        contrasena = request.form.get("contrasena")
        email = request.form.get("email")
        telefono = request.form.get("telefono")

        persona = c.Usuario(nombre, direccion, contrasena, telefono, email)
        persona.registrar_usuario()
    return render_template('index_conuser.html')

@app.route('/iniciar_sesion', methods=['POST', 'GET'])
def iniciar_sesion():
    if request.method == 'POST':
        nombre = request.form.get("username")
        contrasena = request.form.get("password")

        usuario = c.Usuario(nombre, "", contrasena, "", "")
        if usuario.iniciar_sesion():
            print("Inicio de sesión exitoso.") 
            return render_template('index_conuser.html')
        else:
            print("Inicio de sesión fallido.")
            return render_template('index.html')

@app.route('/form_combo', methods=['POST', 'GET'])
def manejar_formulario_combos():
    #recojo los datos del formulario
    print(request.get_data())
    id = generar_id()
    entrante = request.form.get("entrante")
    pizza = request.form.get("pizza")
    bebida = request.form.get("bebida")
    postre = request.form.get("postre")
    
    #creo un menu
    menu = m.MenuComposite()
    menu.add_hijo(m.MenuItem(entrante))
    menu.add_hijo(m.MenuItem(pizza))
    menu.add_hijo(m.MenuItem(bebida))
    menu.add_hijo(m.MenuItem(postre))
    
    #recogo el precio de los productos
    precio = menu.get_precio()    
    print(precio)
    #paso los datos al director para que cree el combo
    director_combo._builder.crear_id(id)
    director_combo._builder.crear_entrante_menu(entrante)
    director_combo._builder.crear_pizza_menu(pizza)
    director_combo._builder.crear_bebida_menu(bebida)
    director_combo._builder.crear_postre_menu(postre)
    director_combo._builder.crear_precio(precio)
    director_combo.crear_menu(id, entrante, pizza, bebida, postre, precio)
    
    csv_builder_menu = m.CSV_menu_Builder()
    if not os.path.isfile('menu.csv'):
            csv_builder_menu.crear_csv_menu()
    csv_builder_menu.añadir_menu(id, entrante, pizza, bebida, postre, precio)
    
    mensaje = "Pedido realizado con éxito. Su total es de " + str(precio) + "€"
    flash(mensaje, "success")
    return render_template("pedidorealizado.html", mensaje = mensaje)

@app.route('/form_comboALA', methods=['POST', 'GET'])
def manejar_formulario_combosALA():
    combo_id = generar_id()
    combo_nombre = request.form.get("combo_nombre")
    print("ID del combo generado:", combo_id)
    print("Nombre del combo:", combo_nombre)

    # Guardar en CSV
    guardar_en_csv(combo_id, combo_nombre)

    mensaje = "Pedido realizado con éxito. Su total es de 12.99€"
    flash(mensaje, "success")
    return render_template("pedidorealizado.html", mensaje = mensaje)

def guardar_en_csv(combo_id, combo_nombre):
    file_exists = os.path.isfile('combos.csv')
    
    with open('combos.csv', mode='a', newline='') as file:
        fieldnames = ['id', 'combo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Escribir encabezados solo si el archivo no existe

        # Escribir datos del combo en el archivo CSV
        writer.writerow({'id': combo_id, 'combo': combo_nombre})

if __name__ == '__main__':
    app.run(debug=True)