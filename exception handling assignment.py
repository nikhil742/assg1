
#1)
    
try:
    a=3
    if (a<4):
    a = a / (a-3)
    print(a)

except:
    ZeroDivisionError as e:
    print("there is an error")
    print(e)


#2)
try:
    l=[1,2,3]
    print(l[3])
except Exception as e:
    print("Error is identify")
    print(e)

#3)
print('an exception\nNameError')

#4)
print('The output is-->-5 \na/b result in zero')

#5)

try:
    from tweepy import *
except  Exception as e:
    print('The import error')
    print(e)

x='xyz'
try:
    int(x)
except Exception as e:
    print("Value error occur")
    print(e)

try:
    l=[1,2,3]
    print(l[3])
except Exception as e:
    print("Error is identify")
    print(e)

#6)
class under_age(Exception):
    def __init__(self,age):
        self.age = age
        print('you are %d years old, please enter age above 18 to proceed'%(self.age))
def enter_age():
    try :
        x = int(input('enter your age :'))
        if x<18 :
            raise under_age(x)
        print('now you can apply for the visa...!! as you are above 18')
    except under_age as e :
        print('this is an under age error.')
        enter_age()
enter_age()


