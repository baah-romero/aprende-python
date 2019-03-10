#Programa que pedirá introducir un carácter por teclado
#  y lo convertirá a base binaria, octal, decimal y hexadecimal

v2=input('Introducir una letra: ')
c=ord(v2) #Convertir a decimal el valor ASCII introducido
print(v2 ,' en binario es ', bin(c)) #Imprimir el valor en binario
print(v2 ,' en octal es ', oct(c)) #Imprimir el valor en octal
print(v2 ,' en decimal es ', c) #Imprimir el valor en decimal
print(v2 ,' en hexadecimal es ', hex(c)) #Imprimir el valor en hexadecimal
