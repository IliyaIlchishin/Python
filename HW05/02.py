import random
import time

field = [1,2,3,
         4,5,6,
         7,8,9]

WhenWins = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def DrawField(field):
    print("-------------")
    for i in range(3):
        print ("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print ("-------------")

def PlayerNames():
        print('Пожалуйста введите имя игрока')
        player = input('Имя игрока - ')
        return player

def FirstMove(player1,player2):
        n = random.randint(1,2)
        switch = 0
        if n == 1:
                switch = 1
                return switch
        if n == 2:
                switch = 2
                return switch

def PlaceSymbol(move,symbol):
    field[move-1] = symbol

def WinCondition(field, player1,player2):
    win = ''
    for i in WhenWins:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = player1
            print(f'Игра окончена, победил {player1}')
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = player2  
            print(f'Игра окончена, победил {player2}')
             
    return win

GameOver = False
player1 = PlayerNames()
player2 = PlayerNames()
switch = FirstMove(player1,player2)

while GameOver == False:
        DrawField(field)
        if switch == 1:
                print(f'Ход игрока - {player1}')
                symbol = "X"
                move = int(input(f'{player1}, выбери ячейку: '))
                switch+=1
        elif switch == 2:
                print(f'Ход игрока - {player2}')
                symbol = "O"
                move = int(input(f'{player2}, выбери ячейку: '))
                switch-=1
        PlaceSymbol(move,symbol)
        win = WinCondition(field,player1,player2)
        if win != '':
                GameOver = True
        else:
                GameOver = False
DrawField(field)
print("Игра окончена")        
print(f'Победил {win}')   


 