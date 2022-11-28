import json

def AddStudent(students_DB):
    NewStudentInput = list(input('Введите данные ученика (Фаимилия, Имя, Класс), через запятую - ').split(','))
    students_DB[NewStudentInput[0]] =  NewStudentInput[1:]
    return students_DB

def AddScores(students_DB):
    print('Введите Фамилию ученика')
    surname = input('')

    print('Выберите предмет')
    subject = int(input('1 - математика, 2 - физика, 3 - Литература, 4 - Информатика  '))
    if subject == 1:
        subject_r = str('Математика')
    if subject == 2:
        subject_r = str('Физика')
    if subject == 3:
        subject_r = str('Литература')   
    if subject == 4:
        subject_r = str('Информатика') 
    print('Введите оценку - ')
    grade = int(input(''))
    students_DB[surname].append({subject_r : [grade]})
    
    return students_DB

def StudentSearch(students_DB):
    print('Введите имя студента')
    name = input('')
    flag = 0 
    for i in (students_DB):
        if i == name:
            flag=1 
    if flag > 0:
        print(f'ученик с фамилией {name} найден')
        print(f'{students_DB[name][1:]}')
    if flag == 0:
        print(f'ученика с фамилией - {name} нет в списке')
    return None
    
def save_db(students_DB) :
    json.dump(students_DB,open('DBstudent.json','w'))
    

students_DB = { 'Трубочкин' : (['Андрей','5Г'], {"Математика": [4,3,5]}), 
                'Лапухин' : (['Федор', '3А'], {"Литература": [3,5]},{"Математика": [4,5,4]} )          
}


