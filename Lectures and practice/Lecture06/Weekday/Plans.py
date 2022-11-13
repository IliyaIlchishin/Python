import Today as td
import time


def plans(dayname):
        if dayname == "Today is the working day":
            print('_________________________________________________')
            time.sleep(1)
            print ('What you are going to do today after the work?')
            time.sleep(1)
            print ("1 - go home, 2 - go to a bar, 3 - I'll play PC ")
            time.sleep(1)
            print ('_________________________________________________')
            choice = input("Please enter only number ")
            if choice == 1:
               result = "Go home, buddy!"
               
            if choice == 2:
                result = "That's my boy" 
                
            if choice == 3:
                result = "Send me your nick in steam"  
                
            return result
        if dayname == "Today is the weekend":
            print ('_________________________________________________')
            print ('What are your choice for the weekend?')
            print ("1 - bar, 2 - footbal, 3 - racing")
            print ('_________________________________________________')
            choice = input("Please enter only number ")
            if choice == 1:
                result = "I know a good bar with good girls"
            if choice == 2:
                result = "We are the team!!!"
            if choice == 3:
                result = "NFS only in real life"
    

result = plans("Today is the working day")
print(result)