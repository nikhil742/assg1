
#1)
year=int(input("Enter the year"))
if (year%4 == 0 and year%400 == 0 or year%100!= 0):
  	print("Entered year is a leap year")




#2)
print("Enter length")
length = input()
print("Enter breadth")
breadth = input()
if length == breadth:
  print("Yes, it is square")
else:
  print ("No, it's Rectangle")


#3)
print("Enter the first age")
first = input()
print("Enter second age")
second = input()
print("Enter third age")
third = input()

if first >= second and first >= third:
 	 print ("Oldest is",first)
elif second >= first and second >= third:
  	print ("Oldest is",second)
elif third >= first and third >= second:
  	print ("Oldest is",third)
else:
  	print ("All are equal")


#4)
points=int(input("enter the value of points"))
if(points<=50):
    print("Sorry! No prize this time.")
elif(points>50 and points<=150):
    print("Congratulations! You won a  football")
elif(points>150 and points<=180):
    print("Congratulations! You won a 1001 inventionsthat change the world Book")
elif(points>180 and points<=200):
    print("Congratulations! You won a  amazon vouchers ")


#5)
item=int(input("enter the no. of item"))
cost=item*100
if(cost>=1000):
    print("10% discount on item")
else:
    print("No discount on the item")
discount=cost-cost*.1
print(discount)

