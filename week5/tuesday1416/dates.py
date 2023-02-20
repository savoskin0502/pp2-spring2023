import datetime

# data - год-месяц-день
# time - seconds/mili/hours
date1 = datetime.datetime(year=2021, month=2, day=14)
date2 = datetime.datetime(year=2023, month=2, day=14)
print(
    date1 <= date2
)
print(
    date2 - date1, type(date2 - date1)  # datetime.timedelta()
)
timedelta1 = datetime.timedelta(days=1, hours=12)
print(date2 + timedelta1)
print(date1.isoweekday())
# strptime/strftime
date_string = "2023-02-01"
our_date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
print(our_date, type(our_date))
print(our_date.strftime('%B %Y'))

# print(d, type(d))
