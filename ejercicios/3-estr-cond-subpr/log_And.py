#Prestamos
s = float(input('Introducir el sueldo: '))
a = int(input('Introducir la antigüedad en años exactos: '))
if s >= 700 and a >= 3 : #Comprobar si cobra más de 700 y lleva 3 años
    print('\n------------RESULTADO-------------')
    print('Préstamo concedido!!!!') #Si cumple ambas condiciones se le presta.
else : #Si no se cumplen ambas, se búsca que le falta para poder prestar.
    print('\n------------RESULTADO-------------')
    sr, sa = 700 - s, 3 - a #sr será € faltan y sa los años que faltan
    if s < 700 : #Comprobar si lo que falta es € en la nómina
        print('Te faltan ', sr ,'€ más en el sueldo para poder prestarte.')
    if a < 3 : #Comprobar si lo que falta es antigüedad
        print('Te faltan ', sa ,' años en la empresa para poder prestarte.')
