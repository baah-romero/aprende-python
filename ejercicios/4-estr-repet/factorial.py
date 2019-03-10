#Calcular el factorial
n = int(input('Introducir el valor que se quiere saber su factorial: '))
i, f = 0, 1 #Definir contador y valor inicial del factorial
while i < n :
    i += 1 #Incrementar +1 el contador
    f = f * i #Calcular el factorial
print('\n---------Resultado--------')
print('El factorial de ', n ,' es: ', f)
