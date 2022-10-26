
def fibonacci (num):
    
    if num in [1,2]:
        return 1
    else:
       return fibonacci(num - 1) + fibonacci(num-2)
      
lst = [0]
for e in range (1, 10):
    lst.append (fibonacci(e))
print (lst) 

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке