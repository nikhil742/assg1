#1
radius=float(input("Enter the radius of circle"))
def area(radius):
  area_circle=3.14*radius*radius
  return area_circle
final_area=area(radius)
print("The area of the circle with the inserted radius is",final_area)

#2
#creating a method to determine whether a number is perfect or not
def perfect(n):
  sum = 0
  for i in range(1,n):
    if n%i == 0:
      sum = sum + i
  if sum == n:
    return True
  else:
    return False
#Calling method in for loop
for i in range(1,1001):
  if perfect(i):
    print (i)


#ques3-->
def times_tables(n, t=1):
    if t == 13:
        return
    print(str(n) + " x " + str(t) + " = " + str(n*t))
    times_tables(n, t+1)
times_tables(int(input("Enter number: ")))

#ques4-->
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))

#ques5-->
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
dict={n:factorial(n)}
print(dict)
