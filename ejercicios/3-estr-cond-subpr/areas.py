#Cálculo de áreas
n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))
n3 = float(input('Valor 3: '))
if n1 != n3 and n1 != n2 and n2 != n3 :
    if n1 > n2 and n1 > n3 :
        may = n1
        if n2 > n3 :
            med, mn = n2, n3
        else :
            med, mn = n3, n2
    elif n2 > n1 and n2 > n3 :
        may = n2
        if n1 > n3 :
            med, mn = n1, n3
        else :
            med, mn = n3, n1
    elif n3 > n1 and n3 > n2 :
        may = n3
        if n1 > n2 :
            med, mn = n1, n2
        else :
            med, mn = n2, n1
    at, ac, ar = (may * med) / 2, med ** 2, may * med
    aes = 2 * 3.1416 * (mn ** 2)
    print('\n------------RESULTADO-------------')
    print('Mayor = ', may ,' | Mediano = ', med ,' | Menor = ', mn)
    print('\tTriángulo: (b*h)/2 - (', may ,'*', med ,') / 2 = ', at)
    print('\tCuadrado: lado^2 - (', may ,'^2) = ', ac)
    print('\tRectángulo: (b*h) - (', may ,'*', med ,') = ', ar)
    print('\tCirculo: 2pi*r^2 - (2*3.1416*', mn ,'^2) = ', aes)
