#Juego de piedra papel tijera entre un humano y una máquina
import random
desc = "Piedra", "Papel", "Tijera"
print('Bienvenido a Piedra-Papel-Tijera')
hum, maq, emp, cnt = 0, 0, 0, 0
tot = int(input('Número de vicotrias para ganar (Mínimo 2 rondas):'))
while tot < 2:
    tot = int(input('Error, deben jugarse al menos 2 rondas. Cuantas desea jugar: '))
while (hum < tot) and (maq < tot) :
    maquina = random.randint(1,3) #Jugada de la máquina
    print('--------------------------------------------------')
    cnt += 1 #Contador de rondas hasta tener un ganador
    print('Ronda ', cnt ,':')
    humano = int(input('\nJugar: 1-Piedra | 2-Papel | 3-Tijera :')) #Jugada del humano
    #Evaluar el resultado de la ronda jugada
    if (humano == 1 and maquina == 3) or (humano == 2 and maquina == 1) or (humano == 3 and maquina == 2) :
        hum += 1
        print('\n-> Ronda para Humano: ', desc[humano - 1] ,' sobre ', desc[maquina - 1])
    elif humano == maquina :
        emp += 1
        print('\n-> Ronda en Empate. Ya van ', emp ,' de ', cnt ,' Rondas.')
    else :
        maq += 1
        print('\n-> Ronda para la Máquina: ', desc[maquina - 1] ,' sobre ', desc[humano - 1])
    print('\nResultado actual de la partida tras la ronda ', cnt ,': ')
    print('Humano -> ', hum ,' victorias\nMáquina -> ', maq ,' victorias\nGana quien llegue antes a ', tot ,' rondas ganadas.\n\n')
vMaq = (maq / cnt) * 100
vHum = (hum / cnt) * 100
vEmp = (emp / cnt) * 100
print('--------------------------------------------------------------\n')
if hum == tot :
    print('Victoria HUMANA!!!\nRondas necesarias para ganar: ', cnt)
    print('Rondas en empate: ', emp ,' un ', vEmp ,'%')
    print('Rondas perdidas por el humano: ', maq ,', un ', vMaq ,'%')
    print('Rondas ganadas por el humano: ', hum ,', un ', vHum ,'%')
elif maq == tot :
    print('Victoria de la MAQUINA!!!\nRondas necesarias para ganar: ', cnt)
    print('Rondas en empate: ', emp ,' un ', vEmp ,'%')
    print('Rondas perdidas por la máquina: ', hum ,', un ', vHum ,'%')
    print('Rondas ganadas por la máquina: ', maq ,', un ', vMaq ,'%')
