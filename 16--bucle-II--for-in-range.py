
### BUCLES II (video 16)
# For in range
#---------------------------------

for in range()    
for i in range(5):
    print(i)  # 0,1,2,3,4

print("------------")

# for in range()    
for x in range(5,50,3): #desde5 hasta50 step3
    print(f"valor de la variable {x}") # 5,8,11,14..47
    # print(x)  # 5,6,7,8,9
    
#---------------------------------

#len() 
valido = False
email = input("ingrese su email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido = True
        
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")