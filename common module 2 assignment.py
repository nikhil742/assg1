#1)
class Animal():
    animal=5
    def animal_attribute(self):
        print(self.animal)
class Tiger(Animal):
    def tiger_attribute(self):
        print("The tigger attributes")
x=Tiger()
x.animal_attribute()

#2)
class A():
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())


#3)
class Cop():
    def __init__(self,name,age,work,experience,designation):
        self.name=name
        self.age=age
        self.work=work
        self.experience=experience
        self.designation=designation
    def display(self):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)
    def add(self):
        print("Add the following details",self.name)
    def update(self,n,a,w,e,d):
        self.name=n
        self.age=a
        self.work=w
        self.experience=e
        self.designation=d
        print("The Updated details are:")
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)
    def updated_details(self):
        return (self.name,self.age,self.work,self.experience,self.designation)
x=Cop('nikhil',22,'Ceo','2yrs','ABC')
x.display()
x.update('neha',23,'Manager','5yrs','CDF')
x.updated_details()
class Mission(Cop):
   def add_mission(self):
        print("The mission is alloted to:",self.updated_details())
prbhakr=Mission('neha',23,'Manager','5yrs','CDF')
prbhakr.add_mission()


#4)
class Shape():
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def method_area(self,len,bre):
       print("Area is:",self.len*self.bre)
class Rectangle(Shape):
    print("Area of Reactangle")
x=Rectangle(3,4)
x.method_area(3,4)
class Square(Shape):
    print("Area of Square")
y=Square(5,6)
y.method_area(5,6)

