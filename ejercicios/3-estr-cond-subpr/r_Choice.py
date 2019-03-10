#menú elecciones
import random #Importa la libreria random para las funciones
cad1 = 'Hola', 'Adios', 'Tarde'
rc = random.choice(cad1) #Escoger aleatoriamente el valor de una palabra de cad1
hum = input('Introducir un valor (Hola, Adios o Tarde) para adivinar: ')
if hum == rc : #Comprobación de si el humano ha acertado la palabra aleatoria
    print('\n------------RESULTADO-------------')
    print('Has ACERTADO!!!')
else : #Si el humano ha fallado
    print('\n------------RESULTADO-------------')
    print('Has FALLADO!!!')
    print('La cadena aleatoria escogida es: ', rc) #Mostrar la cadena random
