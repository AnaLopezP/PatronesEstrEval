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
    pizza_builder = Pizzeria_builder.pizzeria_AnaLaRana.Pizza()
    pizza_director = Pizzeria_builder.pizzeria_AnaLaRana.PizzaDirector(pizza_builder)
    masa = request.form.get(masa)
    salsa = request.form.get(salsa)
    ingrediente = request.form.get(ingrediente)
    return render_template('creatupizza.html', pizza=pizza)
