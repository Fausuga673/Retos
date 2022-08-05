# Escriba un programa que genere un menú de opciones para calcular el volumen de los sólidos geométricos tal como se ilustra a continuación:

#####Volumen de sólidos#####
# 1. Cubo
# 2. Prisma
# 3. Pirámide
# 4. Esfera
# 5. Cilindro
# 6. Cono

import math

opcion = input('Ingresa el número correspondiente a la figura: 1. CUBO, 2. Prisma, 3. Pirámide, 4. Esfera, 5. Cilindro, 6. Cono : ')

if opcion == '1':
    lado = int(input('Ingresa la medida de uno de sus lados: '))
    potencia = pow(lado, 3)
    print(f'El volumen del cubo es: {potencia}cm³')
    
elif opcion == '2':
    lado = int(input('Ingresa la medida de uno de sus lados: '))
    base = int(input('Ingresa la base: '))
    altura = int(input('Ingresa la altura: '))
    res = ((lado * base) * altura)
    print(f'El volumen del prisma es: {res}cm³')

elif opcion == '3':
    lado = int(input('Ingresa la medida de uno de sus lados: '))
    base = int(input('Ingresa la base: '))
    altura = int(input('Ingresa la altura: '))
    res = base
    res = (res * altura) / 3
    print(f'El volumen de la pirámide es: {res}cm³')

elif opcion == '4':
    radio = int(input('Ingresa el radio: '))
    res = 4/3 * math.pi * radio ** 3
    print(f'El volumen de la esfera es: {res}cm³')

elif opcion == '5':
    radio = int(input('Ingresa el radio: '))
    altura = int(input('Ingresa la altura: '))
    res = (math.pi * (radio * radio)) * altura
    print(f'El volumen del cilindro es: {res}cm³')

elif opcion == '6':
    radio = int(input('Ingresa el radio: '))
    altura = int(input('Ingresa la altura: '))
    area_base = math.pi * radio ** 2
    res = (area_base * altura) / 3
    print(f'El volumen del cono es: {res}cm³')

else: 
    print('Opción no válida')