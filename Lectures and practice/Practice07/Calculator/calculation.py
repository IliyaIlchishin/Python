import input

def calculate(lst):
    result = 0
    for s in lst:
        if s == '*' or s == '/':
            if s == '*':
                index = lst.index(s)
                result = lst[index - 1] * lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index-1] / lst[index+1]
                lst= lst[:index-1] +[result]+lst[index+2:]
    
    for s in lst:
        if s == '+' or s == '-':
            if s == '+':
                index = lst.index(s)
                result = lst[index - 1] + lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index-1] - lst[index+1]
                lst= lst[:index-1] +[result]+lst[index+2:]
    return round(result,2)


