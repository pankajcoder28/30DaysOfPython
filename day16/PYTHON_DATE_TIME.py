'''1. Get the current day, month, year, hour, minute and timestamp from datetime
module'''
from datetime import datetime
current = datetime.now()
print(current)
day = current.day
print(day)
month = current.month
print(month)
year = current.year
print(year)
hour = current.hour
print(hour)
minute = current.minute
print(minute)
ts = current.timestamp()
print(ts)

'''2.Format the current date using this format: "%m/%d/%Y, %H:%M:%S")'''
ftime = current.strftime('%m/%d/%y, %H:%M:%S')
print(ftime)

#3. Today is 5 December, 2019. Change this time string to time.
time_string = '5 December, 2019'
time_obj = current.strptime(time_string, '%d %B, %Y')
print(time_obj)

#4. Calculate the time difference between now and new year.
now = current.now()
new_year = datetime( year = 2026, month= 12 ,day = 31)

diff = new_year - now
print(diff)

#5. Calculate the time difference between 1 January 1970 and now.
now = current.now()
w = '1 January 1970'
date = current.strptime(w, '%d %B %Y') 

diff = now - date
print(diff)
#6
from datetime import datetime

activity = "User logged in"

now = datetime.now()

timestamp = now.timestamp()

print(f"📝 Activity: {activity}")
print(f"📅 Date & Time: {now.strftime('%d/%m/%Y, %H:%M:%S')}")
print(f"⏱️ Timestamp: {timestamp}")


