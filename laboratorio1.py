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
            
def mostrar_tablero1(tablero,cantidad_cartas,cordx1,cordy1):
    i=0
    j=0
    w=0
    q=0

    print('  ',end='')
    while i < cantidad_cartas :
        print(i,end=' ')
        i+=1
    print('')
    while w<len(tablero):
        print(j,end=' ')
        j+=1
        while q<len(tablero[w]):
            if tablero[w][q]==0:
                print('  ',end='')
            elif tablero[w][q] == tablero[cordx1][cordy1]:
                if w== cordx1 and q== cordy1:
                 print(str(tablero[cordx1][cordy1]),end=' ')
                else:     
                    print ('X ', end='')
            else:
                    print ('X ', end='')
            q+=1
        q=0
        w+=1            
        print('')

def mostrar_tablero2(tablero,cantidad_cartas,cordx1,cordy1,cordx2,cordy2):
    i=0
    j=0
    w=0
    q=0

    print('  ',end='')
    while i < cantidad_cartas :
        print(i,end=' ')
        i+=1
    print('')
    while w<len(tablero):
        print(j,end=' ')
        j+=1
        while q<len(tablero[w]):
            if tablero[w][q]==0:
                print('  ',end='')
            elif tablero[w][q] == tablero[cordx1][cordy1]:
                if w== cordx1 and q== cordy1:
                 print(str(tablero[cordx1][cordy1]),end=' ')
                else:     
                    print ('X ', end='')
            elif tablero[w][q] == tablero[cordx2][cordy2]:
                if w== cordx2 and q== cordy2:
                 print(str(tablero[cordx2][cordy2]),end=' ')
                else:     
                    print ('X ', end='')        
            else:
                    print ('X ', end='')
            q+=1
        q=0
        w+=1            
        print('')
def memorice(tablero,cantidad_cartas):
    suma=1
    c=1
    jugador1=0
    jugador2=0 
    
    while suma>0:
        print(mostrar_tablero(tablero,cantidad_cartas))
        if c==1:
                print ("Jugador 1 jugando")
                
        else:
                print ("Jugador 2 jugando")

        suma=0
        cordenadax1=int(input("Ingrese la primera coordenada de su primera carta: ")) 
        cordenaday1=int(input("Ingrese la segunda coordenada de su primera carta: "))
        print(mostrar_tablero1(tablero,cantidad_cartas,cordenadax1,cordenaday1))
        cordenadax2=int(input("Ingrese la primera coordenada de su segunda carta: "))
        cordenaday2=int(input("Ingrese la segunda coordenada de su segunda carta: "))
        print(mostrar_tablero2(tablero,cantidad_cartas,cordenadax1,cordenaday1,cordenadax2,cordenaday2))
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
#print (Tablero_completo)
#print(mostrar_tablero(Tablero_completo))

#Solo falta cambiar nombre de variables a ingles y ordenar un poco el codigo

print(memorice(Tablero_completo,Cantidad_cartas))