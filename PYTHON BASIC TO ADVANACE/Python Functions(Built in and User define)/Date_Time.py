from datetime import date, datetime, time, timedelta 
import calendar

print("======== DATE ========")

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
day = int(input("Enter Day: "))

# Create Date

d = date(year, month, day)

print("Date: ", d)
print("Year: ", d.year)
print("Month: ", d.month)
print("Day: ", d.day)

print("Today's Date :", date.today())

print("Weekday (Monday=0): ", d.weekday())

print("ISO Weekday (Monday=1): ", d.isoformat())

new_year = int(input("Enter New Year: "))

print("\n========= NEW YEAR =========")

print("Replace Year: ", d.replace(year=new_year))

print("ISO Format: ", d.isoformat())

print("\n========= DATETIME =========")

hour = int(input("Enter Hour: "))

minute = int(input("Enter Minute: "))

second = int(input("Enter Second: "))

dt = datetime(year, month, day, hour, minute, second)

print("datetime : ", dt)

print("Year : ", dt.year)
print("Month : ", dt.month)
print("Day : ", dt.day)
print("Hour : ", dt.hour)
print("Minute : ", dt.minute)
print("Second : ", dt.second)
print("Microsecond : ", dt.microsecond)

print("Only Date: ", dt.date())
print("Only Time: ", dt.time())

print("Timestamp: ", dt.timestamp())

new_month = int(input("Enter New Month: "))
print("Replace Month: ", dt.replace(month=new_month))

print("DD/MM/YYYY: ", dt.strftime("%D/%M/%Y"))
print("Day Name: ", dt.strftime("%A"))
print("Month Name: ", dt.strftime("%B"))
print("Time: ", dt.strftime("%I:%M:%S %p"))

print("\n========= STRING TO DATETIME =========")

s = input("Enter Date (DD-MM-YYYY): ")
new_date = datetime.strptime(s, "%d-%m-%Y")

print("Converted Date: ", new_date)

print("\n========= TIME =========")

t = time(hour, minute, second)

print("Time: ", t)
print("Hour: ", t.hour)
print("Minute: ", t.minute)
print("Second: ", t.second)

print("\n========= TIMEDELTA =========")

today = datetime.now()

days = int(input("Enter Days to Add: "))
print("After Days: ", today + timedelta(days=days))

days = int(input("Enter Days to Subtract: "))
print("Before Days: ", today - timedelta(days=days))

weeks = int(input("Enter Weeks to Add: "))
print("After Weeks: ", today + timedelta(weeks=weeks))

hours = int(input("Enter Hours to Add: "))
print("After Hours: ", today + timedelta(hours=hours))

minutes = int(input("Enter Minutes to Add: "))
print("After Minutes: ", today + timedelta(minutes=minutes))

seconds = int(input("Enter Seconds to Add: "))
print("After Seconds: ", today + timedelta(seconds=seconds))


print("\n========= CALENDAR =========")

# print(calendar.month(year, month))

# print("Leap Year: ", calendar.isleap(year))

# print("Weekday: ", calendar.weekday(year, month, day))


cal_year = int(input("Enter Calendar Year: "))
cal_month = int(input("Enter Calendar Month (1-12): "))

print("\nCalendar\n")
print(calendar.month(cal_year, cal_month))

print("Leap Year:", calendar.isleap(cal_year))

day = int(input("Enter Day to Check Weekday: "))

print("Weekday Number:", calendar.weekday(cal_year, cal_month, day))

