
### TUPLA ()
### LISTA []

mitupla = ("Jun",8.9,True,"Olivera", 2012)
print(type(mitupla))  #<class 'tuple'>  

print(mitupla)  # ('Jun', 8.9, True, 'Olivera', 2012)
print(list(mitupla)) # ['Jun', 8.9, True, 'Olivera', 2012] #5# convierte en LISTA
print(type(mitupla))  #<class 'tuple'>  

# ------------------------------------------------------------------------

milista = ["groo", 6.78, "PEPE", 8, 1234, 8]
print(type(milista))
print(milista)

print(tuple(milista))  # ('groo', 6.78, 'PEPE', 8, 1234) #convierte en TUPLA

# ------------------------------------------------------------------------

print(milista.count(8))  #ctos 8 hay
print(mitupla.count("PEPE"))  #ctos PEPE hay

print(len(mitupla)) #ctos elem tiene tupla
p1 = mitupla.index("Olivera")  # se puede ver el INDEX
print("index es: " + str(p1))


# ------------------------------------------------------------------------

resu = mitupla + tuple(milista)
print(resu)

print(len(resu))

## TUPLA UNITARIA la coma, 
# ------------------------------------------------------------------------

mitupla2 = ("Jhonr",) #sin , cta caracteres
print(len(mitupla2))

## EMPAQUETADO DE TUPLA
# ------------------------------------------------------------------------

mitupla3 = "Pedro","Jhon", 5, True, 89.04, "Rafa" #sin ()
print(mitupla3)

## DESEMPAQUETADO DE TUPLA
# ------------------------------------------------------------------------

mitupla4 = ("Peo","Jon", 35, 4.7, True, 89.04, False, 2022)
nombre, segNombre, edad, tal, Hombre, Salario, Empleado, ano = mitupla4
print(nombre)
print(edad)
print(tal)
print(Hombre)

print(ano)