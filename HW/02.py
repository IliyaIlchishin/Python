

#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Примечание:
# Используйте знания об Алгебра Логике, вы должны перебрать все возможные комбинации значений X, Y, Z (принимают значения 0 или 1)
# ⋁ +  ⋀ *     ¬  not 

for x in range(2):
        for y in range(2):
            for z in range(2):
                print (x,y,z)
                a = (x+y+z)*-1
                print('a = ', a)
                b = (x*-1) * (y*-1) * (z*-1)
                print('b = ', b)
                
                if a==b:
                    print(' Утверждение верно')
                else:
                    print('Утверждение не верно')






