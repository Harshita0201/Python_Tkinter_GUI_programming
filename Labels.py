from tkinter import*
root = Tk()
#creating a label widget
myLabel1=Label(root,text="Hello world!")
#putting it onto the screen
#myLabel.pack()
myLabel2=Label(root,text="My name is XYZ")
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
myLabel3=Label(root,text="Here we go....").grid(row=2,column=0)
root.mainloop()
