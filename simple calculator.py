from tkinter import *
import tkinter as tk

count = 0


    
root = Tk()
root.title('Simple Calculator')



e = Entry(root, width=20 )
e.config(font=('Monospace',40,'bold'))
e.grid(row=0, column=0, columnspan=4, padx=40, pady=30)


def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)
    
def button_add():
    first_number = e.get()
    global math
    global f_num
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
        
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    

def button_sub():
    first_number = e.get()
    global math
    global f_num
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)


def configure_button(button):
    button.config(font=('Monospace', 50, 'bold'),
                 bg='#3b3b3b',
                 fg='#ffffff',
                 activebackground='#b3b3b3',
                 activeforeground='#fffff0',
                 padx=40,
                 pady=40)



#Button 1 Details
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
configure_button(button1)

#Button 2 Details
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
configure_button(button2)

#Button 3 Details
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
configure_button(button3)

#Button 4 Details
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
configure_button(button4)

#Button 5 Details
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
configure_button(button5)

#Button 6 Details
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
configure_button(button6)

#Button 7 Details
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
configure_button(button7)

#Button 8 Details
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
configure_button(button8)

#Button 9 Details
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
configure_button(button9)

#Button 0 Details
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
configure_button(button0)

#Button Add Details
button_addition = Button(root, text="+", padx=40, pady=20, command=button_add)
configure_button(button_addition)

#Button Subtract Details
button_sub = Button(root, text="-", padx=40, pady=20, command=button_sub)
configure_button(button_sub)

#Button Equals Details
button_equals = Button(root, text="=", padx=40, pady=20, command=button_equal)
configure_button(button_equals)

#Button Clear Details
button_clear = Button(root, text="C", padx=40, pady=20, command=button_clear)
configure_button(button_clear)

#Button Dot Details
button_dot = Button(root, text=".", padx=40, pady=20, command=lambda: button_click('.'))
configure_button(button_dot)




button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

button0.grid(row=5,column=1)

button_addition.grid(row=4,column=3)
button_sub.grid(row=3,column=3)
button_equals.grid(row=5,column=3)
button_clear.grid(row=5,column=0)
button_dot.grid(row=5,column=2)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.mainloop()