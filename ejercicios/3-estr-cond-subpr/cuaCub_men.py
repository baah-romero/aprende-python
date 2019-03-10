#Cuadrado y cubo del menor
n1 = int(input('Introducir un número entero: '))
n2 = int(input('Introducir un número entero: '))
if n1 != n2 : #Comprobar que son distintos N! y N2
    if n1 > n2 : #Comprobar si N1 es mayor
        print('\n------------RESULTADO-------------')
        print('El número N2 es el menor con valor: ', n2)
        cua, cub = n2 ** 2, n2 ** 3 #Calcular el cuadrado y cubo de N2
        print('El cuadrado de N2 es: ', cua)
        print('El cubo de N2 es: ', cub)
    else : #Si N1 no es mayor, entonces N2 es el mayor
        print('\n------------RESULTADO-------------')
        print('El número N1 es el menor con valor: ', n1)
        cua, cub = n1 ** 2, n1 ** 3 #Calcular el cuadrado y cubo de N1
        print('El cuadrado de N1 es: ', cua)
        print('El cubo de N1 es: ', cub)
else :
    print('\n------------RESULTADO-------------')
    print('N1 y N2 son IGUALES!!!!')
