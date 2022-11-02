from itertools import count
import random
import time

# Option 1 - Туповатый бот 

# def RandCandies (step,candy):
    
#     takeCandy = random.randint(1,step)
#     if candy < step:
#         takeCandy = candy
#         return int(takeCandy)
#     return int(takeCandy)

# def Intro(candy, step):
#     intro = (f'Добро пожаловать ненасытный странник!\n'
#             'Внимательно прочти правила прежде, чем начать\n'
#             'На столе {candy} конфет\n'
#             'За раунд ты можешь взять не более {step} конфет\n'    
#             'Побеждет то, кто забирет последние конфеты\n')
#     print(intro)
#     print(f'========= Введи свое мя игрок ========')
#     player = input('Имя - ')
#     return player

# candy = 121
# step = 28 
# PlayerScore = 0 #Кол-во конфет 1го игрока
# BotScore = 0 #Кол-во конфет 2го игрока
# count = 0
# player = Intro(candy, step)


# while candy >= 0:

#     print(f'====== Ход Игрока ======')
#     time.sleep(1)
#     playerTakes = int(input(f'Твой ход {player}\n'))
#     count+=1
#     if playerTakes > step:
#         print(f'Смотри не лопни. За ход можно взять только {step} конфет')
#         time.sleep(1)
#         playerTakes = int(input(f'Сколько конфет ты берешь, {player}? \n'))
#     PlayerScore = PlayerScore+playerTakes
#     candy = candy - playerTakes
#     print(f'На столе осталось {candy} конфет')
#     time.sleep(1)
#     print(f'====== Ход компьютера ======')
#     time.sleep(1)

#     botTakes = RandCandies(step,candy)
#     BotScore=BotScore+botTakes
#     print(botTakes)
#     count+=1
#     candy = candy - botTakes
#     print(f'На столе осталось {candy} конфет')
#     time.sleep(1)
#     print(f'======Текущий счет=======')
#     print(f'Кол-во конфет у {player}: {PlayerScore}')
#     print(f'Кол-во конфет у компютера: {BotScore}')
# if count % 2 == 1:
#     print(f'**********************************************')
#     print(f'**********************************************')
#     print(f'======== Победил {player} ========')
#     print(f'**********************************************')
#     print(f'**********************************************')
# else:
#     print(f'**********************************************')
#     print(f'**********************************************')
#     print(f'======== Победил компютер ========')
#     print(f'**********************************************')
#     print(f'**********************************************')


# Option 2 -  Бот с мозгами???
# while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step


def CandiesPerRound (step,candy, playerTakes):
    if candy >= 29:
        for i in range (step+1,(step*2)-playerTakes):
            if candy % i == 0 :
                targetStep = i #30
                print(targetStep)
                takeCandy = targetStep - playerTakes
                print (takeCandy)
            if candy % i == 1 :
                targetStep = i #30
                print(targetStep)
                takeCandy = targetStep - playerTakes
                print (takeCandy)
    if candy < step:
        takeCandy = candy
        print(takeCandy)
   

CandiesPerRound(28,172,12)


# def Intro(candy, step):
#     intro = (f'Добро пожаловать, ненасытный странник!'
#              'Внимательно прочти правила прежде, чем начать'
#              'На столе {candy} конфет'
#              'За раунд ты можешь взять не более {step} конфет'    
#              'Побеждает то, кто заберет последние конфеты')
#     print(intro)
#     print(f'========= Введи свое мя игрок ========')
#     player = input('Имя - ')
#     return player

# candy = 121
# step = 28 
# PlayerScore = 0 #Кол-во конфет 1го игрока
# BotScore = 0 #Кол-во конфет 2го игрока
# count = 0
# player = Intro(candy, step)

# while candy > 0:

#     print(f'====== Ход Игрока ======')
#     time.sleep(1)
#     playerTakes = int(input(f'Твой ход {player}\n'))
#     count+=1
#     if playerTakes > step:
#         print(f'Смотри не лопни. За ход можно взять только {step} конфет')
#         time.sleep(1)
#         playerTakes = int(input(f'Сколько конфет ты берешь, {player}? \n'))
#     PlayerScore = PlayerScore+playerTakes
#     candy = candy - playerTakes
#     print(f'На столе осталось {candy} конфет')
#     time.sleep(1)
#     print(f'====== Ход компьютера ======')
#     time.sleep(1)

#     botTakes = RandCandies(step,candy)
#     BotScore=BotScore+botTakes
#     print(botTakes)
#     count+=1
#     candy = candy - botTakes
#     print(f'На столе осталось {candy} конфет')
#     time.sleep(1)
#     print(f'======Текущий счет=======')
#     print(f'Кол-во конфет у {player}: {PlayerScore}')
#     print(f'Кол-во конфет у компютера: {BotScore}')
# if count % 2 == 1:
#     print(f'**********************************************')
#     print(f'**********************************************')
#     print(f'======== Победил {player} ========')
#     print(f'**********************************************')
#     print(f'**********************************************')
# else:
#     print(f'**********************************************')
#     print(f'======== Победил компютер ========')
#     print(f'**********************************************')
#     print(f'**********************************************')






# # 1) Создайте программу для игры с конфетами человек против бота.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# # Первый ход делает человек. За один ход можно забрать не более чем 28 конфет. 
# # Все конфеты оппонента достаются сделавшему последний ход. 
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# # 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф
# # a) Добавьте игру против бота
# # *** b) Подумайте как наделить бота ""интеллектом"" (Теория игр)




# # ОТВЕТ: Первому  игроку  надо первым ходом забрать остаток от целочисленного деления
# # имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1
# # В дальнейшем первому игроку нужно повторять стратегию, хотя без калькулятора не всегда это удобно посчитать))))
# # Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
# # если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19 и так далее..
# # Это как реализовано в игре против компа, хотя я прау раз выиграл, видимо не совсем правильно работает(((((





