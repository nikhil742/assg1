##1)
import pandas as pd
import numpy as np
df = pd.DataFrame({
        'name':['nikhil','rohit','ashutosh'],
        'age':['18','18','17'],
        'mail id':['nikhilsh7421@gmail.com','rohit@gmail.com','ashutosh@gmail.com'],
        'phone no':[9811407145,9879365283,9811408165]
})


print(df)


##in dictonary)
context = {
        'name':['nikhil','rohit','ashutosh'],
        'age':['18','18','17'],
        'mail id':['nikhilsh7421@gmail.com','rohit@gmail.com','ashutosh@gmail.com'],
        'phone no':[9811407145,9879365283,9811408165]
}

pf = pd.DataFrame(context)
print(pf)

##)

context1 = {
        'name':pd.Series(['nikhil','rohit','ashutosh']),
        'age':pd.Series(['18','18','17']),
        'mail id':pd.Series(['nikhilsh7421@gmail.com','rohit@gmail.com','ashutosh@gmail.com']),
        'phone no':pd.Series([9811407145,9879365283,9811408165])
}

gf = pd.DataFrame(context1)
print(gf)


##2)


import csv
import pandas as pd
a=pd.read_csv('weather.csv')
print(a)

#1)
print("First 5 rows",a.head(5))

#2)
print("First 10 rows",a.head(10))

#3)
df=pd.DataFrame(a)
print(df.describe(include='all'))

#4)
print("last 5 rows",a.tail(5))

#5)
b=df.loc[0]
print("Extract 2 column",b)
df=pd.DataFrame(b)
print(df.describe(include='all'))

