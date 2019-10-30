
from tkinter import * 
mainwindow = Tk() 
def leftclick(event): 
	print("left") 
def middleclick(event): 
	print("middle") 
def rightclick(event): 
	print("right") 
frame = Frame(mainwindow, width=300, height=250) 
frame.bind("<Button-1>", leftclick) 
frame.bind("<Button-2>", middleclick) 
frame.bind("<Button-3>", rightclick) 
frame.focus_set() 
frame.pack()
mainwindow.mainloop()
 



 