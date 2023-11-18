'''Este archivo contiene la inicializacion de la aplicacion y la lógica común que necesita para funcionar.
Aquí inicializo instancias de clases, configuro bases de datos, etc.'''

from flask import Flask, request
from pizzeria import Pizzeria_builder as l
#from Pizzeria_builder import pizzeria_AnaLaRana
from aplicacionPIZZ import routes

app = Flask(__name__)


pizza_builder = l.Pizza()
director = l.PizzaDirector(pizza_builder)

def manejar_formulario():
    #recojo los datos del formulario del html
    masa = request.form.get(masa)
    salsa = request.form.get(salsa)
    ingrediente = request.form.get(ingrediente)
    tecnica = request.form.get(tecnica)
    presentacion = request.form.get(presentacion)
    extras = request.form.get(extras)
    bebidas = request.form.get(bebidas)
    postre = request.form.get(postre)
    
    #paso los datos al director para que cree la pizza
    director._builder.crear_masa(masa)
    director._builder.crear_salsa(salsa)
    director._builder.crear_ingrediente(ingrediente)
    director._builder.crear_tecnica(tecnica)
    director._builder.crear_presentacion(presentacion)
    director._builder.crear_extras(extras)
    director._builder.crear_bebidas(bebidas)
    director._builder.crear_postre(postre)
    
    director.crear_pizza()
    return "Pizza pedida con éxito."
    
if __name__ == '__main__':
    app.run(debug=True)