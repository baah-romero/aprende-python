#Ordenar alfabeticamente 2 nombres
nom1 = input('Introducir un nombre: ')
nom2 = input('Introducir un nombre: ')
if nom1 != nom2 : #Comprobar si los nombres son distintos
    print('\n------------RESULTADO-------------')
    print('Los Nombres son DISTINTOS!')
    if nom1 < nom2 : #Comprobar que nom1 es menor
        print(nom1) #nom1 está mas cercano a la A en el diccionario
        print(nom2) #nom2 está detrás en el diccionario
    else : #Si nom1 es mayor, entonces nom2 es el menor de ambos
        print(nom2) #nom2 está mas cercano a la A en el diccionario
        print(nom1) #nom1 está detrás en el diccionario
else : #Si los nombres no son distintos, es que son IGUALES!
    print('\n------------RESULTADO-------------')
    print('Los números son IGUALES!!!!!!')
