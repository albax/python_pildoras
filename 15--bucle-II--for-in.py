
### BUCLES II (video 15)
# For in [ ]
#---------------------------------


email = False
miEmail = input("Ingrese su email: ")

# for i in "juan@pildorasinfo.com":  #recorriendo un string :: 1era vuelat i=j ::2da vuelta i=u ...
for i in miEmail:
    if (i == "@"):
        email = True
        
if email== True:
    print("Email correcto")
else:
    print("Email NO es correcto")
    
    
#---------------------------------    

contador = 0
miEmail = input("Ingrese su email: ")

# for i in "juan@pildorasinfo.com":  #recorriendo un string :: 1era vuelat i=j ::2da vuelta i=u ...
for i in miEmail:
    if (i == "@" or i=="."):
        contador = contador + 1     #contador
        
if contador == 2:
    print("Email correcto")
else:
    print("Email NO es correcto")
    

#---------------------------------    
# for in range()    

for i in range(5):
    print(i)  # 0,1,2,3,4