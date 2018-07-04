#1)
f=open('xyz.txt','r',encoding='utf8')
d=f.readlines()
print("last line is-->",d[-1])

#2)
with open("xyz.txt",'r',encoding='utf8') as t:
    d=t.read().split()
    print(len(d))

#3)
with open("xyz.txt",encoding='utf8') as f:
    with open("out.txt", "w",encoding='utf8') as f1:
        for line in f:
            f1.write(line)
#4)
with open('xyz.txt',encoding='utf8') as fh1, open('out.txt',encoding='utf8') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)

#5)
import random
f=open('Random.txt','w')
for i in range(10):
    data=str(random.randint(1,10))
    f.write(data)
    f.write("\n")
f.close()
print("\nReading the file now")
file1 = open("Random.txt",'r')
file2 = open("sorted.txt",'w')
list1=file1.readlines()
list1.sort()
file2.writelines(list1)
file1.close()
file2.close()

