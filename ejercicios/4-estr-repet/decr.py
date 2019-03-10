#Decrementar con negativos
i, sn, sp = 2, 0, 0
pos = 0
while i >= 0 :#Mientras no se hayan introducido 3 valores negativos...
    n = float(input('Introducir un número: '))
    if n < 0 : #Si el valor es < 0 (negativo)
        i -= 1 #Decrementar hasta llegar a 0
        sn += n #Sumar los valores negativos
    else : #Si el valor introducido es >= 0 (positivo)
        pos += 1 #Incrementar +1 los valores positivos
        sp += n #Sumar los positivos
print('\n--------RESULTADO---------')
print('Valores positivos introducidos: ', pos)
print('\tSuma de valores positivos: ', sp)
print('\t\tSuma de valores negativos: ', sn)
