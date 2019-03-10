#Juego que generará un número secreto aleatoriamente y el jugador
#.. deberá introducir el numero de intentos que tendrá para adivinarlo.
import random
print('Juego del numero secreto.')
limDer = int(input('Introducir el número máximo para el rango de numeros a adivinar: '))
limInte = int(input('Introducir el número de intentos para adivinar el número: '))
if limInte != 0 :
    izq, der = 1, limDer #Límites iniciales de la búsqueda
    inte = 0 #contador del número de intentos
    secreto = random.randint(1, limDer) #Generar el número aleatorio entre 1-LimDer
    encontrado = False
    while not encontrado and inte < limInte :
        inte += 1 #Sumar 1 a intentos
        print('El número a adivinar está entre ', izq ,' y ', der)
        num = izq - 1 #Inicializar num=izq-1 para entrar al bloque que pida numero para jugar
        while num < izq or num > der :
            num = int(input('[Intento :' + str(inte) + '] => Ingrese :'))
            if num < izq or num > der :  #Comprobar que el numero es válido
                print('Error, se le pidió un número entre ', izq ,' y ', der ,', vuelva a probar...')
        if num == secreto : #Comprobar si se ha encontrado el número
            encontrado = True #Sólo si el número secreto se ha encontrado
        elif num > secreto :
            der = num #Modificar el valor der para acortar el rango de numeros y facilitar encontrarlo
        else :
            izq = num #Modificar el valor izq para acortar el rango de numeros y facilitar encontrarlo
    if encontrado:
        print('\nEnhorabuena!!!! Has acertado el número secreto ', num ,' en ', inte)
    else :
        print('\nLo sentimos mucho!!! No has logrado acertar en ', inte ,' intentos,\nel número secreto era: ', secreto)
