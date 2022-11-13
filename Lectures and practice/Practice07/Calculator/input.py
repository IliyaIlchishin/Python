


def inputdata():
    first_input = str(input('вводите данные - '))
    return first_input

def parse(data):
    result = []
    digit =""
    for i in data:
        if i.isdigit():
            digit += i
        else:
            result.append(int(digit))
            digit =""
            result.append(i)
    else:
        result.append(int(digit))
    return result

