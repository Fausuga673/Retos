# Se requiere identificar a que municipio(s) del departamento del Cesar corresponde el código ingresado mediante el archivo de entrada.

entrada = open('entrada.txt', encoding="UTF-8")   # abre el archivo
linea = entrada.readlines()                       # lee las líneas
entrada.close                                     # se cierra el archivo cuando encuentre toda la información

municipio = {
    '20001' : 'VALLEDUPAR',
    '20011' : 'AGUACHICA',
    '20013' : 'AGUSTÍN CODAZZI',
    '20032' : 'ASTREA',
    '20045' : 'BECERRIL',
    '20060' : 'BOSCONIA',
    '20175' : 'CHIMICHAGUA',
    '20178' : 'CHIRIGUANÁ',
    '20228' : 'CURUMANÍ',
    '20238' : 'EL COPEY',
    '20250' : 'EL PASO',
    '20295' : 'GAMARRA',
    '20310' : 'GONZÁLEZ',
    '20383' : 'LA GLORIA',
    '20400' : 'LA JAGUA DE IBIRICO',
    '20443' : 'MANAURE BALCÓN DEL CESAR',
    '20517' : 'PAILITAS',
    '20550' : 'PELAYA',
    '20570' : 'PUEBLO BELLO',
    '20614' : 'RÍO DE ORO',
    '20621' : 'LA PAZ',
    '20710' : 'SAN ALBERTO',
    '20750' : 'SAN DIEGO',
    '20770' : 'SAN MARTÍN',
    '20787' : 'TAMALAMEQUE',
}

salida = open('salida.txt', 'w', encoding='UTF-8')              # abre el archivo y se guarda como 'salida'
for lineas in linea:                                            # se recorren todas las lineas en el archivo de entrada
    salida.write(municipio[lineas.replace('\n', '')] + "\n")    # se escriben los municipios que se hayan buscado por su codigo
    salida.close                                                # cierra el archivo