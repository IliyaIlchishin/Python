import datetime as dt

def logger(lst,result):
    with open('file.txt', 'a') as file:
        first_input = ''.join(lst)
        file.write(first_input,int(result))

