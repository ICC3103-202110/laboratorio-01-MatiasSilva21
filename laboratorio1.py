def crear_tablero():
    tablero1=[]
    tablero2=[]
    for i in range(5):
        tablero1.append(0)
    for j in range(4):
        tablero2.append(tablero1)
            
    return tablero2
      
print (crear_tablero())      