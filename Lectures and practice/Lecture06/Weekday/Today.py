import DayInput as day

def today(day):
    dayName = ''
    if day <= 5:
        dayName = "Today is the working day"
    if day >5 and day < 8:
        dayName = "Today is the weekend"
    if day == 0 or day < 0:
        print('Please enter the correct day')
    if day >7:
        print('Please enter the correct day')  
    return dayName
