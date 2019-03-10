#Sacar el número máximo con if
n1 = float(input('Introducir un número: '))
n2 = float(input('Introducir otro número: '))
if n1 > n2 : #Comprobar que n1 es mayor
    print('\n------------RESULTADO-------------')
    print('El número mayor es N1 con el valor: ', n1)
else : #Si n1 no es mayor, entonces n2 es el mayor de ambos
    print('\n------------RESULTADO-------------')
    print('El número mayor es N2 con el valor: ', n2)
