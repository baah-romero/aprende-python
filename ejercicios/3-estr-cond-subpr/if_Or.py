#Comprobador de explotación laboral
s = float(input('Introducir el sueldo con 2 decimales en €: '))
h = int(input('Introducir el número de horas trabajadas esta semana: '))
if s < 950 or h > 40 : #el sueldo es menor a 950 ó curra más de 40h?
    print('\n------------RESULTADO-------------')
    print('Te están EXPLOTANDO -> Cambia de curro!')
if s >= 950 and h <= 40 : #Si cobra más de 950 y curra menos de 40h
    print('\n------------RESULTADO-------------')
    print('Buen curro!')
