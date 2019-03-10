#Número secreto entre 1-10
import random #Importar libreria random
r = random.randint(1,10) #Generar aleatorio entre 1-10
izq, der, a = 1, 10, 0 #Definir limites y contador
for i in range(3) : #Bucle de 3 intentos para acertar
    a += 1 #Contador de intentos
    pr = int(input('Probar suerte: '))
    if pr != r : #Comprobar si el número aleatorio es igual al intento
        #Controlar el rango a adivinar
        if pr > r :
            der = pr #El rango maximo es pr ahora como ayuda
        else :
            izq = pr #El rango minimo es pr por ahora
        print('-----\nError, el valor está entre ', izq ,' y ', der)
        print('\tLe quedan ', (2 - i) ,' intentos.\n-------\n')
    else :
        print('\nHas acertado!!!!\n\tNecesitaste ', a ,' intentos.')
        break #corta la ejecución de FOR cuando se acierta
