import database as db
import export 
import fakeloading as load
import time
import DBimport as dbi

def printPhonebook():
    print('---------------------------------------')
    print('Ввведите код операции: экспорт - 1, импорт - 2 ')
    i = int(input('Введите число - '))

    if  i == 1:
        print("В каком виде вы хотите экспортировать телефонную книгу?\n")
        time.sleep(0.5)
        print("1 - строчный вывод ")
        print("Фамилия_1,Имя_1,Телефон_1,Описание_1\n")
        time.sleep(1)
        print("2 - столбцом ")
        print("Фамилия_1 \nИмя_1 \nТелефон_1 \nОписание_1")  
        time.sleep(1)
        print()
        j = int(input('Введите 1 или 2 - '))
        if j == 1:
            export.ExportInOneLine(db.phonebook)
            load.loading()
        if j == 2:
            export.ExportInColumns(db.phonebook)
            load.loading()
        

printPhonebook()