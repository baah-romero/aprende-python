#If anidados
n1 = int(input('Introducir un número entero: '))
n2 = int(input('Introducir un número entero: '))
n3 = int(input('Introducir un número entero: '))
#Comprobar que no sean iguales ninguno de los números
if n1 != n2 and n1 != n3 and n2 != n3 :
    if n1 > n2 and n1 > n3 : #Comporbar si N1 es el mayor
        print('\n------------RESULTADO-------------')
        print('El número máyor es N1 con el valor: ', n1)
        if n2 > n3 : #Comprobar cual es el menor
            print('El número menor es N3 con el valor: ', n3)
        else :
            print('El número menor es N2 con el valor: ', n2)
    elif n2 > n1 and n2 > n3 : #Comprobar si el mayor es N2
        print('\n------------RESULTADO-------------')
        print('El número máyor es N2 con el valor: ', n2)
        if n1 > n3 : #Comprobar cual es el menor
            print('El número menor es N3 con el valor: ', n3)
        else :
            print('El número menor es N1 con el valor: ', n1)
    elif n3 > n1 and n3 > n2 : #Comprobar si el mayor es n3
        print('\n------------RESULTADO-------------')
        print('El número máyor es N3 con el valor: ', n3)
        if n1 > n2 : #Comprobar cual es el menor
            print('El número menor es N2 con el valor: ', n2)
        else :
            print('El número menor es N1 con el valor: ', n1)
    med = (n1 + n2 + n3) / 3 #Calcular la media de los 3 números
    print('La media de los 3 números introducidos es: ', med) #Mostrar la media
else : #Mensaje de error si 2 números son iguales
    print('\n------------RESULTADO-------------')
    print('Error, al menos 2 números son iguales.')
