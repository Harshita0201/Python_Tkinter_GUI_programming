from tkinter import *
root=Tk()
v=StringVar()
e=Entry(root,width=50,textvariable=v).pack()
e.insert(0,"Enter Name: ")
#e.get()
#the get function gets the stuff typed into the entry field
#insert(0,text="Enter Name: ")
#this will insert the text at the 0 index within the entry widget
def myClick():
    #myLabel=Label(root,text="Hello " + v.get())
    #myLabel.pack()
    #or
    Hello="Hello " + v.get()
    myLabel=Label(root,text=Hello).pack()
    

myButton=Button(root,text="Enter your name",command=myClick).pack()
root.mainloop()
