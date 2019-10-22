# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('600x500')

canvas = tk.Canvas(window, bg='white', height=500, width=450)
image_file1 = tk.PhotoImage(file='funcube.gif')
image1 = canvas.create_image(10, 10, anchor='nw', image=image_file1)
x0, y0, x1, y1= 50, 50, 80, 80

image_file2 = tk.PhotoImage(file='1.gif')
image2 = canvas.create_image(10, 200, anchor='nw', image=image_file2)
x0, y0, x1, y1= 10, 10, 50, 50


#line = canvas.create_line(x0, y0, x1, y1)
#oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
#arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
#rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
canvas.pack()

def moveit():
    canvas.move(image2, 0, 10)

def moveup():
    canvas.move(image2, 0, -10)

b = tk.Button(window, text='move', command=moveit).pack()
b2 = tk.Button(window, text='moveup', command=moveup).pack()

window.mainloop()