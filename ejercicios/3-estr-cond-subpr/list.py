#Hacer lista con elif
n = int(input('Introducir un número entero (1-3): '))
if n == 1 : #Comprobar si n es 1
    print('\n------------RESULTADO-------------')
    print('Uno')
elif n == 2 : : #Comprobar si n es 2
    print('\n------------RESULTADO-------------')
    print('Dos')
elif n == 3 : : #Comprobar si n es 3
    print('\n------------RESULTADO-------------')
    print('Tres')
else : : #Si n no es 1, 2 o 3; mostrar el mensaje de error
    print('\n------------RESULTADO-------------')
    print('Error, opciones válidas: 1-3. No vale la opción: ', n)
