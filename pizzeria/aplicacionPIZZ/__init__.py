'''Este archivo contiene la inicializacion de la aplicacion y la lógica común que necesita para funcionar.
Aquí inicializo instancias de clases, configuro bases de datos, etc.'''
import sys
sys.path.append('C:/Users/Usuario/Documents/GITHUB2/PatronesEstrEval/pizzeria')
from flask import Flask, request, render_template
import os
import Pizzeria_builder.pizzeria_AnaLaRana as l
import Pizzeria_builder.cliente as c
#from Pizzeria_builder import pizzeria_AnaLaRana
#from aplicacionPIZZ import routes

app = Flask(__name__)


pizza_builder = l.Pizza()
director = l.PizzaDirector(pizza_builder)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/pizzacreativa', methods=['POST', 'GET'])
def pizzacreativa():
    return render_template('creatupizza.html')

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
    return "Pizza pedida con éxito."
    
@app.route('/registro', methods=['POST', 'GET'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        direccion = request.form.get("direccion")
        usuario = request.form.get("usuario")
        contraseña = request.form.get("contraseña")
        email = request.form.get("email")
        telefono = request.form.get("telefono")

        usuario = c.Usuario(nombre, direccion, usuario, contraseña, telefono, email)

    return render_template('registro.html')
if __name__ == '__main__':
    app.run(debug=True)