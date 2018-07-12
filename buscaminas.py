from __future__ import print_function
from random import randint

def mostrarMatriz(matriz):
    longitud = len(matriz)
    print(' | 1 2 3 4 5 6 7 8\n')
    print('  ----------------\n')
    for i in range (longitud):
        print(str(i+1) + '| ', end = '')
        for j in range (longitud):
            print(str(matriz[i][j]) +' ', end='')
        print('\n')

def revisarMatriz(matriz):
    longitud = len(matriz)
    cont = 0

    for i in range (longitud):
        for j in range (longitud):
            if(matriz[i][j] == 'O'):
                cont += 1
    
    return cont
            

def sitioRandom(matriz):
    y = randint(0,len(matriz)-1)
    x = randint(0,len(matriz)-1)
    while(matriz[y][x] == 1):
        print(matriz[y][x])
        y = randint(0,len(matriz)-1)
        x = randint(0,len(matriz)-1)

    matriz[y][x] = 1

def llenarMatriz(matriz, minas):
    for i in range (minas):
       sitioRandom(matriz)

def contarMinas(matriz, y, x, flag):
    longitud = len(matriz)
    minas = 0

    for i in range (-1,2):
        for j in range(-1,2):
            if(i == 0 and j == 0):
                continue
            elif(-1 < (y+i) < longitud and -1 < (x+j) < longitud):
                if(matriz[y+i][x+j] == 1):
                    minas += 1
    
    return minas

def iniciar():
    minas = 10
    longitud = 8
    restantes = minas

    matrizJuego = [['O' for i in range(longitud)] for i in range(longitud)]
    matriz = [['0' for i in range(longitud)] for i in range(longitud)]
    banderas = []

    llenarMatriz(matriz, minas)
    mostrarMatriz(matrizJuego)
    #mostrarMatriz(matriz)
    print('Bienvenido al buscaminas v1.0')
    print('Para jugar necesitas saber dos cosas antes que nada:')
    print('1) Las X son las coordenadas horizontales, de izquierda a derecha')
    print('2) Las Y son las coordenadas verticales, de arriba hasta abajo')
    print('Para jugar solo necesitas colocar las coordenadas y seguir las instrucciones\n')

    while True:
        mostrarMatriz(matrizJuego)
        print('Minas restantes: {}'.format(restantes))
        try:
            y = int(raw_input('Ingresa la coordenada en Y:'))
            x = int(raw_input('Ingresa la coordenada en X:'))
        except ValueError:
            print('Solo puedes ingresar numeros en este campo')
            continue
        
        if not(1 <= x <= longitud or 1 <= y <= longitud):
            print('Solo puedes ingresar valores del 1 al {} en ambos campos'.format(longitud))
            continue

        flag = raw_input('Es bandera? (s/n):')
        while(flag.lower() != 's' and flag.lower() != 'n'):
            print('Solo puede ingresar s o n en este campo')
            flag = raw_input('Es bandera? (s/n):')

        y -= 1
        x -= 1

        if(matrizJuego[y][x] == 'F' and flag.lower() == 's'):
            print('Ya existe una bandera en este sitio')
            opt = raw_input('Desea quitar esta bandera? (s/n):')

            while(opt.lower() != 's' and opt.lower() != 'n'):
                print('Solo puede ingresar s o n en este campo')
                opt = raw_input('Desea quitar esta bandera? (s/n):')

            if(opt.lower() == 's'):
                print('entra')
                matrizJuego[y][x] = 'O'
                restantes += 1
                continue
            else:
                continue


        if(restantes == 0 and flag.lower() == 's'):
            print('Ya has colocado el maximo de banderas, intenta nuevamente')
            continue

        if(matriz[y][x] == 1 and flag.lower() == 'n'):
            print('Has caido en una mina :(')
            iniciar()
            return

        if(flag.lower() == 'n'):
            matrizJuego[y][x] = contarMinas(matriz, y, x, flag)
        else:
            matrizJuego[y][x] = 'F'
            restantes -= 1

        termino = revisarMatriz(matrizJuego)

        if(termino == 0):
            print('Felicidades! Has completado esta partida de buscaminas')
            break
            
iniciar()