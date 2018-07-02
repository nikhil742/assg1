
#1)
list_1=[]
for i in range(0,10):
    y=int(input("enter the number"))
    list_1.append(y)
print(list_1)          

#2) infinite loop
for i in range(0,100):
i=0
while(i<100):
    print(i)
#3)
list1=[]
for i in range(0,4):
    l=int(input("enter the number"))
    list1.append(l)
print(list1)       
list2=[]
for l in list1:
    sq=l*l
    list2.append(sq)
print(list2)
          
          
#4)
y=[1,2,3,1.2,3.2,'nikhil']
i=[]
f=[]
s=[]
for a in y:
   if (type(a)==int):
       i.append(a)
   elif (type(a)==float):
       f.append(a)
   elif (type(a)==str):
       s.append(a)
   else:
        print("not defined")
       

print(i)
print(f)   
print(s)      

#5)
even=[]
odd=[]
for i in range(1,101):
    if(i%2 == 0):
        even.append(i)
    else:
        odd.append(i)
        
print(even)
print(odd)



#6
# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = 4
pypart(n)

#7)
x={'1':"one",'2':"two"}
for key in x.keys():
    print(key,x[key])

#8)
x=[0,1,2,3,4,5,6,7,8,9]
y=int(input("enter the required no."))
for i in x:
    if(i==y):
        x.pop(i)
    else:
        continue
print(x)

