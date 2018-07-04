#1)
The above tuple is equivalent to struct_time structure. This structure has following attributes −

Index	Attributes	Values
0	tm_year	2008
1	tm_mon	1 to 12
2	tm_mday	1 to 31
3	tm_hour	0 to 23
4	tm_min	0 to 59
5	tm_sec	0 to 61 (60 or 61 are leap-seconds)
6	tm_wday	0 to 6 (0 is Monday)
7	tm_yday	1 to 366 (Julian day)
8	tm_isdst	-1, 0, 1, -1 means library determines DST
Getting current time
To translate a time instant from a seconds since the epoch floating-point value into a time-tuple, pass the floating-point value to a function (e.g., localtime) that returns a time-tuple with all nine items valid.
The time module
This module provides a number of functions to deal with dates and the time within a day. It’s a thin layer on top of the C runtime library.
A given date and time can either be represented as a floating point value (the number of seconds since a reference date, usually January 1st, 1970), or as a time tuple.
Getting the current time
Example: Using the time module to get the current time

#2)
import datetime
t=datetime.datetime.now()
print("Current date and time is:",t)
print(t.strftime("%Y-%m-%d %H:%M:%S"))

#2)
import datetime
d=datetime.date.today()
print(d.month)

#4)	
import datetime
a = '2010-01-31'
d = datetime.datetime.strptime(a, "%Y-%m-%d")
print(“The day is:”d.day)

#5)
import datetime
d=datetime.datetime(2009,10,5,18,00)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.second)

#6)
import time
print ("Time is",time.localtime())

#7)
import math
num=int(input("Enter the number"))
print ("The factorial of entered number is : ", end="")
print (math.factorial(num))

#8)
import math
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
print(math.gcd(num1,num2))

#9)
import os
print(os.getcwd())
import os
s=os.getenv('path')
print(s)

	
