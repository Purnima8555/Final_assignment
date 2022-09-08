#range(s,s,s) --> start ,stop, step
from signal import default_int_handler


for i in range(0,10,1):
    print(f"The value of i is: {i}")  


days_list = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

for day in days_list:
    print(f"The single day is: {day}")

    