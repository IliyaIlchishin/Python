
def AddStudent(students_DB):
    NewStudentInput = list(input('Введите данные ученика (Фаимилия, Имя, Класс), через запятую - ').split(','))
    students_DB[NewStudentInput[0]] =  NewStudentInput[1:]
    return students_DB

def AddScores(students_DB):
    print('Введите Фамилию ученика')
    surname = input('')

    print('Выберите предмет')
    subject = int(input('1 - математика, 2 - физика  '))
    if subject == 1:
        subject_r = str('Математика')
    if subject == 2:
        subject_r = str('Физика')

    print('Введите оценку - ')
    grade = int(input(''))
    students_DB[surname].append({subject_r : [grade]})
    
    return students_DB

def StudentSearch():
    return None
    





students_DB = { 'Трубочкин' : ['Андрей','5Г'], 
                 'Лапухин' : ['Федор', '3А'],            
}




