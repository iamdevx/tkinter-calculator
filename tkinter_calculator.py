import tkinter as tk

window=tk.Tk()
window.geometry('400x400')
window.title("Calculator")


# ENTRY BOX
e=tk.Entry(window, width=46, borderwidth=5)
e.grid(row=0, column=0, columnspan=5)


# BUTTON
def click(num):
    result=e.get()
    e.delete(0, tk.END)
    e.insert(0, str(result) + str(num))

b1=tk.Button(window, text='1', width=8, command= lambda: click(1))
b1.grid(row=4, column=0, pady=5)

b2=tk.Button(window, text='2', width=8, command= lambda: click(2))
b2.grid(row=4, column=1, pady=5)

b3=tk.Button(window, text='3', width=8, command= lambda: click(3))
b3.grid(row=4, column=2, pady=5)

b4=tk.Button(window, text='4', width=8, command= lambda: click(4))
b4.grid(row=3, column=0, pady=5)

b5=tk.Button(window, text='5', width=8, command= lambda: click(5))
b5.grid(row=3, column=1, pady=5)

b6=tk.Button(window, text='6', width=8, command= lambda: click(6))
b6.grid(row=3, column=2, pady=5)

b7=tk.Button(window, text='7', width=8, command= lambda: click(7))
b7.grid(row=2, column=0, pady=5)

b8=tk.Button(window, text='8', width=8, command= lambda: click(8))
b8.grid(row=2, column=1, pady=5)

b9=tk.Button(window, text='9', width=8, command= lambda: click(9))
b9.grid(row=2, column=2, pady=5)

b11=tk.Button(window, text='0', width=8, command= lambda: click(0))
b11.grid(row=5, column=2, pady=5)


# OPERATIONS
def add():
    n1=e.get()
    global operation
    global first_num
    operation= "addition"
    first_num=float(n1)
    e.delete(0, tk.END)

b14=tk.Button(window, text='+', width=8, command=add)
b14.grid(row=4, column=3, pady=5)

def sub():
    n1=e.get()
    global operation
    operation= "subtraction"
    global first_num
    first_num=float(n1)
    e.delete(0, tk.END)

b13=tk.Button(window, text='-', width=8, command=sub)
b13.grid(row=3, column=3, pady=5)

def mul():
    n1=e.get()
    global operation
    operation= "multiplication"
    global first_num
    first_num=float(n1)
    e.delete(0, tk.END)

b12=tk.Button(window, text='*', width=8, command=mul)
b12.grid(row=2, column=3, pady=5)

def mod():
    n1=e.get()
    global operation
    operation= "modulation"
    global first_num
    first_num=float(n1)
    e.delete(0, tk.END)

b18=tk.Button(window, text='%', width=8, command=mod)
b18.grid(row=1, column=2, pady=5)

def div():
    n1=e.get()
    global operation
    operation= "division"
    global first_num
    first_num=float(n1)
    e.delete(0, tk.END)

b19=tk.Button(window, text='/', width=8, command=div)
b19.grid(row=1, column=3, pady=5)

def plus_minus():
    n1=e.get()
    global operation
    operation= "plusminus"
    global first_num
    first_num=float(n1)
    e.delete(0, tk.END)
    e.insert(0, -first_num)

b10=tk.Button(window, text='+/-', width=8, command=plus_minus)
b10.grid(row=5, column=1, pady=5)


# EQUAL
def equal():
    n2=e.get()
    second_num=float(n2)
    e.delete(0, tk.END)
    if operation== "addition":
        e.insert(0, first_num + second_num)
    elif operation== "subtraction":
        e.insert(0, first_num - second_num)
    elif operation== "multiplication":
        e.insert(0, first_num * second_num)
    elif operation== "division":
        e.insert(0, first_num / second_num)
    elif operation== "modulation":
        e.insert(0, first_num % second_num)
    elif operation== "plusminus":
        e.insert(0, -first_num)

b15=tk.Button(window, text='=', width=8, command=equal)
b15.grid(row=5, column=3, pady=5)


# CLEAR
def clear():
    e.delete(0, tk.END)

b17 = tk.Button(window, text='Clear', width=8, command=clear)
b17.grid(row=1, column=1, pady=5)


# EXIT
def destroy():
    window.destroy()

b20=tk.Button(window, text='Exit', width=8, command=destroy)
b20.grid(row=5, column=0, pady=5)


window.mainloop()