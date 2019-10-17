# tkinter 的Listbox視窗部件（選項）


import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


window = tk.Tk()

window.title('這個是我的第一個視窗表')

window.geometry('500x300')

# 在圖形介面上建立一個標籤label用以顯示並放置
var1 = tk.StringVar()  # 建立變數，用var1用來接收滑鼠點選具體選項的內容
l = tk.Label(window, bg='yellow', fg='black',font=('Arial', 12), width=10, textvariable=var1)
l.pack()

# 建立一個方法用於按鈕的點選事件
def print_selection():
    value = lb.get(lb.curselection())   # 獲取listbox(lb)當前格子選中的文字
    var1.set(value)  # 為label設定值

# 建立一個按鈕並放置，點選按鈕呼叫print_selection函式
b1 = tk.Button(window, text='打印選擇', width=15, height=2, command=print_selection)
b1.pack()

# 建立Listbox併為其新增內容
var2 = tk.StringVar()
var2.set(('vivi','wendy','aken','4')) # 為變數var2設定值

# 建立Listbox
lb = tk.Listbox(window, listvariable=var2)  #將var2的值賦給Listbox
# 建立一個list並將值迴圈新增到Listbox控制元件中
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end', item)  # 從最後一個位置開始加入值
lb.insert(1, 'first')       # 在第一個位置加入'first'字元
lb.insert(3, 'second')      # 在第二個位置加入'second'字元
lb.delete(2)                # 刪除第二個位置的字元
lb.pack()

window.mainloop()
