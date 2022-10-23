
def Input_Coordinates():
    x, y = input('Please enter coordinates x , y: ') .split(",")
    a = []
    while int(x) == 0 or int(y) == 0:
        print("Coordinates can't be equal 0. Please enter again")
        x, y = input('Please enter coordinates x , y: ') .split(",")
    else:
        a.append(int(x))
        a.append(int(y))
        return a

def DistanceBTWCoordinates (a,b):
    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return int(length)

a = Input_Coordinates()
b = Input_Coordinates()
length = DistanceBTWCoordinates(a,b)

print(length)

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,10
# - A (7,-5); B (1,-1) -> 7,2
