import os
import datetime

# FIRST TASK
print(os.getcwd(),)
print(os.listdir())



# SECOND TASK

entered_date = str(input('Enter the date(for example: 09.02.2019):')).replace('.', ' ')
day, month, year = entered_date.split(' ')
day_name = datetime.date(int(year), int(month), int(day))
week_number = day_name.isocalendar()[1]
print("Name of this day -", day_name.strftime("%A"), '; Week number of this date -', week_number)








