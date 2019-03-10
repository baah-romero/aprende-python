#Programa que pedirá introducir un numero por teclado
# en base decimal y lo convertirá a base binaria, octal,
# hexadecimal y su caracter ASCII
v1=int(input('Introducir un numero: '))#Pedir num por teclado y almacenarlo en v1
b=bin(v1) #Cambiar a binario el valor v1 y almacenar en b
print(v1, 'en binario es ', b)#Imprimir binario
o=oct(v1) #Cambiar a octal el valor v1 y almacenar en o
print(v1, 'en octal es ', o)#Imprimir octal
hx=hex(v1) #Cambiar a hexadecimal el valor v1 y almacenar en hx
print(v1, 'en hexadecimal es ', hx)#Imprimir hexadecimal
asc=chr(v1) #Cambiar a ASCII el valor v1 y almacenar en asc
print(v1, 'en ASCII es el carácter ', asc)#Imprimir binario 
