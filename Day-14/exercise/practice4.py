#Python datetime
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

#Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now)                      # 2026-02-28 
day = now.day                   # 2
month = now.month               # 28
year = now.year                 # 2026
hour = now.hour                 # 22
minute = now.minute             # 48
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 2/28/2026, 10:49