
# TASK 1

# a = int(input('Please enter number a: ')) #5
# b = int(input('Please enter number b: ')) #25
# if b * b == a:
#     print( a, 'a is the square of', b)
# elif a*a == b:
#     print(b, 'is the square of', a)
# else:
#     print('a and b are not squares of each other')

# Best solution
# num1, num2 = input() .split(",")
# if int (num1) ** 2 == int (num2) or int(num2) ** 2 == int (num1):
#     print('да')
# else:
#     print('нет')


# TASK 2
# InputList = []
# num = int(input("Enter number of elements for list : "))
# for i in range(0, num): 
#     element = int(input("Please enter the number: "))
#     InputList.append(element)   
# print('Here is the list of all values = \n', InputList)
# print(max(InputList))   

# Best Solution
# lst = [int(x) for x in input().split(',')]
# print (max(lst))


# TASK 3
#  EndNum = int(input('Please enter number '))
# StartNum = EndNum - (EndNum*2)
# i = StartNum

# while i <= EndNum:
#     print (i)
#     i+=1

# Best solution
# n = int(input ( ))
# lst = []
# for i in range(-n, n + 1):
#     lst.append(i)
#       if i != 0:
#           1st.append(i)
# print(*lst, sep=',')



# n = int (input('Введите целое число: '))
# for number in range(-n, n+1):
#     print(number)


#TASK 4

# a = float(input('Please enter float number '))
# b = int(a)
# c = round (a - b,2)
# result = int(c * 10)
# print(result)

# num = float(input ())
# float_part = num - int(num)
# print dint (float part* 10))


#TASK 5
# import re
# def checker (num):
#     if (num % 5 == 0 and num % 10 == 0) or num %15 == 0:
#         if num % 30 == 0:
#             return False
#     else:
#         return True
#     return False
# num = int (input ())
# print (checker (num))
