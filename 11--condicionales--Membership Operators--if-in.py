
### CONDICIONALES IV (video 13)
# Membership Operators  IF in
#---------------------------------

print("Asignaturas 2024")
print("Asignaturas optativas: INFORMATICA  - PRUEBAS DE SOFTWARE - USABILIDAD") 

asignatura = input("Escribe la asignatura escogida: ")
asignatura_escogida = asignatura.upper()

if asignatura_escogida in ("INFORMATICA","PRUEBAS DE SOFTWARE","USABILIDAD"):
    print("Asignatura elegida: " + asignatura.upper())
else:
    print("La asignatura escogida NO EXISTE")    