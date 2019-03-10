#Contar negativos con for
cnt = 0
for i in range(3) :
    n = int(input('Introducir numero: '))
    if n < 0 :
        cnt += 1
print('\n-----RESULTADO-------')
print('Se han introducido ', cnt ,' números negativos.')
