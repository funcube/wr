# tkinter 的資料輸入然後按鍵後文件輸出。 

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


window = tk.Tk()

window.title('這個是我的第一個視窗表')

window.geometry('500x300')


e1 = tk.Entry(window, show='*', font=('Arial', 14))   # 顯示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 顯示成明文形式
e1.pack()
e2.pack()

# 第5步，定義兩個觸發事件時的函式insert_point和insert_end（注意：因為Python的執行順序是從上往下，所以函式一定要放在按鈕的上面）
def insert_point(): # 在滑鼠焦點處插入輸入內容
    var1 = e1.get() +e2.get()
    t.insert('insert', var1)
def insert_end():   # 在文字框內容最後接著插入輸入內容
    var2 = e1.get()
    t.insert('end', var2)
# 第6步，建立並放置兩個按鈕分別觸發兩種情況
b1 = tk.Button(window, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()

# 第7步，建立並放置一個多行文字框text用以顯示，指定height=3為文字框是三個字元高度
t = tk.Text(window, height=3)
t.pack()

window.mainloop()
