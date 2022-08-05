# hacer un programa que obtenga los números primos menores a un número ingresado.

# En este caso se implementa la Criba de Eratóstenes. 
# Partimos de una lista de números que van de 2 hasta un determinado número. Eliminamos de la lista los múltiplos de 2. Luego tomamos el primer número después del 2 que no fue eliminado (el 3) y eliminamos de la lista sus múltiplos, y así sucesivamente.

entrada = open('entrada.txt', encoding='UTF-8') # abre el archivo
linea = entrada.readlines()                     # lee las lineas y se almacenan en 'linea'
entrada.close()                                 # cierra el archivo una vez se haya encontrado toda la información

i = 0
num = int(linea[0]) # pasamos la información de 'linea' a número y lo almacenamos en 'num'
p = 0
primos = []

while i != num:         # mientras i sea diferente de num...
    i += 1              # ...i va incrementar y cuando sea igual a num, el ciclo se detendrá
    primos.append(i)    # i se almacena en 'primos'

for par in primos:          # recorremos la información de 'primos'
    if par % 2 == 0:        # dividimos par entre 2, si el resto es igual a 0...
        primos.remove(par)  # ...removemos los números pares.

while primos[p] * primos[p] < num:      # mientras lo potencia de la posición actual sea menor a num
    p += 1 # la posición incrementa
    for impares in primos:              # recorremos los datos de 'primos'
        if impares % primos[p] == 0:    # se divide impares por la actual posición de primos, si el resto es igual a 0...
            primos.remove(impares)      # ...dejamos solo los números primos   
        if num in primos:               
            primos.remove(num)          # en caso de que el número que ingremos se encuentre en 'primos' lo removemos   

primos = primos[1:] # eliminamos el número 1 ya que no es primo.

# con el código que hemos usado anteriormente, eliminamos el 2 y el 3, como son números primos tenemos que volver a ingresarlos.
primos.insert(0, 3)
primos.insert(0, 2)

primosRev = primos[::-1]         # invertimos los datos de primos
primosRev = str(primosRev)[1:-1] # convertimos primosRev a string y eliminamos los corchetes

salida = open('salida.txt', 'w', encoding='UTF-8')  # abrimos el archivo de salida
salida.write(f'{num} => {primosRev}')               # escribimos el numero ingresado y la información de primosRev 
salida.close()                                      # cerramos el archivo de salida 