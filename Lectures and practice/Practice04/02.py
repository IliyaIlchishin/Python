import math

def find_roots(a, b, c):
    d = b ** 2 -4 * a * c
    if d > 0:
        x1 = -b + (d**0.5)/(2*a)
        x2 = -b + (d**0.5)/(2*a)
        return x1, x2 
    if d == 0:
        x = -b / (2 * a)
        return (x, )
    return None


result = find_roots(3, -4, -3)

if not result:
    print('Нет корней')
elif len(result) == 2: 
    print(f'Корни = {result[0]}, {result[1]}')
else:
    print (f'Корень = {result[0]}')


# def SquareRoot():
#     a = 6
#     b = 20
#     c = 12
#     d = b*b-4*a*c
#     x1 = (-b + math.sqrt(d))/(2*a)
#     x2 = (-b - math.sqrt(d))/(2*a)
#     print(f'a: {a}, b: {b}, c: {c}')
#     print(f'd: {d}, x1: {x1}, x2: {x2}')

# SquareRoot()

# 2. Найдите корни квадратного уравнения Ax2 + Bx + C = 0

# D = B^2 - 4*A*C
# X = - D/ (2*A)
# x1= (-b + sqrt(D)) / (2 * a)
# x2= (-b - sqrt(D)) / (2 * a)