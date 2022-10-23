# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]
# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

def NegativePositiveRange (list):
    r = int(input('Please enter number: \n'))  
    for i in range (-r,r+1):
        list.append(i)
    print(f'The list of ellements from {-r} to {r}')
    print(f'{elements}\n')
   
def DeleteNegative (list):
    length = len(list)
    
    newlist = []
    i = 0
    while i < (length):
        if list[i]>0:
            newlist.append(list[i])
            i+=1
        else: i+=1
    return (newlist)
 
def ProductOfNumbers (list):
    index = [2,4,3,1,8] 
    product = 1               
    for i in range(0,len(index)-1):
        product = product * list[index[i]]
    return product

def SumOfEven(list):
    sum=0
    for i in range(len(list)):
        if list[i]%2==0:
            sum=sum+list[i]
    return sum

elements = []   
NegativePositiveRange(elements)
elements = DeleteNegative(elements)
print (f'{elements}\n')

product = ProductOfNumbers(elements)
print(f'The product of elements is {product}\n')

SumEven = SumOfEven(elements)
print(f'The sum of even numbers is {SumEven} \n')