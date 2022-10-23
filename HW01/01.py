
day = int (input('Please enter the number of the weekday: '))
if day > 0 and day <= 5:
    print('Working day ')
elif day >= 6 and day <= 7:
    print('Weekend!')
else:
    print('Please enter the number from 1 to 7')


# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
#