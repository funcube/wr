
#標籤的初步相關寫法跟參考
#pack,grid,palce 的差別

from tkinter import *
from PIL import Image,ImageTk


root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

w=1200
h=600

x =(screenWidth -w)/2
y =(screenHeight -h)/2


root.geometry("%dx%d+%d+%d" % (w,h,x,y))

root.title("如如測試用視窗")
# label 的標準使用辦法

img1 = Image.open('funcube.gif')
file1 =ImageTk.PhotoImage(img1)
#canvas.create_image(10,150,anchor='w',image =file1)

#label = Label(root,text ="我隨便打字的,長度要長一點。",fg="green",bg ="yellow",
	          #height =300, width =500,#這個是標籤的寬高
	          #font =("Helvetica",10,"bold"),#這個是字形設定的方式
	          #wraplength =80,justify ="left",#這個是多行文字對齊方式—：left:向左靠齊，right:右靠齊，center:置中
	          #image=file1,compound ="top",# 圖片跟文件的呈現方式，center:文字在上面，bottom文字下，UP文字上，left,right
	          #relief="raised")# 框框樣式 ，raise :浮起來，groove 內凹框，sunken 文字內凹

lab4 = Label(root,image=file1)

lab1 = Label(root,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(root,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(root,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15

#pack ,grid,palce 三種放置wiget的方式

#label.pack()                        # 包裝與定位元件，沒有標註就是最上面
#lab1.pack(side=LEFT,fill =X)        # 包裝與定位元件，向左靠齊
#lab2.pack(side=RIGHT,pady =10)       # 包裝與定位元件，向左靠齊
#lab3.pack(fill =X)                  # 包裝與定位元件，向右靠齊 fill 與sdie 無法並用哦。 請注意

lab1.grid(row=0,column=0,sticky=W)   # 格狀包裝, sticky =side 的功能 一樣是對齊
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝


lab4.place(x=200,y=200,width=500,height=240)



root.mainloop()