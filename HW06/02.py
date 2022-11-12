
lst = [12,'sadf',5643] 
num_lst = list(filter(lambda x: type(x) == int, lst))
print(num_lst)
str_lst = list(filter(lambda x: type(x) == str, lst))
print(str_lst)
 
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

