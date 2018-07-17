from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,width = 160,height=50)
Tops.pack(side=TOP)

root1 = Frame(root,width = 900,height=700)
root1.pack(side=LEFT)

root2 = Frame(root ,width = 400,height=700)
root2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))




lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="restaurant Management system",fg="blue",bd=5)
lblinfo.grid(row=0,column=0)

lblinfo = Label(Tops, font=( 'aria' ,20,'bold' ),text=localtime,fg="black")
lblinfo.grid(row=1,column=0)


text_Input=StringVar()
operator =""

txtdisplay = Entry(root2,font=('ariel' ,20), textvariable=text_Input , bd=3
                   ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)


def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


btn0=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="0",bg="grey", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btn1=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="1",bg="grey", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="2",bg="grey", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="3",bg="grey", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

btn4=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="4",bg="grey", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="5",bg="grey", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="6",bg="grey", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

btn7=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="7",bg="grey", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="8",bg="grey", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="9",bg="grey", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)




multiply=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="*",bg="grey", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)

btnc=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="clear",bg="grey", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="=",bg="grey",command=eqals)
btnequal.grid(row=5,column=2)

Addition=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="+",bg="grey", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)

Division=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="/",bg="grey", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)

Substraction=Button(root2,height=2,width=7,bd=4, fg="white", font=(15),text="-",bg="grey", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)




rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(root1, font=( 'aria' ,14, 'bold' ),text="Order No",fg="green")
lblreference.grid(row=0,column=0)
txtreference = Entry(root1,font=('ariel' ,14,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="white")
txtreference.grid(row=0,column=1)

lblfries = Label(root1, font=( 'aria' ,14, 'bold' ),text="Fries Meal",fg="green")
lblfries.grid(row=1,column=0)
txtfries = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Fries ,insertwidth=4,bd=6,bg="white")
txtfries.grid(row=1,column=1)

lblLargefries = Label(root1, font=( 'aria' ,14, 'bold' ),text="Lunch Meal",fg="green")
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="white")
txtLargefries.grid(row=2,column=1)


lblburger = Label(root1, font=( 'aria' ,14, 'bold' ),text="Burger Meal",fg="green")
lblburger.grid(row=3,column=0)
txtburger = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="white")
txtburger.grid(row=3,column=1)

lblFilet = Label(root1, font=( 'aria' ,14, 'bold' ),text="Pizza Meal",fg="green")
lblFilet.grid(row=4,column=0)
txtFilet = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="white")
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(root1, font=( 'aria' ,14, 'bold' ),text="Cheese burger",fg="green",bd=10)
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="white")
txtCheese_burger.grid(row=5,column=1)


lblDrinks = Label(root1, font=( 'aria' ,14, 'bold' ),text="Drinks",fg="green",bd=10)
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="white")
txtDrinks.grid(row=0,column=3)

lblcost = Label(root1, font=( 'aria' ,14, 'bold' ),text="cost",fg="green",bd=10,anchor='center')
lblcost.grid(row=1,column=2)
txtcost = Entry(root1,font=('ariel' ,14,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white")
txtcost.grid(row=1,column=3)

lblService_Charge = Label(root1, font=( 'aria' ,14, 'bold' ),text="Service Charge",fg="green",bd=10)
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white")
txtService_Charge.grid(row=2,column=3)

lblTax = Label(root1, font=( 'aria' ,14, 'bold' ),text="Tax",fg="green",bd=10,anchor='center')
lblTax.grid(row=3,column=2)
txtTax = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white")
txtTax.grid(row=3,column=3)

lblSubtotal = Label(root1, font=( 'aria' ,14, 'bold' ),text="Subtotal",fg="green",bd=10)
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white")
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(root1, font=( 'aria' ,14, 'bold' ),text="Total",fg="green",bd=10)
lblTotal.grid(row=5,column=2)
txtTotal = Entry(root1,font=('ariel' ,14,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="white")
txtTotal.grid(row=5,column=3)


lblTotal = Label(root1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(root1,padx=16,pady=8, bd=7 ,fg="white",font=('ariel' ,14,'bold'),width=10, text="TOTAL", bg="grey",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(root1,padx=16,pady=8, bd=7 ,fg="white",font=('ariel' ,14,'bold'),width=10, text="RESET", bg="grey",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(root1,padx=16,pady=8, bd=7 ,fg="white",font=('ariel' ,14,'bold'),width=10, text="EXIT", bg="grey",command=qexit)
btnexit.grid(row=7, column=3)



def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="black", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=(15), text="Fries Meal", fg="red", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=(15), text="25", fg="green", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=(15), text="Lunch Meal", fg="red", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=(15), text="40", fg="green", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=(15), text="Burger Meal", fg="red", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=(15), text="35", fg="green", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=(15), text="Pizza Meal", fg="red", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=(15), text="50", fg="green", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=(15), text="Cheese Burger", fg="red", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=(15), text="30", fg="green", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=(15), text="Drinks", fg="red", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=(15), text="35", fg="green", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(root1,padx=16,pady=8, bd=7 ,fg="white",font=('ariel' ,14,'bold'),width=10, text="PRICE", bg="grey",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()

