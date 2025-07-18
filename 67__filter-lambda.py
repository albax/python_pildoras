###############################################
### 67__filter-lambda.py
###
### LISTA []
### TUPLA ()
###############################################


### con clase y filter
### entrega atraves de filter los pares

def nro_par(num):
    
    if num %2 == 0: # nros divisibles /2 osea PARES
        return True
    
numeros = [13, 15, 67, 6, 17, 98, 57, 40]

print(list(filter(nro_par, numeros)))


print("--------------------------------------------")

### con lambda y filter
### entrega atraves de filter los pares

numeros = [13, 15, 67, 6, 17, 98, 57, 40]

print(list(filter(lambda nro_par: nro_par%2==0, numeros)))