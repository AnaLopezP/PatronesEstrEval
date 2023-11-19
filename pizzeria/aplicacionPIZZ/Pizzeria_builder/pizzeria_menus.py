from abc import ABC, abstractmethod
import csv
import os.path
from flask import request

class ComboBuilder(ABC):
    
    @property
    @abstractmethod
    def crear_combo(self):
        pass
    
    @abstractmethod
    def crear_pizza_menu(self):
        pass
    
    @abstractmethod
    def crear_bebida_menu(self):
        pass
    
    @abstractmethod
    def crear_postre_menu(self):
        pass
    
    @abstractmethod
    def crear_id(self):
        pass
    
    @abstractmethod
    def crear_precio(self):
        pass
    
class Combo:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.pizza = ""
        self.bebida = ""
        self.postre = ""
        
    @property
    def combo(self):
        combo = [self.pizza, self.bebida, self.postre]
        self.reset()
        return combo

    def crear_pizza_menu(self, pizza):
        self.pizza = pizza
        
    def crear_bebida_menu(self, bebida):
        self.bebida = bebida 
        
    def crear_postre_menu(self, postre):
        self.postre = postre
        
    def crear_id(self, id):
        self.id = id
        
    def crear_precio(self, precio):
        self.precio = precio
        
class Producto():
    def __init__(self):
        self._combo = []
        
    def añadir_combo(self, combo):
        self._combo.append(combo)
    
    def __str__(self):
        return f"Combo: {', '.join(self._combo)}"
    
class CSV_combo_Builder():
    def crear_csv_combo(self):
        with open('combo.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "pizza", "bebida", "postre", "precio"])
        file.close()
    
    def añadir_combo(self, id, pizza, bebida, postre, precio):
        with open('combo.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, pizza, bebida, postre, precio])
        file.close()
        
class ComboDirector():
    def __init__(self, builder):
        self._builder = builder
        
    def crear_combo(self, pizza, bebida, postre, id, precio):
        self._builder.crear_pizza_menu(pizza)
        self._builder.crear_bebida_menu(bebida)
        self._builder.crear_postre_menu(postre)
        self._builder.crear_id(id)
        self._builder.crear_precio(precio)
        
    @property
    def builder_combo(self):
        return self._builder
    
    @builder_combo.setter
    def builder_combo(self, builder):
        self._builder = builder