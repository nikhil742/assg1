#1
x=('nikhil','rohit','vivek','neha')
print(" there are the following tuple ",x)
print("length of the tuple is",len(x))


#2) to fing the largest and smallest elements of the tupple
y=(58,64,886,998,170,162)
#Finding the element
print(" maximum element ",max(y))
print("minimum element ",min(y))


#3
z=(1,2,3,4,5,6)
pro=(1*2*3*4*5*6)
print(" product ",pro)



#SETS:)


#1)DIFFERENCE OF TWO SETS
a={"jan","feb","march","april"}
b={"jan","may","june","july"}
c=a.difference(b)
print(c)
#COMPARING TWO SETS

a={"jan","feb","march","april"}
b={"jan","may","june","july"}
#DISPLAYING SETS
print("The first set is",a)
print("The second set is",b)

#DISPLAYNG  TWO SETS
t_set=a<=b
print("the comparison of two sets is",t_set)
f=a.intersection(b)
print(f)

#INTERSECTION OF TWO SETS
s=a.intersection(b)
print(s)


#DICTIONARIES:)


#1)

dict={'Name':'nikhil','Age':'18','Class':'13'}
print(dict['Name'])
print(dict['Class'])

#2
mydict = {'rohit':40,'anmol':2,'priyanka':1,'pandey':3}

for key in sorted (mydict.keys()):
 print("%s: %s" % (key, mydict[key]))

#3
s='MISSISSIPPI'
#converting string to lists
l=list(s)
m=l.count('M')
i=l.count('I')
s=l.count('S')
p=l.count('P')
#creating final dictionary
dict={'M':m,'I':i,'S':s,'P':p}
print("dictionary ",dict)





