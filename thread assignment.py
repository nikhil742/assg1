#1)
import threading
import time
from threading import Thread
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        time.sleep(5)
        print("kya seen", self.h)

thread1 = mythread('hay')
thread1.start()

#2)
import time
import threading
class number(threading.Thread):
    def __init__(self,delay):
        threading.Thread.__init__(self)
        self.delay=delay
    def show(self):
        time.sleep(self.delay)
    def run(self):
        for i in range(1,11):
            print(i)
            self.show()
n=number(1)
n.start()
n.join()
print("The process is ended")

#3)
import time
import threading
class thread(threading.Thread):
    def __init__(self,delay):
        threading.Thread.__init__(self)
        self.delay=delay
    def show(self):
        start=time.time()
        delay=2*self.delay
        time.sleep(delay)
        self.delay=self.delay+1
        end=time.time()
        print("Time delay between two element are",int(end-start,))
    def list(self):
        list=['1','2','3','4','5','6','7','8','9']
        for i in list:
            thread.show(self)
            print(i)
    def run(self):
        self.list()
th=thread(1)
th.start()
th.join()
print("The process is ended")


#4)
import time
import threading
from math import factorial
class fact(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num
    def factorial(self):
        return(factorial(num))
    def show(self):
        print(self.factorial)
    def run(self):
        self.factorial(self)
num=int(input("Enter the number"))
x=fact('num')
x.factorial()
print("the factorial of number is",x.factorial())

