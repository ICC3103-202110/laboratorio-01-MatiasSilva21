import random

def create_board(card_count):
    board=[]
    for row in range(card_count):
        line=[]
        for col in range(card_count):
            line.append(0)
        board.append(line)
    return board

def create_deck(card_count):
    cards=[]
    for card in range(card_count):
        card+=1
        cards.append(card)
        cards.append(card)
    random.shuffle(cards) 
    return cards   

def fill_board(board,cards):
    counter = 0
    for row in range(len(board)):
        for col in range(len(board[row])):

            if counter > len(cards)-1:
                break

            else:
                board[row][col] = cards[counter]
                counter += 1


    return board 

def show_board(board,card_count):
    horizontal_cords=0
    vert_cords=0
    print('  ',end='')

    while horizontal_cords < card_count :
        print(horizontal_cords,end=' ')
        horizontal_cords+=1
    print('')

    for row in board:
        print(vert_cords,end=' ')
        vert_cords+=1

        for col in row:
            if col==0:
                print('  ',end='')

            else:
                    print ('X ', end='')

        print('')
            
def show_board_1(board,card_count,cordx1,cordy1):
    horizontal_cords=0
    vert_cords=0
    counter_1=0
    counter_2=0

    print('  ',end='')
    while horizontal_cords < card_count :
        print(horizontal_cords,end=' ')
        horizontal_cords+=1
    print('')

    while counter_1<len(board):
        print(vert_cords,end=' ')
        vert_cords+=1

        while counter_2<len(board[counter_1]):
            if board[counter_1][counter_2]==0:
                print('  ',end='')

            elif board[counter_1][counter_2] == board[cordx1][cordy1]:
                if counter_1== cordx1 and counter_2== cordy1:
                 print(str(board[cordx1][cordy1]),end=' ')

                else:     
                    print ('X ', end='')

            else:
                    print ('X ', end='')

            counter_2+=1

        counter_2=0
        counter_1+=1            
        print('')

def show_board_2(board,card_count,cordx1,cordy1,cordx2,cordy2):
    horizontal_cords=0
    vert_cords=0
    counter_1=0
    counter_2=0

    print('  ',end='')
    while horizontal_cords < card_count :
        print(horizontal_cords,end=' ')
        horizontal_cords+=1
    print('')

    while counter_1<len(board):
        print(vert_cords,end=' ')
        vert_cords+=1

        while counter_2<len(board[counter_1]):
            if board[counter_1][counter_2]==0:
                print('  ',end='')

            elif board[counter_1][counter_2] == board[cordx1][cordy1]:
                if counter_1 == cordx1 and counter_2== cordy1:
                 print(str(board[cordx1][cordy1]),end=' ')

                else:     
                    print ('X ', end='')

            elif board[counter_1][counter_2] == board[cordx2][cordy2]:

                if counter_1 == cordx2 and counter_2== cordy2:
                 print(str(board[cordx2][cordy2]),end=' ')

                else:     
                    print ('X ', end='')  

            else:
                    print ('X ', end='')

            counter_2+=1

        counter_2=0
        counter_1+=1            
        print('')

def memorice(board,card_count):
    summ=1
    change_player=1
    player_1=0
    player_2=0 
    
    while summ>0:
        print(show_board(board,card_count))
        if change_player==1:
                print ("Player 1 playing")
                
        else:
                print ("Player 2 playing")

        summ=0
        cordx1=int(input("Enter the first coordinate of your first card: ")) 
        cordy1=int(input("Enter the second coordinate of your first card: "))

        print(show_board_1(board,card_count,cordx1,cordy1)) 

        cordx2=int(input("Enter the first coordinate of your second card: "))
        cordy2=int(input("Enter the second coordinate of your second card: "))
        
        print(show_board_2(board,card_count,cordx1,cordy1,cordx2,cordy2))
        if board[cordx1][cordy1]==board[cordx2][cordy2]:
            
            board[cordx1][cordy1] = 0
            board[cordx2][cordy2] = 0
            
            print(show_board(board,card_count))

            if change_player==1:
                player_1+=1
                print("point for player 1")
                print('')

            else:
                player_2+=1
                print("point for player 2") 
                print('')   
        else:
            if change_player== 1:
                change_player-=1
            
            else:
                change_player+=1

            print ('is the turn of the other player')

        for i in range(len(board)):
            for j in range(len(board[i])):
                    summ+=board[i][j]

    print('the final result: ',player_1," - ",player_2)

Card_count=int(input('how many cards would you like to play: '))
full_board=fill_board(create_board(Card_count),create_deck(Card_count))


#actualizado a ingles

print(memorice(full_board,Card_count))