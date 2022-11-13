import Today as td
import DayInput as DI
import Plans as pl

def start():
    day = DI.weekday()
    TheDay = td.today(day)
    print(TheDay)

    plan = pl.plans(TheDay)
    print(plan)