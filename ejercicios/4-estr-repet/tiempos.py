#Calculos de tiempo
import time
f = 1 #variable f inicializada = 1
t1 = time.clock() #Primera medición time, antes de pedir valor
n = int(input('Ingrese un valor para calcular el factorial: '))
t2 = time.clock() #Segunda medición time, después del valor
for i in range(1, n+1) : #Bucle para hacer factorial
    f *= i #Calcular valor de f en cada vuelta
t3 = time.clock() #Tercera medición time, después de calucular el factorial.
tt1 = t2 - t1 #Tiempo transcurrido para introducir valor
tt2 = t3 - t2 #Tiempo transcurrido para calcular el factorial
print('\n-------RESULTADO--------')
print('Tiempo transcurrido en introducir valor: ', tt1 ,'segundos.')
print('\tTiempo transcurrido en sacar factorial de ', n ,': ', tt2 ,'segundos.')
print('\t\tFactorial: ', f)
