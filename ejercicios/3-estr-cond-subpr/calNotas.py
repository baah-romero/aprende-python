#Cálculo de nota media
n1 = float(input('Nota primer trimestre: '))
n2 = float(input('Nota segundo trimestre: '))
n3 = float(input('Nota tercer trimestre: '))
m = round((n1 + n2 + n3) / 3, 1) #Calcular media redondeada a 1 decimal
if m >= 0 and m < 2.5 :
    print('\n------------RESULTADO-------------')
    print('\tMuy Deficiente - ', m)
elif m >= 2.5 and m < 4.5 :
    print('\n------------RESULTADO-------------')
    print('\tSuspenso, ponte las pilas - ', m)
elif m >= 4.5 and m < 5 :
    print('\n------------RESULTADO-------------')
    print('\tSuspenso, un pelín de esfuerzo y apruebas - ', m)
elif m >= 5 and m < 6 :
    print('\n------------RESULTADO-------------')
    print('\tSuficiente - ', m)
elif m >= 6 and m < 7 :
    print('\n------------RESULTADO-------------')
    print('\tBien - ', m)
elif m >= 7 and m < 8.5 :
    print('\n------------RESULTADO-------------')
    print('\tNotable - ', m)
elif m >= 8.5 and m < 9.5 :
    print('\n------------RESULTADO-------------')
    print('\tSobresaliente - ', m)
elif m >= 9.5 and m <= 10 :
    print('\n------------RESULTADO-------------')
    print('\tExcelente - ', m)
else :
    print('\n------------RESULTADO-------------')
    print('\tERROR, no puede existir nota mayor que 10 - ', m)
