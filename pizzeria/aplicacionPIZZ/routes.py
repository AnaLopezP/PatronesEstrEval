'''Este archivo contiene las rutas específicas de la aplicacion.
Puedo definir las rutas y fnciones asociadas a ellas en este archivo.'''

from flask import render_template
from aplicacionPIZZ import app, director

@app.route('/')
def home():
    return render_template('index.html')

def pizzacreativa():
    pizza = director.crear_pizza()
    return render_template('creatupizza.html', pizza=pizza)
