#Comprobar si son iguales o no y cual es mayor.
n1 = float(input('Introducir un número: '))
n2 = float(input('Introducir otro número: '))
if n1 != n2 : #Comprobar si n1 y n2 son distintos
    print('\n------------RESULTADO-------------')
    print('Los números en N1 y N2 son DISTINTOS!')
    if n1 > n2 : #Comprobar que n1 es mayor
        print('El número mayor es N1 con el valor: ', n1)
    else : #Si n1 no es mayor, entonces n2 es el mayor de ambos
        print('El número mayor es N2 con el valor: ', n2)
else : #Si los números no son distintos, es que son IGUALES!
    print('\n------------RESULTADO-------------')
    print('Los números son IGUALES!!!!!!')
