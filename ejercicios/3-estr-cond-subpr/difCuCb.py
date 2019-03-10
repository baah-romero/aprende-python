n1 = int(input('Introducir un número entero: '))
n2 = int(input('Introducir un número entero: '))
if n1 != n2 : #Comprobar que son distintos N! y N2
    if n1 > n2 : #Comprobar si N1 es mayor
        print('\n------------RESULTADO-------------')
        cux, cbx = n1 ** 2, n1 ** 3 #Calcular el cuadrado y cubo de N1 (mayor)
        cum, cbm = n2 ** 2, n2 ** 3 #Calcular el cuadrado y cubo de N2 (menor)
        print('El número N1 es el mayor con valor: ', n1)
        print('\tEl cuadrado de ', n1 ,' es: ', cux) #Cuadrado del mayor
        print('\tEl cubo de ', n1 ,' es: ', cbx) #Cubo del mayor
        print('El número N2 es el menor con valor: ', n2)
        print('\tEl cuadrado de ', n2 ,' es: ', cum) #cuadrado del menor
        print('\tEl cubo de ', n2 ,' es: ', cbm) #cubo del menor
    else : #Si N1 no es mayor, entonces N2 es el mayor
        print('\n------------RESULTADO-------------')
        cux, cbx = n2 ** 2, n2 ** 3 #Calcular el cuadrado y cubo de N1 (mayor)
        cum, cbm = n1 ** 2, n1 ** 3 #Calcular el cuadrado y cubo de N2 (menor)
        print('El número N2 es el mayor con valor: ', n2)
        print('\tEl cuadrado de ', n2 ,' es: ', cux) #Cuadrado del mayor
        print('\tEl cubo de ', n2 ,' es: ', cbx) #Cubo del mayor
        print('El número N1 es el menor con valor: ', n1)
        print('\tEl cuadrado de ', n1 ,' es: ', cum) #cuadrado del menor
        print('\tEl cubo de ', n1 ,' es: ', cbm) #cubo del menor
    dcu, dcb = cux - cum, cbx - cbm #Calcular diferencias entre cuadrados y cubos
    print('\n----------DIFERENCIAS------------')
    print('La diferencia de los cuadrados es: ', cux ,'-', cum ,'= ', dcu)
    print('La diferencia de los cubos es: ', cbx ,'-', cbm ,'= ', dcb)
else :
    print('\n------------RESULTADO-------------')
    print('N1 y N2 son IGUALES!!!!')
