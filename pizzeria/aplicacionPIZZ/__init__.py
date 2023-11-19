'''Este archivo contiene la inicializacion de la aplicacion y la lógica común que necesita para funcionar.
Aquí inicializo instancias de clases, configuro bases de datos, etc.'''
import sys
sys.path.append('C:/Users/Usuario/Documents/GITHUB2/PatronesEstrEval/pizzeria')
from flask import Flask, request, render_template
import os
import Pizzeria_builder.pizzeria_AnaLaRana as l
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
    ingredientes = request.form.get("ingredientes")
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
    
if __name__ == '__main__':
    app.run(debug=True)