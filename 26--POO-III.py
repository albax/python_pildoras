### POO III
# 
#---------------------------------
#

class Coche():
    
    # propiedades | caracteristicas
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    # metodos | comportamientos
    def arrancar(self):
        self.enmarcha = True   #miCoche.enmarcha=True !!! de forma implicita
        print("El coche ARRANCO")
        
    def estado(self):
        if (self.enmarcha):
            return "El coche esta en MARCHA"
        else:
            return "El coche esta DETENIDO"
    
miCoche = Coche()
    
print("largo:", miCoche.largoChasis)
print("ancho: " + str(miCoche.anchoChasis))
print("el coche tiene:", miCoche.ruedas, "ruedas")
miCoche.arrancar()
print(miCoche.estado())

