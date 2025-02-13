
milista=["maria","pedro",60,True,2.7,"'Lucia'"]

milista.append("akio")  #add al final
milista.extend(["per","ecu","arg"]) #add concadena
print(milista)
print('--------------------------------')

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