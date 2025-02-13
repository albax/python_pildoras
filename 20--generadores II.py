### generadores II (video 20)
# yield from
#---------------------------------

def devuelve_ciudades(*ciudades):  # * espera muchos args
    for elem in ciudades:
        # print(type(elem)) #<class 'str'> 
        # print(type(ciudades)) #<class 'tuple'> 
        # print(elem)
        
        ## anillados
        for subElem in elem:
            yield from elem
            # print(subElem)  #solo para probar q arroja


ciudades_devueltas = devuelve_ciudades("Mdrid","Paris","Berlin","Roma")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))