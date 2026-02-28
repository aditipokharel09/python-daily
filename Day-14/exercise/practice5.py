#Formatting Date Output Using strftime

from datetime import datetime
new_year = datetime(2026, 2, 28)
print(new_year)      # 2026-02-28 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) 
print(f'{day}/{month}/{year}, {hour}:{minute}')  
