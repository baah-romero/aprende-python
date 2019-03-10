#Piedra, papel o tijera
import random #Importa funciones Random
import time #importa funciones Tiempo
mju = "Piedra", "Papel", "Tijera" #Definir jugadas
hwi, mwi = 0, 0 #Partidas ganadas por humano o máquina = 0
cnt = 0 #Contador de rondas totales
t1 = time.clock() #Primera marca en time para iniciar el cronómetro
while hwi < 3 or mwi < 3 :
    cnt += 1
    rm = random.randint(1,3) #Jugada de la máquina
    print('\n---------Jugada [', cnt ,']--------')
    jh = int(input('1-Piedra | 2-Papel | 3-Tijera: ')) #Jugada del humano
    if (jh == 1 and rm == 3) or (jh == 2 and rm == 1) or (jh == 3 and rm == 2) :
        hwi += 1 #+1 a las rondas ganadas del humano
        print('\n\tRonda para el humano: ', mju[jh-1] ,' sobre ', mju[rm-1])
        if hwi == 3 :
            break
    elif jh == rm : #En caso de que sean iguales las jugadas...
        print('\n\tEMPATE!!! - ', mju[jh-1] ,' = ', mju[rm-1])
        continue
    else :
        mwi += 1 #+1 a las rondas ganadas por la máquina
        print('\n\tRonda para la máquina: ', mju[rm-1] ,' sobre ', mju[jh-1])
        if mwi == 3 :
            break
t2 = time.clock() #Segunda marca en timpe para parar el cronómetro
tt = round((t2 - t1), 3) #Tiempo transcurrido enla partida en segundos.
print('\n-----Resultado Final-------')
if hwi == 3 :
    print('\tGanador el Humano!!!')
elif mwi == 3 :
    print('\tGanó la máquina!!!')
print('Tiempo transcurrido en la partida: ', tt ,'segundos.')
