###############################################
### Archivos Externos v.37
### .io
###############################################

#---------------------------------

#--CREACION--APERTURA--MANIPULACION--CIERRE--

from io import open

#escribir
arch_text0 = open("37_archivo.txt","w")
frase = "estpendo dia para estudiar Python \n el jueves"
arch_text0.write(frase)
arch_text0.close()

#leer
arch_text1 = open("37.1_archivo.txt","r")
texto1 = arch_text1.read()
arch_text1.close()
print(".read :: " + texto1)

#readlines -- leer linea x line
arch_text2 = open("37.1_archivo.txt","r")
texto2 = arch_text2.readlines()
arch_text2.close()
print(texto2) #lista
print(".readlines :: " + str(texto2))
print(".readlines :: " + str(texto2[1]))


#---------------------------------
# Añadir mas lineas
arch_text3 = open("37_archivo.txt","a") #append
arch_text3.write("\n siempre es mejor aprender algo NUEVO como python")
arch_text3.close()

#---------------------------------
# colocar el puntero de inicio
arch_text4 = open("37_archivo.txt","rb") #read | binary
arch_text4.seek(int(len(arch_text4.read())/2))
print(arch_text4.read())

# arch_text4.seek(12,0) # 0 begining | 1 current | 2 end
# # arch_text4.seek(-10, 2)
# # prints current position
# print(arch_text4.tell())
# # Converting binary to string and printing
# print(arch_text4.readline().decode('utf-8'))
# arch_text4.close()