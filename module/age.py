import datetime
DOB = input("Enter your bitrhdate in format yyyy-mm-dd =")
year,month,day=map(int,DOB.split( - ))
date=datetime.date(year,month,day)
datetime.date.today()-date
age=(datetime.date.today()-datetime.date).days//365
print("your age is =" , age)