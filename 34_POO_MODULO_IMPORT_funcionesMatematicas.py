###############################################
### POO MODULOS v.34
### 34_POO_MODULO_IMPORT_funcionesMatematicas.py
###############################################

#---------------------------------
##Usar guion bajo antes del número:
# pythonCopyclass _1Cliente:
##Usar una letra antes del número:
# pythonCopyclass N1Cliente:
#---------------------------------

## forma simple de IMPORT
#
# import POO_import_MODULO_funcionesMatematicas
# sumar(7,5)
# 
# from POO_import_MODULO_funcionesMatematicas import sumar
# from POO_import_MODULO_funcionesMatematicas import * # todo
# sumar(7,5)
#---------------------------------

# Importar con ALIAS:
# archivo: 1***archivo.py
# PERO NO CUMPLE CON PEP 8
# no es recomendado, puede causar problemas de depuración y mantenimiento

import importlib
impor_modulo_funcionesMate = importlib.import_module('34_POO_MODULO_funcionesMatematicas')

impor_modulo_funcionesMate.sumar(7,5)
impor_modulo_funcionesMate.restar(7,5.2)
impor_modulo_funcionesMate.multiplicar(7,5.2)

