from datetime import datetime

#today = datetime(2021, 7, 6)
#today_now = datetime.now()
#print(today)
#print(today_now)

#timestamp = datetime.timestamp(today)
#print(timestamp)
#timestamp_now = datetime.timestamp(today_now)
#print(timestamp_now)

#today = datetime(2021, 7, 6)
#print(today)
#timestamp = datetime.timestamp(today)
#print(timestamp)
#today_from_timestamp = datetime.fromtimestamp(timestamp)
#print(today_from_timestamp)
#today_format = today.strftime('%d %B %Y')
#print('Today is', today_format)
#print('Today is', today.strftime('%A'))

today = datetime.today()
print(today)
utc_today = today.utcnow()
print(utc_today)
print(today.date())
print(today.time())
print(today.isocalendar())
print(today.isoformat())