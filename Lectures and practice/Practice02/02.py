
sentence = input('Please enter the sentence: ')
letter = input('Please enter the symbol you would like to count: ')
count=0

for i in sentence: 
     if i == letter:
         count += 1

print (f'We have {count} letters {letter} in the sentence')



# Задание 2
# Напишите программу, в которой пользователь будет задавать две струки, одна из них - буква, а вторая фраза/слово, п
# (Не используя встроенные функции)
# *Пример*
# Ввод:
# a
# abasdadsa
# Ответ: 3