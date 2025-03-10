# #GUI - tkinter
# #root window
# from tkinter import *
# #instance of class TK
# root = Tk()
# #display the window
# root.mainloop()
# ----------#or
# import tkinter as tk
# def main():
#     window= tk.Tk()
#     window.mainloop()
# main()
# ------------------------------
# #button
# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()
#=========================================================================
# #create buttons
# from tkinter import Tk, Label, Button
# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")
#         self.label = Label(master, text="This is our first GUI!")
#         self.label.pack()
#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()
#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#     def greet(self):
#         print("Greetings!")
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()


#==================================================================
# #canvas
# from tkinter import *
# master = Tk()
# w = Canvas(master, width=40, height=60)
# w.pack()
# canvas_height=20
# canvas_width=200
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y )
# mainloop()

#===========================================================
# #checkbutton
# from tkinter import *
# master = Tk()
# var1 = IntVar()
# Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
# mainloop()

#=========================================================

# #Entry
# from tkinter import *
# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()

#=================================================
"""
#Frame
from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)
root.mainloop()
"""
#================================================================

# #Listbox
# from tkinter import *
# top = Tk()
# Lb = Listbox(top)
# Lb.insert(3, 'Python')
# Lb.insert(4, 'Java')
# Lb.insert(1, 'C++')
# Lb.insert(2, 'Any other')
# Lb.pack()
# top.mainloop()

#==================================================
"""
#menu
#click on file and help
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()
"""

#===================================================

"""
#calculator
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)
root = Tk()
my_gui = Calculator(root)
root.mainloop()

"""
#=========================================================
"""
#Table
from tkinter import *
class Table:
    def __init__(self,root):
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
# create root window
root = Tk()
t = Table(root)
root.mainloop()

"""

#==========================================================

