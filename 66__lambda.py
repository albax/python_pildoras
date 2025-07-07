###############################################
### 66__lambda.py
###
### LISTA []
### TUPLA ()
###############################################

## normal
def area_triangulo(base, altura):
    return (base*altura)/2

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,4)
print(triangulo1)
print(triangulo2)


## lambda
area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(7,8))
print(area_triangulo(5,8))


print("--------------------------------------------")

alCubo=lambda nro:pow(nro,3)
# alCubo=lambda nro:nro**3

print(alCubo(13))