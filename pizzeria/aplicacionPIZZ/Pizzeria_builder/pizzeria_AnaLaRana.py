from abc import ABC, abstractmethod
import csv
import os.path
from flask import request

class PizzaBuilder(ABC):
    
    @property
    @abstractmethod
    def crear_pizza(self):
        pass
    
    @abstractmethod
    def crear_masa(self):
        pass
    
    @abstractmethod
    def crear_salsa(self):
        pass
    
    @abstractmethod
    def crear_ingrediente(self):
        pass
    
    @abstractmethod
    def crear_tecnica(self):
        pass
    
    @abstractmethod
    def crear_presentacion(self):
        pass
    
    @abstractmethod
    def crear_extras(self):
        pass
    
    @abstractmethod
    def crear_bebidas(self):
        pass
    
class Pizza:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.masa = ""
        self.salsa = ""
        self.ingrediente = []
        self.tecnica = ""
        self.presentacion = ""
        self.extras = ""
        self.bebidas = ""
        self.postre = ""
        
    @property
    def pizza(self):
        pizza = [self.masa, self.salsa, self.ingrediente, self.tecnica, self.presentacion, self.extras, self.bebidas]
        self.reset()
        return pizza
    
    def crear_masa(self, masa):     
        self.masa = masa
        
    def crear_salsa(self, salsa):      
        self.salsa = salsa
    
    def crear_ingrediente(self, ingrediente):    
        self.ingrediente.append(ingrediente)
    
    def crear_tecnica(self, tecnica):      
        self.tecnica = tecnica
        
    def crear_presentacion(self, presentacion):     
        self.presentacion = presentacion
    
    def crear_extras(self, extras):  
        self.extras = extras
    
    def crear_bebidas(self, bebidas):     
        self.bebidas = bebidas
        
    def crear_postre(self, postre):      
        self.bebidas = postre
        
class Producto():
    def __init__(self):
        self._pizza = []
        
    def add(self, parte):
        self._pizza.append(parte)
        
    def __str__(self):
        return f"Partes de la pizza: {', '.join(self._pizza)}"        
        

class CSV_Builder():
    def crear_csv(self):
        with open('pizza.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Masa", "Salsa", "Ingrediente", "Tecnica", "Presentacion", "Extras", "Bebidas", "Postre"])
        file.close()
        
    def añadir_pizza(self, masa, salsa, ingrediente, tecnica, presentacion, extras, bebidas, postre):
        with open('pizza.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            print(masa, salsa, ingrediente, tecnica, presentacion, extras, bebidas, postre)
            writer.writerow([masa, salsa, ingrediente, tecnica, presentacion, extras, bebidas, postre])
        file.close()

class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder
        
    def crear_pizza(self, masa, salsa, ingrediente, tecnica, presentacion, extras, bebidas, postre):
        self._builder.crear_masa(masa)
        self._builder.crear_salsa(salsa)
        self._builder.crear_ingrediente(ingrediente)
        self._builder.crear_tecnica(tecnica)
        self._builder.crear_presentacion(presentacion)
        self._builder.crear_extras(extras)
        self._builder.crear_bebidas(bebidas)
        self._builder.crear_postre(postre)
        
    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder

