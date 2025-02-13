### POO III .2
# 
#---------------------------------
#

class Coche():
    
    # metodo constructor
    def __init__(self) -> None:
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4  #encapsulado
        self.__enmarcha = False
    
    # metodos | comportamientos
    def arrancar(self, arrancamos):
        
        self.__enmarcha = arrancamos
        
        if (self.__enmarcha):
            return "El coche esta en MARCHA"
        else:
            return "El coche esta DETENIDO"
        
    def estado(self):
        print("Ruedas: ", self.__ruedas, "ruedas", #encapsulado
              "Ancho: ", self.__anchoChasis, 
              "Largo: ", self.__largoChasis)
        

    
miCoche = Coche()
    
print(miCoche.arrancar(True))

miCoche.__ruedas = 3  ## no deberia suceder, no DEBE cambiar el constructor, ncesita ENCAPSULACION
miCoche.estado()



