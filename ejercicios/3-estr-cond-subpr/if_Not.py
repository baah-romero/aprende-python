#Carnet de conducir
e = int(input('Introduce tu edad: '))
if not e < 18 : #not hace que sea si no e es menor que 18 (e es mayor?)
    print('\n------------RESULTADO-------------')
    print('Puede acceder a sacarse el carnet!')
else :
    print('\n------------RESULTADO-------------')
    print('No puede acceder, es menor de edad!')
