'''Este archivo contiene la inicializacion de la aplicacion y la lógica común que necesita para funcionar.
Aquí inicializo instancias de clases, configuro bases de datos, etc.'''

from flask import Flask
from Pizzeria_builder import pizzeria_AnaLaRana
from aplicacionPIZZ import routes

app = Flask(__name__)

pizza_builder = pizzeria_AnaLaRana.Pizza()
director = pizzeria_AnaLaRana.PizzaDirector(pizza_builder)
if __name__ == '__main__':
    app.run(debug=True)