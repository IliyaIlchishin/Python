
global phonebook
phonebook = [["Иванов","Антон","442213","бухгалтер"],
["Сидоров","Петр","342474","уборщик"],
["Ладья","Васильевная","236584","секретарь"],
["Хитров","Вячеслав","666999","генеральный директор"],
["Хитров","Брат","666998","заместитель генерального директора"],
]

global importdatabase
importdatabase = []

def printLST(lst):
    length = len(lst)
    temp =''
    for i in range(0,length-1):
        print()
        for j in range(0,4):
            if j == 0:
                temp = lst[i][j]
                print(f"Фамилия - {temp}, ", end='')
            if j == 1:
                temp = lst[i][j]
                print(f"Имя - {temp}, ", end='')
            if j == 2:
                temp = lst[i][j]
                print(f"Телефон - {temp}, ", end='')
            if j == 3:
                temp = lst[i][j]
                print(f"Должность - {temp} ", end='')




