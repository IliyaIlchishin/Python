
def Input_Coordinates():
    x, y = input('Please enter coordinates x , y: ') .split(",")
    while int(x) == 0 or int(y) == 0:
        print("Coordinates can't be equal 0. Please enter again")
        x, y = input('Please enter coordinates x , y: ') .split(",")
    else:
      return int (x), int(y)

def CheckCoordinates (x,y):
    if x > 0 and y > 0:
     print('Quarter 1')
    elif x < 0 and y > 0:
      print('Quarter 2')
    elif x < 0 and y < 0:
     print('Quarter 3')
    elif x > 0 and y < 0:
      print('Quarter 4')


x, y = Input_Coordinates()
print('Coordinate x:', x, 'and coordinate y:',y)
CheckCoordinates(x,y)

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


