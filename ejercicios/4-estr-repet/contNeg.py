#Contar los negativos de una serie
n = int(input('Cuantos números tendrá la serie? '))
cne = 0 #Declarar contador
for i in range(n) : #repetir n veces
    t = int(input('Valor: '))
    if t < 0 : #Comprobar si el valor es menor que 0
        cne += 1 #si es negativo, +1 al contador
print('\n-----RESULTADO-------')
print('Se han introducido ', cne ,' números negativos.')
