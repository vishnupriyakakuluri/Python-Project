# import calendar
# a=calendar.HTMLCalendar(calendar.SUNDAY)
# b=a.formatmonth(2019,1)
# print(b)
#
# -------------------------------------------------------
# import calendar
# a=calendar.TextCalendar(calendar.SUNDAY)
# b=a.formatmonth(2025,1)
# print(b)
# # -----------------------------------------------------
# import calendar
# #a=calendar.TextCalendar(calendar.SUNDAY)
# for i in calendar.month_name:
#     print(i)
# ------------------------------------------------
# import calendar
# #a=calendar.TextCalendar(calendar.SUNDAY)
# for i in range(1,12):
#     a=calendar.monthcalendar(2019,i)
#     week1=a[0]
#     week2=a[1]
#     if week1[calendar.FRIDAY] !=0:
#         temple=week1[calendar.FRIDAY]
#     else:
#         temple=week2[calendar.FRIDAY]
#
#     print(calendar.month_name[i],temple)


from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
import time
import datetime
# print(datetime.datetime.today())
# #from how long I'm using PyCharm in secs
# print(time.time())
# print(time.localtime())
# print(date.today())
# #print(datetime.now())'''
# i=date.today()
# print("today'd date is:", i.day,'/',i.month, i.year,i.weekday())
# i=datetime.datetime.now()
# print(i.strftime("%a, %d, %b, %y"))
# print(i.strftime("%A, %d, %B, %Y"))
# print(i.strftime('%c'))
# print(i.strftime('%x'))
# print(i.strftime('%X'))
# i=datetime.datetime.now()
# print('today:',i)
# print(timedelta(days=365,hours=8,minutes=45))
# print('one year from now:'+str(datetime.datetime.now()+timedelta(days=455,hours=3)))
# ----------------------------------------------------------------------------
# import calendar
# '''a=calendar.TextCalendar(calendar.MONDAY)
# b=a.formatmonth(2019,1)
# print(b)
# year=2020
# print(calendar.calendar(1989))'''
# for i in calendar.month_name: print(i)
# a=calendar.TextCalendar(calendar.MONDAY)
#
# for i in a.itermonthdays(2012,2): print(i)
# a=calendar.HTMLCalendar(calendar.MONDAY)
# b=a.formatmonth(2019,1)
# print(b)

#=====================================================
# import calendar
# a=calendar.calendar(2025)
# # a=calendar.TextCalendar(calendar.SUNDAY)
# for i in range(1,13):
#     b=a.formatmonth(2025,i)
#     for j in b:
#         if b.weekday()==0:
#             print("salary is credited")
#         else:
#             pass
#============================================================================
# import calendar
# def first_monday(year, month):
#     first_day_weekday, num_days_in_month = calendar.monthrange(year, month)
#     if first_day_weekday == calendar.MONDAY:
#         return 1
#     else:
#         offset = (calendar.MONDAY - first_day_weekday + 7) % 7
#         return 1 + offset
# year = 2025
# for month in range(1, 13):
#     first_monday_date = first_monday(year, month)
#     print(f"First Monday of {calendar.month_name[month]} {year} is: {first_monday_date}")

#=============================================================================
# import calendar
# # Loop through each month in 2025
# for month in range(1, 13):
#     # Find the first Monday of the month
#     first_day_weekday, _ = calendar.monthrange(2025, month)
#     first_monday = 1 + (calendar.MONDAY - first_day_weekday + 7) % 7
#
#     # Print the result
#     print(f"First Monday of {calendar.month_name[month]} 2025 is: {first_monday}")
#===========================================================================
# import calendar
# #a=calendar.TextCalendar(calendar.SUNDAY)
# for i in range(1,13):
#     a=calendar.monthcalendar(2019,i)
#     week1=a[0]
#     week2=a[1]
#     if week1[calendar.MONDAY] !=0:
#         temple=week1[calendar.MONDAY]
#     else:
#         temple=week2[calendar.MONDAY]
#
#     print(calendar.month_name[i],temple)

#==================================================================





