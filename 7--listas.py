
### LISTA []
### TUPLA ()


milista=["maria","pedro",60,True,2.7,"'Lucia'"]

milista.append("akio")  #add al final
milista.extend(["per","ecu","arg"]) #add concadena
# milista.remove(60) #remove
## milista.replace(2,"DOS") # NO es para LISTAS
# milista.pop() #elimina el ult de lista

print(type(milista[5])) # <class 'str'>

print(milista.index("akio")) #ver index
print(milista) #['maria', 'pedro', 60, True, 'akio', 'per', 'ecu', 'arg']


#----------------------------------

print(milista[:2]) #['maria', 'pedro']  #imprime 0 y 1
print(milista[:-2]) #['maria', 'pedro', 60, True, 'akio', 'per'] #imprime desde final 0 y 1
print(milista[2:]) #[60, True, 'akio', 'per', 'ecu', 'arg'] #imprime apartir de 01"2"
print(milista[2:-2]) #[60, True, 'akio', 'per'] #imprime desde final 0 y 1 hasta 01"2"

print(milista[-2]) #ecu
print(milista[::]) #['maria', 'pedro', 60, True, 'akio', 'per', 'ecu', 'arg']
print(milista[::-1]) #['arg', 'ecu', 'per', 'akio', True, 60, 'pedro', 'maria']  # ALREVES
print(milista[::-2]) #['arg', 'per', True, 'pedro']  ##cd 2
print(milista[-2::]) #['ecu', 'arg']  ## solo 2
print(milista[-2:]) #['ecu', 'arg']  ##solo 2

#----------------------------------

print("akio" in milista) #True
print(milista.index("arg"))  #7

#----------------------------------

milista2 = ["fred", 5, True, 78.99]
print(milista2)
print(milista2[::-1])

#----------------------------------

milistaA=["Sandra","Lucas"]
milistaB=[True, 45.67,"Abe"]

milistaC=["Sandra","Lucas"] * 3 # REPITE

miList = milistaA + milistaB # + CONCATENA
print(miList) #['Sandra', 'Lucas', True, 45.67, 'Abe']
print(miList[:]) #['Sandra', 'Lucas', True, 45.67, 'Abe'] OK

print(milistaC[:]) #['Sandra', 'Lucas', 'Sandra', 'Lucas', 'Sandra', 'Lucas']

#----------------------------------