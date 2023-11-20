from abc import ABC, abstractmethod
import csv
import os.path
from flask import request

class MenuComponente(ABC):
    @abstractmethod
    def get_precio(self):
        pass
    
class ComboBuilder(ABC):
    
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
    
class Combo(MenuComponente):
    def __init__(self, codigo):
        super().__init__()
        self.codigo = codigo
        self.elementos = []
    
    def get_precio(self):
        return sum(elemento.get_precio() for elemento in self.elementos)
    
    def añadir_elemento(self, elemento):
        self.elementos.append(elemento)
        
class Producto(MenuComponente):
    def __init__(self, nombre, precio):
        super().__init__()
        self.nombre = nombre
        self.precio = precio
        
    def get_precio(self):
        return self.precio
    
    def __str__(self):
        combo_str = f"{self.nombre}: {', '.join(map(str, self.combo))}"
        subcombos_str = "\n".join(map(str, self._combos))
        return f"{combo_str}\n{subcombos_str}" if self._combos else combo_str
        

class CSV_combos_Builder():
    def crear_csv_combos(self):
        with open('combo.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["codigo","entrante", "pizza", "bebida", "postre", "precio"])
        file.close()
    
    def añadir_combos(self, codigo, entrante, pizza, bebida, postre, precio):
        with open('combo.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([codigo, entrante, pizza, bebida, postre, precio])
        file.close()
        
class ComboDirector():
    def __init__(self, builder):
        self._builder = builder
        
    def crear_combos(self, entrante, pizza, bebida, postre, precio):
        self._builder.crear_entrante_menu(entrante)
        self._builder.crear_pizza_menu(pizza)
        self._builder.crear_bebida_menu(bebida)
        self._builder.crear_postre_menu(postre)
        self._builder.crear_precio(precio)
        
    def crear_menu_compuesto(self, codigo):
        self._builder.crear_menu(codigo)
        
    @property
    def builder_combos(self):
        return self._builder
    
    @builder_combos.setter
    def builder_combos(self, builder):
        self._builder = builder