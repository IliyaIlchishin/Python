import database as DB




def ExportInOneLine(lst):
    length = len(lst)
    temp =''
    for i in range(0,length-1):
        
        for j in range(0,4):

            if j == 0:
                temp = lst[i][j]
                with open('export.txt', 'a') as file:
                    file.write(f'Фамилия - {temp}, ')
            if j == 1:
                temp = lst[i][j]
                with open('export.txt', 'a') as file:
                    file.write(f'Имя - {temp}, ')
            if j == 2:
                temp = lst[i][j]
                with open('export.txt', 'a') as file:
                    file.write(f'Телефон - {temp}, ')
            if j == 3:
                temp = lst[i][j]
                with open('export.txt', 'a') as file:
                    file.write(f'Должность - {temp};\n')

def ExportInColumns(lst):
    length = len(lst)
    temp =''
    for i in range(0,length-1):
        
        for j in range(0,4):

            if j == 0:
                temp = lst[i][j]
                with open('export.txt', 'a') as file:
                    file.write(f'Фамилия - {temp}, \n')
            if j == 1:
                temp = lst[i][j]
                with open('export.txt', 'a') as file:
                    file.write(f'Имя - {temp}, \n')
            if j == 2:
                temp = lst[i][j]
                with open('export.txt', 'a') as file:
                    file.write(f'Телефон - {temp}, \n')
            if j == 3:
                temp = lst[i][j]
                with open('export.txt', 'a') as file:
                    file.write(f'Должность - {temp};\n')
                    file.write(f'\n')            


