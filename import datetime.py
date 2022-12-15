import datetime
year=int(input("Enter your  year:"))
month=int(input("Enter your  month:"))
day=int(input("Enter your date:"))
my_date=datetime.date(year,month,day)
print(my_date)
print(type(my_date))
