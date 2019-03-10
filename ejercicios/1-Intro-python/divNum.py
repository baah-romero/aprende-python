print('Programa que hace la división entera, división con decimales\n y el resto de la división de 2 numeros decimales.')
n1 = float(input('Introducir un numero decimal: '))
n2 = float(input('Introducir un numero decimal: '))
de,dd,rd = n1 // n2, n1 / n2, n1 % n2
print('División Entera: ', n1 ,'//', n2 ,'=', de)
print('División con Decimales: ', n1 ,'/', n2 ,'=', dd)
print('Resto de la División: ', n1 ,'%', n2 ,'=', rd)
