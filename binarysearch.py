import random

def BinarySearch(list,findNum):
    left = 0 
    right = len(sortedList)-1
    while (left< right):
        middle = (left + right)/2
        if (findNum == list[middle]):
            return middle
        elif (findNum<list[middle]):
            right = middle - 1
        else:
            left = middle + 1
        return 'nothing'
     
lstNumbers = [random.randint(-200, 200) for i in range(25)]
print(lstNumbers)
sortedList = sorted(lstNumbers)
print (sortedList)
even = list(map(int,filter(lambda x: not x%2 and x > 50 and x<100 ,sortedList)))
print(even)
   
searchnum = 10

# result = BinarySearch(sortedList,searchnum)
# print(result)



# test = set(lst)
# test = sorted(test)
# print(test)
# test = (set(map(int,filter(lambda e: not e%2 and e>30, test))))


