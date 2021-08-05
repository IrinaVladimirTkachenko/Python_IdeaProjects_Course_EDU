from datetime import timedelta, datetime

#year = timedelta(days=365)
#print(year)

#today = datetime.now()
#print('Today is', today)
#print('23 days from today will be', (today + timedelta(days=23)))
#print('93 days from today will be', (today + timedelta(days=93)))
#print('45 days from today will be', (today + timedelta(days=45)))
#print('230000 seconds from today will be', (today + timedelta(seconds=230000)))

today = datetime.now()
last_birthday = datetime(2020, 12, 11)
print('My last birhday was {0} days ago.'.format((today - last_birthday).days))

year = timedelta(days=365)
leap_year = timedelta(days=366)
print('There are {0} seconds in a year and {1} seconds in a leap year.'
      .format(year.total_seconds(), leap_year.total_seconds()))

print('There are {0} days in 7 years and {1} days in 7 leap years.'
      .format((year * 7).days, (leap_year * 7).days))



