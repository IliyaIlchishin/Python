import studentsDB as STDB


def WorkingMode():
    print('Пожалустай выберите режим доступа к личному кабинету')
    print('1 - преподаватель, 2 - ученик')
    a = int(input('Введите 1 или 2 '))
    if a == 1:
        print('Выберите режим работы:')
        mode = int(input('1 -  добавить ученика, 2 - добавить оценку, 3 - выйти из программы '))
        while mode == 1 or mode == 2: 
            if mode == 1:
                STDB.AddStudent(STDB.students_DB)
                print('Что дальше?')
                mode = int(input('1 -  добавить ученика, 2 - добавить оценку, 3 - выйти из программы '))
            if mode == 2:
                STDB.AddScores(STDB.students_DB)
                print('Что дальше?')
                mode = int(input('1 -  добавить ученика, 2 - добавить оценку, 3 - выйти из программы '))
        if mode == 3: 
            print(STDB.students_DB)

    if a == 2:
        print('Выберите режим работы:')
        mode = int(input('1 - найти студента по фамилии, 2 - выйти из программы '))
        if mode == 1:
            STDB.StudentSearch(STDB.students_DB)
            print()
        if mode == 2:
            print('До свидания!')


WorkingMode()