import datetime
import pytz

iso_format_string = '%Y-%m-%dT%H%:%M:%S%z'

#now_utc = datetime.datetime.now(pytz.timezone('UTC'))
#print(now_utc.strftime(iso_format_string))

#now_eu_kiev = now_utc.astimezone(pytz.timezone('Europe/Kiev'))
#print(now_eu_kiev.strftime(iso_format_string))

#now_eu_istanbil = now_utc.astimezone(pytz.timezone(('Europe/Istanbul')))
#print(now_eu_istanbil.strftime(iso_format_string))

naive_now = datetime.datetime.now()
print(naive_now)
kiev_timezone = pytz.timezone('Europe/Kiev')
local_datetime = kiev_timezone.localize(naive_now)
print(local_datetime)

#all_timezones = pytz.all_timezones
#for timezone in all_timezones:
 #   print(timezone)