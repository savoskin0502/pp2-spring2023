import datetime


# date - year-month-day
# time - hours-seconds

date1 = datetime.datetime(year=2023, month=2, day=14)
date2 = datetime.datetime(year=2023, month=1, day=1)
print(date1, type(date1))
print(date1 > date2)
print(date2 - date1, type(date2 - date1))
day_delta = datetime.timedelta(days=1)

new_date = date1 + day_delta
print(new_date)  # strftime/strptime
print(new_date.strftime('%B %Y'))
date_string = '2023-02-01'
date_result = datetime.datetime.strptime(date_string, '%Y-%m-%d')
print(date_result, type(date_result))

print(datetime.datetime.now())
print(date2.isoweekday())
# datetime.datetime
# timedelta
