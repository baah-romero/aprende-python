#Contador de Si
i = 0
a = input('Introducir S o s para seguir, N o n para cortar: ')
while a == 'S' or a == 's' :#Comprobar que el valor sea Si o si
    i += 1 #Al ser si, incrementar el contador en 1
    a = input('Introducir S o s para seguir, N o n para cortar: ')
print('\n-------RESULTADO--------')
print('Se han introducido ', i ,' valores S o s')
