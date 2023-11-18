'''Este archivo contiene las rutas específicas de la aplicacion.
Puedo definir las rutas y fnciones asociadas a ellas en este archivo.'''

from flask import render_template, request
from aplicacionPIZZ import app
import Pizzeria_builder.pizzeria_AnaLaRana


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pizzacreativa')
def pizzacreativa():
    #lo comento porque lo he puesto en el init
    '''pizza_builder = Pizzeria_builder.pizzeria_AnaLaRana.Pizza()
    pizza_director = Pizzeria_builder.pizzeria_AnaLaRana.PizzaDirector(pizza_builder)'''
    
    #recojo los datos del formulario del html
    masa = request.form.get(masa)
    salsa = request.form.get(salsa)
    ingrediente = request.form.get(ingrediente)
    tecnica = request.form.get(tecnica)
    presentacion = request.form.get(presentacion)
    extras = request.form.get(extras)
    bebidas = request.form.get(bebidas)
    postre = request.form.get(postre)
    
    #creo la pizza
    
    #return render_template('creatupizza.html', pizza=pizza)
