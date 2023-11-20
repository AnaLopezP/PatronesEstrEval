from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import csv

class Componente(ABC):

    @property
    def padre(self):
        return self._padre

    @padre.setter
    def parent(self, padre):
        self._padre = padre

    def add(self, componente) -> None:
        pass

    def remove(self, componente) -> None:
        pass

    def esta_compuesto(self):
        return False
    
    @abstractmethod
    def get_precio(self):
        pass
    
    @abstractmethod
    def get_id(self):
        pass


class MenuItem(Componente):
    def __init__(self, id, precio):
        self._id = id
        self._precio = precio
        
    def get_precio(self):
        return self._precio
    
    def get_id(self):
        return self._id


class MenuComposite(Componente):
    def __init__(self, nombre):
        self._nombre = nombre
        self._hijos = []

    def add_hijo(self, hijo):
        self._hijos.append(hijo)
        hijo.parent = self

    def remove(self, hijo):
        self._hijos.remove(hijo)
        hijo.parent = None

    def is_composite(self):
        return True

    def get_precio(self):
        for hijo in self._hijos:
            suma = sum(hijo.get_precio())
        return suma

#A partir de aqui es la creacion del menu con builder:
class MenuBuilder(ABC):
    @property
    @abstractmethod
    def crear_combos(self):
        pass
    
    @abstractmethod
    def crear_entrante_menu(self):
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
    def crear_precio(self):
        pass
    
    @abstractmethod
    def crear_menu(self):
        pass

class Menu:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.entrante = ""
        self.pizza = ""
        self.bebida = ""
        self.postre = ""
        
    @property
    def menu(self):
        menu = [self.entrante, self.pizza, self.bebida, self.postre]
        self.reset()
        return menu
    
    def crear_entrante_menu(self, entrante):
        self.entrante = entrante
    
    def crear_pizza_menu(self, pizza):
        self.pizza = pizza
        
    def crear_bebida_menu(self, bebida):
        self.bebida = bebida
        
    def crear_postre_menu(self, postre):
        self.postre = postre
    
class Menu_Producto():
    def __init__(self):
        self._menu = []
    
    def add(self, parte):
        self._menu.append(parte)
        
    def __str__(self):
        return f"Menu({', '.join([str(i) for i in self._menu])})"
    

class CSV_menu_Builder():
    def crear_csv_menu(self):
        with open('menu.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Entrante", "Pizza", "Bebida", "Postre"])
        file.close()

    def añadir_menu(self, entrante, pizza, bebida, postre):
        with open('menu.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            print(entrante, pizza, bebida, postre)
            writer.writerow([entrante, pizza, bebida, postre])
        file.close()

class MenuDirector:
    def __init__(self, builder):
        self._builder = builder

    def crear_menu(self, entrante, pizza, bebida, postre):
        self._builder.crear_entrante_menu(entrante)
        self._builder.crear_pizza_menu(pizza)
        self._builder.crear_bebida_menu(bebida)
        self._builder.crear_postre_menu(postre)
    
    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder
        
