#Programa que saca cociente y Resultado
n1 = int(input('Introducir dividendo entero: '))
n2 = int(input('Introducir divisor entero: '))
c, r = divmod(n1,n2)
print('\n--------------Resultado-------------')
print('La división ', n1 ,'/', n2 ,' tiene como resultado')
print('Cociente: ', c)
print('Resto: ',r)
