#calculator
from tkinter import *
expression = ""

def equal():
    try:

        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
 
    except:
 
        equation.set(" error ")
        expression = ""

def number(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 


def clear():
    global expression
    expression = ""
    equation.set("")
 
 
if __name__ == "__main__":
    
    root = Tk()
    root.configure(background="white")
    root.title("Calculator")
    root.geometry("305x180")
    
    equation = StringVar()
       
   
    expression_field = Entry(root, text=equation)
 
    
    expression_field.grid(columnspan=4, ipadx=70)
 
    equation.set('0')
     

    
    button1 = Button(root, text=' 1 ', fg='white', bg='grey',
                     command=lambda: number(1), height=1, width=6, font = (15))
    button1.grid(row=4, column=0)
 
    button2 = Button(root, text=' 2 ', fg='white', bg='grey',
                     command=lambda: number(2), height=1, width=6, font = (15))
    button2.grid(row=4, column=1)
 
    button3 = Button(root, text=' 3 ', fg='white', bg='grey',
                     command=lambda: number(3), height=1, width=6, font = (15))
    button3.grid(row=4, column=2)
 
    button4 = Button(root, text=' 4 ', fg='white', bg='grey',
                     command=lambda: number(4), height=1, width=6, font = (15))
    button4.grid(row=3, column=0)
 
    button5 = Button(root, text=' 5 ', fg='white', bg='grey',
                     command=lambda: number(5), height=1, width=6, font = (15))
    button5.grid(row=3, column=1)
 
    button6 = Button(root, text=' 6 ', fg='white', bg='grey',
                     command=lambda: number(6), height=1, width=6, font = (15))
    button6.grid(row=3, column=2)
 
    button7 = Button(root, text=' 7 ', fg='white', bg='grey',
                     command=lambda: number(7), height=1, width=6, font = (15))
    button7.grid(row=2, column=0)
 
    button8 = Button(root, text=' 8 ', fg='white', bg='grey',
                     command=lambda: number(8), height=1, width=6, font = (15))
    button8.grid(row=2, column=1)
 
    button9 = Button(root, text=' 9 ', fg='white', bg='grey',
                     command=lambda: number(9), height=1, width=6, font = (15))
    button9.grid(row=2, column=2)
 
    button0 = Button(root, text=' 0 ', fg='white', bg='grey',
                     command=lambda: number(0), height=1, width=6, font = (15))
    button0.grid(row=5, column=0)
 
    plus = Button(root, text=' + ', fg='white', bg='grey',
                   command=lambda: number("+"), height=1, width=6,  font =(15))
    plus.grid(row=2, column=3)
 
    minus = Button(root, text=' - ', fg='white', bg='grey',
                   command=lambda: number("-"), height=1, width=6, font = (15))
    minus.grid(row=3, column=3)
 
    multiply = Button(root, text=' * ', fg='white', bg='grey',
                   command=lambda: number("*"), height=1, width=6, font = (15))
    multiply.grid(row=4, column=3)
 
    divide = Button(root, text=' / ', fg='white', bg='grey',
                    command=lambda: number("/"), height=1, width=6, font = (15))
    divide.grid(row=5, column=3)
 
    equal = Button(root, text=' = ', fg='white', bg='grey',
                   command=equal, height=1, width=6, font = (15))
    equal.grid(row=5, column=2)
 
    clear = Button(root, text='Clear', fg='white', bg='grey',
                   command=clear, height=1, width=6, font = (15))
    clear.grid(row=5, column='1')
 
    
    root.mainloop()

