#Sumar números
ac, a, i = 0, 'S', 0 #Definición de variables
while a == 'S' or a == 's' : #Comporbar que se desea seguir ejecutando
    n = float(input('Introducir un número: '))
    ac += n #Incrementar acumulador con valor de n
    i += 1 #contar cuantos valores se han introducido
    a = input('Desea continuar? (S o s para si, otro valor para cortar: )')
print('\n---------RESULTADO--------')
print('Se han introducido ', i ,' números.')
print('\tLa suma de todos ellos es ', ac)
