# комментарий
#a = 23
#b = 'I am'
##s = False
#print(b,a,'years old' )
#print('{}-{}'.format(a,b)) 
#print(f'{a}-{b}')
#print(s)

#lists instead of arrays
#list = ['suck', 'something']

#print(list)

#input() input data
#a = input()
#b = input()
#print(a,b)    

#c = int(input())
#g = float(input())
#print(f'{c}-{g} ''what is wrong with you')
# // деление на целое число
# ** возведение в степень
# round - function that allows to minimize the number of digits after the comma
#a = 1.3235
#b = 3
#c = round(a*b,3) 
#print(c)


# logical operations

# < > <= >= ==  !=

# not , and, or
# & | 
#f = [2,2,3,4]
#print(f)
#print(not 2 in f)
#isOdd =f[0]%2 == 0
#print(isOdd)
#is_Odd = not f[0]%2 == 0
#print(is_Odd)

#a = input()
#b = input()
#if a > b:
#    print("Max nuber is", a)
#else:
#    print("Max nuber is", b)

#username = input('Please enter your name: ')
#if username == 'Mark':
#    print('Hello Mark')
#elif username == 'Dog':
#    print('Fuck you')
#else:
#    print('You shall not pass!')

# While:
#original = 237
##inverted = 0
# while original != 0:
#    inverted = inverted * 10 + (original%10)
 #   original//=10
#print(inverted)

#original = 237
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original%10)
#    original//=10

#else:
#    print('Все, хорош')    
#print(inverted)

 # for i in enumeration:
 #operator 1
 #operator 2


#for i in 1,2,3,4,5:
#    print(i**2)
#list = [1,2,3,4,5]
#for i in list:
#   print(i)
r = range (10) # or range (1,4) or range (1,4, 2) third argument shows the size of increment
#or i in r:
    #print(i)

#text = 'what is' 
#help (text.istitle)


line = " "
for i in range(1,3):
    line = "+"
    for j in range(3):
        line += "*"
print(line)