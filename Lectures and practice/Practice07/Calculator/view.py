import calculation as calc
import input

def collect_and_result():
    a = input.inputdata()
    lst = input.parse(a)
    result = calc.calculate(lst)
    
    return result


result = collect_and_result
print(str(result))