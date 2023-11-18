'''Este archivo contiene las rutas específicas de la aplicacion.
Puedo definir las rutas y fnciones asociadas a ellas en este archivo.'''

from flask import render_template
from aplicacionPIZZ import app, director
import __init__ as init

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pizzacreativa', methods=['GET', 'POST'])
def pizzacreativa():
    init.manejar_formulario()
    return render_template('creatupizza.html')
