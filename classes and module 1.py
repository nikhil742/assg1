#1)
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print(3.14*self.radius*self.radius)
    def getcircumference(self):
        print(self.radius*2*3.14)
x=Circle(8)
print("The radius is",x.radius)
x.getArea()
x.getcircumference()

#2)
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print(self.name)
        print(self.roll_no)
x=Student('nikhil',22)
print(x.name)
print(x.roll_no)


#3)
class Temperature():
    def convertFahrenheit(self,celsius):
        return (celsius * (8 / 5)) + 32
    def convertCelsius(self,farenhiet):
        return(farenhiet - 32) * (5 / 8)
x=Temperature()
print(x.convertFahrenheit(5))
print(x.convertCelsius(5))

#4)
class Movie_detailes:
    def __init__(self,movie_name,artist_name,release_date,rating):
        self.movie_name=movie_name
        self.artist_name=artist_name
        self.release_date=release_date
        self.rating=rating
    def display(self):
        print("Movie name is", self.movie_name)
        print("Artist name is", self.artist_name)
        print("Release_date is", self.release_date)
        print("rating is",self.rating)
    def update(self,m,a,d):
        print("updated detailes of movie:-->")
        self.movie_name=m
        self.artist_name=a
        self.release_date=d
        print("Movie name is",self.movie_name)
        print("Artist name is", self.artist_name)
        print("Release_date is", self.release_date)
x=Movie_detailes('sanju','ranbir kapoor','29 july 2018',5)
print(x.display())
print(x.update('the forbidden kingdom','jackie chan','2 may 2008'))


#5)
class Expenditure:
    def __init__(self,expenditure,saving):
        self.expenditure=expenditure
        self.saving=saving
    def display(self):
        print(self.expenditure)
        print(self.saving)
    def total_salary(self):
        print("Total salary is",self.expenditure + self.saving)
x=Expenditure(55,56)
print(x.display())
print(x.total_salary())



