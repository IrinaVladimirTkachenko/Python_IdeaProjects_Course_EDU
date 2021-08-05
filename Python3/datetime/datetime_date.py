from datetime import date

#today = date.today()
#print(today)
#print(today.year)
#print(today.month)
#print(today.day)

#date_1 = date(2021, 7, 4)
#date_2 = date(2020, 7,4)
#diff = date_1 - date_2
#print(diff)
#print(type(date_1))
#print(type(date_2))
#print(type(diff))

#today = date.today()
#print(today)

#my_birthday = date(today.year, 12, 11)
#if my_birthday < today:
 #   my_birthday = my_birthday.replace(year=today.year + 1)
#print(my_birthday)
#days_until_birthday = my_birthday - today
#print('You will celebrate your birthday in', days_until_birthday.days, 'days!')

#today = date.today()

#week_day = today.weekday()
#week_day = today.isoweekday()
#print(week_day)

year = input('Please enter a year ')
month = input('Please enter a month ')
day = input('Please enter a day ')

date_1 = date(int(year), int(month), int(day))
# print(date_1)
week_day = date_1.weekday()

if week_day == 0:
    print(date_1, 'is a Monday.')
elif week_day == 1:
    print(date_1, 'is a Tuesday.')
elif week_day == 2:
    print(date_1, 'is a Wednesday.')
elif week_day == 3:
    print(date_1, 'is a Thursday.')
elif week_day == 4:
    print(date_1, 'is a Friday.')
elif week_day == 5:
    print(date_1, 'is a Saturday.')
elif week_day == 6:
    print(date_1, 'is a Sunday.')


