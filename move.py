from tkinter import *
from PIL import Image,ImageTk

tk= Tk()

def leftclick(event): 
	canvas.move(1,-5,0)
	print("left")
def middleclick(event): 
	canvas.move(1,0,-5)
	print("middle") 
def rightclick(event): 
	canvas.move(1,5,0)
	print("right") 

canvas = Canvas(tk,width=640, height=480)



canvas.pack()

canvas.create_polygon(10,10,100,10,50,80,fill ='',outline='black')

canvas.bind("<KeyPress-Left>", leftclick) 
canvas.bind("<KeyPress-Right>", middleclick) 
canvas.bind("<KeyPress-Up>", rightclick) 
canvas.focus_set() 

tk.mainloop()


