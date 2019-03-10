#Primer programa con caracteres especiales
nom = input('Inserte su nombre: ')
ape = input('Inserte su apellido: ')
c = nom + ' ' + ape
r = nom * 3
print("\n-----------Control de caracteres especiales------------\n")
print('Salto de Línea: ', nom ,'\n', ape ,'\n-------')
print('Tabulación: ', nom ,'\t', ape ,'\n-------')
print('Comillas dobles: \"', nom ,'\" - Comillas simples: \'', ape ,'\'\n-------')
print('Concatenación nombre y apellido: ', c ,'\n-------')
print('Repetición de Nombre: ', r ,'\n--------')
a = nom
nom = input('Inserte su nuevo nombre: ')
print('Ha modificado el nombre de ', a ,' por ', nom)
