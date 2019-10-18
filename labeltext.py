# 練習 tkinter 的label 與text 

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import PhotoImage
  
# （1）這個是標籤文字+圖片的寫法函數

def labwrite(name,words):
	root = tk.Tk()
	logo = tk.PhotoImage(file='C:\\Users\\user\\Desktop\\wr\\' + name + '.gif') 
	w1 = tk.Label(root, image=logo).pack(side="right")  
	#words = """標籤加入圖片跟文字 使用的就是"tk.label ，然後裡面的文字如果要改，要先設定一個文字框輸入後，再等於"""
	w2 = tk.Label(root,
		   justify ='left',
           padx = 10,   
           text=words).pack(side="left") 
	root.mainloop()

#labwrite('funcube','測試標籤用') #這個是呼叫函數的方法，要用''把文字說明進入哦


#（2）文本寫法+下拉式滾動條 -Y軸+ 改視窗大小函數

def textwrite(h,w,q): 
	root = tk.Tk()

	ybar =tk.Scrollbar(root)
	ybar.pack(fill=tk.Y,side=tk.RIGHT)
	T = tk.Text(root,height= h, width=w)
	T.pack(fill=tk.Y,side=tk.LEFT)

	ybar.config(command=T.yview)
	T.config(yscrollcommand=ybar.set)

	quote = q
	T.insert('end', quote) # 將資料加入文本中用的是文本函數.insert (左右中間，然後文字)
	root.mainloop()

# textwrite(3,10,'這個是文本測試的資') #呼叫文本

