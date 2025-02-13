
### generadores (video 19)
#---------------------------------

# def generaPares(limite):
#     num = 1
#     miLista = []
    
#     while num < limite:
#         miLista.append(num*2)
#         num = num + 1
#     return miLista

# print(generaPares(3))

#---------------------------------

# def generaPares(cantLimite):
#     num = 1
    
#     while num < cantLimite:
#         yield num*2
#         num = num + 1

# # con yield no necesita return, es iterarble

# devuelveImpares = generaPares(10)

# #para listar
# for i in devuelveImpares:
#     print(i)

#---------------------------------

def generaImpares(cantLimite):
    num = 1
    
    while num < cantLimite:
        yield num*3
        num = num + 1

# con yield no necesita return, es iterarble

devuelveImpares = generaImpares(16)

#para listar todo
# for i in devuelveImpares:
#     print(i)

#imprime proximo uno x uno
print(next(devuelveImpares))
print(next(devuelveImpares))