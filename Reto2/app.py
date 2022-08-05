#Se requiere una solución algorítmica de tal manera que al introducir una oración pueda arrojar la cantidad encontrada de cada carácter, la solución debe contabilizar solo las letras del abecedario de la A a la Z sin distinguir entre mayúsculas y minúsculas.

entrada = open('entrada.txt', 'r', encoding='UTF-8')    # abre el archivo de entrada
lineas = entrada.readlines()                            # lee las lineas del archivo
entrada.close()                                         # cierra el archivo cuando lea todas las lineas

position = 0
caracteres = []
repeticiones = []

# guarda todas las letras en 'caracteres', sin saltos de linea ni espacios
while position < len(lineas):
    position = position+1
    letra = lineas[position-1]
    letra = letra.replace(' ', '')
    letra = letra.replace('\n', '')
    for i in letra:
        caracteres.append(i.upper()) # convertimos todas las letras a mayúscula

# cuenta el número de repeticiones y los guarda en 'repeticiones'
while position < len(caracteres):
    position = position+1
    letra = caracteres[position-1]
    repeticiones.append(f'Repeticiones de la letra {str(letra)}: {str(caracteres.count(letra))}')
    
    # se borran los elementos duplicados en 'repeticiones' para solo tener un resultado por cada letra
    repeticiones = list(set(repeticiones))

salida = open('salida.txt', 'w', encoding='UTF-8')  # abre el archivo de salida
for i in repeticiones:                              # recorremos todos los elementos de 'repeticiones'
    salida.write(i + '\n')                          # escribimos en el archivo de salida los elementos de 'repeticiones'