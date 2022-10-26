
import time
def get_rand(x, y):
    scope = y-x
    print (time.time ())
    result = int (time.time ()*1000) % scope 
    return result

print (get_rand (80, 100)) 
print (get_rand (20, 30))
print (get_rand (50, 100))