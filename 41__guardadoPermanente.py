###############################################
### 41__guardadoPermanente
###
### LISTA []
### TUPLA ()
###############################################


import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        # print("Se ha creado una persona nueva con el nombre de ", self.nombre)
        
    def __str__(self):
        return f"{self.nombre} {self.genero} ({self.edad} años)"
        # return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
    def __repr__(self):
        return "Persona(nombre='{}', genero='{}', edad={})".format(self.nombre, self.genero, self.edad)
    
class ListaPersonas:
    personas = [] #pretendo guardar en [lista]

    # para crear el fichero externo
    def __init__(self):
        #crea
        listaDePersonas = open("41_FicheroExterno.txt", "ab+")
        listaDePersonas.seek(0) #posicionar el puntero al inicio

        try:
            #carga
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo". format(len(self.personas)))
        except:
            print("El fichero esta vacío")
        finally:
            #cierra y borra
            listaDePersonas.close()
            del(listaDePersonas)

    
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
    
    def mostrarPersonas(self):
        for p in self.personas: #recorrer [lista] personas
            # print(p)
            # print(vars(p))   # Muestra un diccionario con los atributos
            print(repr(p)) # Usa __repr__: "Persona(nombre='Sandra', genero='Femenino', edad=24)" #mas detalle
            # print(dir(p))  # Muestra todos los métodos y atributos de la instancia
            # print(getattr(p, 'nombre'))  # Obtiene el valor del atributo 'nombre'
    
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("41_FicheroExterno.txt", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("---------------------------------------------------")
        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

#instancia
miLista = ListaPersonas()

p = Persona("Serginho", "Masculino", 35)
p = Persona("Sandra", "Femenino", 24)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()
miLista.mostrarInfoFicheroExterno()

