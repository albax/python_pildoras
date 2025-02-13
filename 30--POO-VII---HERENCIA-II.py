###############################################
### POO VII  HERENCIA.2
###############################################
#---------------------------------
#

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

# HERENCIA
class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
        
# HERENCIA
class Moto(Vehiculos):
        hcaballito = ""
        def caballito(self):
            self.hcaballito = "Voy haciendo caballito"
        # sobreescribe el estado
        def estado(self):
            print("Marca: ", self.marca,
              "\nModelo: ", self.modelo,
              "\nEn Marcha: ", self.enmarcha,
              "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena,
              "\n", self.hcaballito)
            
class VElectricos():
    def __init__(self):
        self.autonomia = 100
    
    def cargaEnergia(self):
        self.cargando = True

# instancia    
miMoto = Moto("Honda", "CBR")
miFurgoneta = Furgoneta("Renault", "Kangoo")

# instancia multiple


# llama a propiedad
miMoto.caballito()
miFurgoneta.arrancar()

# llamar a la propiedad (metodo)
miMoto.estado()
print("=========================")
miFurgoneta.estado()


