import random

def crear_tablero(tamaño):
    matriz=[]
    for row in range(tamaño):
        fila=[]
        for col in range(tamaño):
            fila.append(0)
        matriz.append(fila)
    return matriz

def crear_mazo(cantidad_cartas):
    cartas=[]
    for i in range(cantidad_cartas):
        i+=1
        cartas.append(i)
        cartas.append(i)
    random.shuffle(cartas) 
    return cartas   

def llenar_tablero(matriz,lista):
    contador = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if contador > len(lista)-1:
                break
            else:
                matriz[fila][columna] = lista[contador]
                contador += 1


    return matriz 

def mostrar_tablero(tablero,cantidad_cartas):
    i=0
    j=0
    print('  ',end='')
    while i < cantidad_cartas :
        print(i,end=' ')
        i+=1
    print('')
    for row in tablero:
        print(j,end=' ')
        j+=1
        for col in row:
            if col==0:
                print('  ',end='')
            else:
                print ('X ', end='')
        print('')

def memorice(tablero,cantidad_cartas):
    suma=1
    c=1
    jugador1=0
    jugador2=0 

    while suma>0:
        if c==1:
                print ("Jugador 1 jugando")
                
        else:
                print ("Jugador 2 jugando")

        print(mostrar_tablero(tablero,cantidad_cartas))
        suma=0
        cordenadax1=int(input("Ingrese la primera coordenada de su primera carta: ")) 
        cordenaday1=int(input("Ingrese la segunda coordenada de su primera carta: "))
        cordenadax2=int(input("Ingrese la primera coordenada de su segunda carta: "))
        cordenaday2=int(input("Ingrese la segunda coordenada de su segunda carta: "))

        if tablero[cordenadax1][cordenaday1]==tablero[cordenadax2][cordenaday2]:
            
            tablero[cordenadax1][cordenaday1] = 0
            tablero[cordenadax2][cordenaday2] = 0
            print(tablero)
            print(mostrar_tablero(tablero,cantidad_cartas))

            if c==1:
                jugador1+=1
                print("punto para jugador 1")
                print('')

            else:
                jugador2+=1
                print("punto para jugador 2") 
                print('')   
        else:
            if c== 1:
                c-=1
            
            else:
                c+=1

            print ('es el turno del otro jugador')

        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                    suma+=tablero[i][j]

    print('El resultado es: ',jugador1," - ",jugador2)

Cantidad_cartas=int(input('ingrese la cantidad de cartas a jugar: '))
Tablero_completo=llenar_tablero(crear_tablero(Cantidad_cartas),crear_mazo(Cantidad_cartas))
print (Tablero_completo)
#print(mostrar_tablero(Tablero_completo))
print(memorice(Tablero_completo,Cantidad_cartas))