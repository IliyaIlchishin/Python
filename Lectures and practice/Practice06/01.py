
def parse (s):
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol 
        else:
            result.append(int (digit))
            digit = ""
            result.append (symbol)
    else:
        # if digit: 
        result.append(int (digit))
    return result

def calculate(lst):
    result = 0
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index-1] / lst[index+1]
        lst= lst[:index-1] +[result]+lst[index+2:]
    
    while '+' in lst:
        index = lst.index('+')
        result = lst[index-1] + lst[index+1]
        lst = lst[:index-1] + [result]+lst[index+2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index-1]- lst[index+1]
        lst = lst[:index-1] + [result]+lst[index+2:]
    return round(result,2)



s = "2+2*2/2+3"
lst = parse(s)
print(lst)

result = calculate(lst)
print(f'Результат {result}')




# Напишите программу вычисления арифметического выражения заданого строкой. 
# Используйте операции +, -,/,*. приоритет операций стандартный
# *Пример: *
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример: *
# 1+2*3 => 7;
# (1+2)*3 => 9;