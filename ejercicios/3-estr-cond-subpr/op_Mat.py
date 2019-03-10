#Operaciones matematicas respecto al mayor y al menor
n1 = int(input('Introducir un número entero: '))
n2 = int(input('Introducir un número entero: '))
if n1 != n2 : #Comprobar que son distintos N! y N2
    if n1 > n2 : #Comprobar si N1 es mayor
        print('\n------------RESULTADO-------------')
        su, res, pr = n1 + n2, n1 - n2, n1 * n2
        dr, de, re = n1 / n2, n1 // n2, n1 % n2
        pot = n1 ** n2
        print('El número N1 es el mayor con valor: ', n1)
        print('El número N2 es el menor con valor: ', n2)
        print('\tSuma de ', n1 ,'+', n2 ,'= ', su) #Suma
        print('\tResta de ', n1 ,'-', n2 ,'= ', res) #Resta
        print('\tProducto de ', n1 ,'*', n2 ,'= ', pr) #Producto
        print('\tDivisión entera de ', n1 ,'//', n2 ,'= ', de) #División entera
        print('\tDicisión real de ', n1 ,'/', n2 ,'= ', dr) #División real
        print('\tResto división de ', n1 ,'%', n2 ,'= ', re) #Resto
        print('\tPotencia de ', n1 ,'**', n2 ,'= ', pot) #Potencia
    else : #Si N1 no es mayor, entonces N2 es el mayor
        su, res, pr = n2 + n1, n2 - n1, n2 * n1
        dr, de, re = n2 / n1, n2 // n1, n2 % n1
        pot = n2 ** n1
        print('El número N2 es el mayor con valor: ', n2)
        print('El número N1 es el menor con valor: ', n1)
        print('\tSuma de ', n2 ,'+', n1 ,'= ', su) #Suma
        print('\tResta de ', n2 ,'-', n1 ,'= ', res) #Resta
        print('\tProducto de ', n2 ,'*', n1 ,'= ', pr) #Producto
        print('\tDivisión entera de ', n2 ,'//', n1 ,'= ', de) #División entera
        print('\tDicisión real de ', n2 ,'/', n1 ,'= ', dr) #División real
        print('\tResto división de ', n2 ,'%', n1 ,'= ', re) #Resto
        print('\tPotencia de ', n2 ,'**', n1 ,'= ', pot) #Potencia
else :
    print('\n------------RESULTADO-------------')
    print('N1 y N2 son IGUALES!!!!')
