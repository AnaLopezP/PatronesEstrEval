'''Este archivo contiene las rutas específicas de la aplicacion.
Puedo definir las rutas y fnciones asociadas a ellas en este archivo.'''

from flask import render_template
from aplicacionPIZZ import app, pizza_builder

@app.route('/')
def home():
    pizza = pizza_builder.crear_pizza()
    return render_template('index.html', pizza = pizza)
