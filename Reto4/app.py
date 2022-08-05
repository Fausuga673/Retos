# Escriba un programa que convierta números binarios en decimales

entrada = open('entrada.txt', 'r', encoding='UTF-8') # abre el archivo de entrada
linea = entrada.readlines()                          # lee las líneas
entrada.close                                        # cierra el archivo cuando se encuentre toda la información

base = 0
binario = linea[0]                                   # acá almacena el contenido de 'linea'
binarioRev = binario[::-1]                           # se invierte la cadena
numeroDecimal = []

# recorremos todos los números y se le asigna la correspondiente potencia base 2
for numBinario in binarioRev:
    base = base+1
    numeroDecimal.append(int(numBinario) * (pow(2, base-1)))

salida = open('salida.txt', 'w', encoding='UTF-8')              # se abre el documento de salida
salida.write(f'{str(binario)} => {str(sum(numeroDecimal))}')    # se escribe el número ingresado y la suma de las potencias para obtener el número décimal
salida.close                                                    # cierra el archivo de salida