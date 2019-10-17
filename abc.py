# tkinter 的 下拉式選單

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


window = tk.Tk()

window.title('這個是我的第一個視窗表')

window.geometry('500x300')

labelTop = tk.Label(window,text = '選擇你最愛的月份')

labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(window, 
                            values=[
                                    "一月", 
                                    "二月",
                                    "三月",
                                    "四月",
                                    "五月"])                      
                                    
print(dict(comboExample)) 
comboExample.grid(column=0, row=1)
comboExample.current(1)

print(comboExample.current(), comboExample.get())

window.mainloop()
