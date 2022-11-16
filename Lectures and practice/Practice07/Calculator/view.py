import calculation as calc
import input
import logging as log


def collect_and_result():
    global a
    a = input.inputdata()
    lst = input.parse(a)
    res = calc.calculate(lst)
    
    return res


def res_print(res):
    print(f" {a} = {res}")





