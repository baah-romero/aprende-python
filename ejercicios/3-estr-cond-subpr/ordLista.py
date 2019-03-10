#Ordenar lista de nombres
no1 = input('Introducir un nómbre: ')
no2 = input('Introducir un nómbre: ')
no3 = input('Introducir un nómbre: ')
if no1 < no2 and no1 < no3:
    print('\n------------RESULTADO-------------')
    print('\t', no1)
    if no2 < no3 :
        print('\t', no2)
        print('\t', no3)
    else :
        print('\t', no3)
        print('\t', no2)
elif no2 < no1 and no2 < no3 :
    print('\n------------RESULTADO-------------')
    print('\t', no2)
    if no1 < no3 :
        print('\t', no1)
        print('\t', no3)
    else :
        print('\t', no3)
        print('\t', no1)
else :
    print('\n------------RESULTADO-------------')
    print('\t', no3)
    if no1 < no2 :
        print('\t', no1)
        print('\t', no2)
    else :
        print('\t', no2)
        print('\t', no1)
