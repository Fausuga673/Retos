#Se requiere que mediante un archivo llamado entrada.txt se ingrese la palabra u oración y como resultado en un archivo llamado salida.txt muestre su equivalente en código morse.

entrada = open('entrada.txt', encoding='UTF-8') # abre el archivo de entrada
linea = entrada.readlines()                     # lee las líneas del archivo
entrada.close()                                 # cierra el archivo una vez se encuentre toda la información

morse = {
    'A' : '· — ',
    'B' : '— · · · ',
    'C' : '— · — · ',
    'CH' : '— — — — ',
    'D' : '— · · ',
    'E' : '· ',
    'F' : '· · — · ',
    'G' : '— — · ',
    'H' : '· · · · ',
    'I' : '· · ',
    'J' : '· — — — ',
    'K' : '— · — ',
    'L' : '· — · · ',
    'M' : '— — ',
    'N' : '— · ',
    'Ñ' : '— — · — — ',
    'O' : '— — — ',
    'P' : '· — — · ',
    'Q' : '— — · — ',
    'R' : '· — · ',
    'S' : '· · · ',
    'T' : '— ',
    'U' : '· · — ',
    'V' : '· · · — ',
    'W' : '· — — ',
    'X' : '— · · — ',
    'Y' : '— · — — ',
    'Z' : '— — · · ',
    '0' : '— — — — —',
    '1' : '· — — — —',
    '2' : '· · — — —',
    '3' : '· · · — —',
    '4' : '· · · · —',
    '5' : '· · · · ·',
    '6' : '— · · · ·',
    '7' : '— — · · ·',
    '8' : '— — — · ·',
    '9' : '— — — — ·',
    '.' : '· — · — · —',
    ',' : '— · — · — —',
    '?' : '· · — — · ·', 
    '"' : '· — · · — ·',
    '!' : '— — · · — —',
    ' ' : ' ',
    '\n' : '\n'
}

position = 0
salida = open('salida.txt', 'w', encoding='UTF-8')  #abre el archivo de salida

while position < len(linea):                        
    position = position+1                           # position incrementará su valor hasta que sea menor que el número de elementos en 'linea'
    for lineas in linea[position-1]:                # recorremos cada letra de cada elemento de 'linea'
        salida.write(str(morse[lineas.upper()]))    # convertimos cada letra a máyuscula y la pasamos a clave morse, luego la escribimos en el archivo de salida