#Programa que resuelve ecuaciones de segundo grado
a = float(input('Introducir valor a: '))
b = float(input('Introducir valor b: '))
c = float(input('Introducir valor c: '))
x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print('\n--------RESULTADO-----------')
print('El valor de X1 es: ', x1)
print('El valor de X2 es: ', x2)
