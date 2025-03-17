###############################################
### SERIALIZACION :: 40__serializacion_II.py
### SERIALIZACION objetos
### pickle.load
###############################################


import pickle

class Vehiculos():
    
    # metodo constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    # metodo
    def arrancar(self):
        self.enmarcha = True
        
    def acelerar(self):
        self.acelera = True
        
    def frenar(self):
        self.frena = True
        
    def estado(self):
        print("Marca: ", self.marca,
              "\nModelo: ", self.modelo,
              "\nEn Marcha: ", self.enmarcha,
              "\nAcelarando: ", self.acelera,
              "\nFrenando: ", self.frena)


#instancias
coche1 = Vehiculos("Mazda", "MX5")
coche1 = Vehiculos("Seat", "Leon")
coche1 = Vehiculos("Renault", "Megane")
