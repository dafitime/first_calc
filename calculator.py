from tkinter import *

count = 0
value1 = 0
value2 = 0

#def click():
#    global count
#    count += 1
#    label.config(text=count)

def calc():
    global count
    count += 1
    if count == 1:
        value == 
        

window = Tk()

#Button 1 Details
button1 = Button(window, text='1', width=4)
button1.config(command=calc)
button1.config(font=('Monospace', 50, 'bold'))
button1.config(bg='#ff6200')
button1.config(fg='#fffb1f')
button1.config(activebackground='#ff0000')
button1.config(activeforeground='#fffb1f')
button1 = lambda:print('1')

#Button 2 Details
button2 = Button(window, text='2', width=4)
button2.config(command=calc)
button2.config(font=('Monospace', 50, 'bold'))
button2.config(bg='#ff6200')
button2.config(fg='#fffb1f')
button2.config(activebackground='#ff0000')
button2.config(activeforeground='#fffb1f')


#Display the values
label = Label(window,text=count)
label.config(font=('Monospace',50,'bold'))
label.pack()
button1.pack()
button2.pack()
window.mainloop()