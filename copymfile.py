
# 這個是為了要可以直接copy 系統裡面的資料。 方便我進行分析。 

import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk



# 定義 將檔案複製過去指定地方
def copyfile(src,dest):
	try:
		shutil.copy(src,dest)
	except shutil.Error as e:
		print('Error: %s'% e)
	except IOError as e:
		print('Error: %s'% e)

# 定義 將檔案移動到指定地方
def movefile(src,dest):

	try:
		shutil.move(src,dest)
	except shutil.Error as e:
		print('Error: %s'% e)
	except IOError as e:
		print('Error: %s'% e)

# 出現一個視窗提醒已經備份完畢了
def labwrite(words):
	root = tk.Tk()
	
	#words = """標籤加入圖片跟文字 使用的就是"tk.label ，然後裡面的文字如果要改，要先設定一個文字框輸入後，再等於"""
	w2 = tk.Label(root,
		   justify ='left',
           padx = 10,   
           text=words).pack(side="left") 

	root.mainloop()


copyfile('M://vivi file//鑫立財務管理 - datebase.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('M://vivi file//鑫立財務管理//鑫立財務系統_be.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('M://vivi file//薪資系統//考勤薪資系統_be.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('M://vivi file//營業現金//現金應付_be.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('M://vivi file//利息單據管理//利息收據輸入_be.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('Z://榮和財務系統_be.mdb','D://google 雲端硬碟//VB-預算計算//')

labwrite('檔案已經全部備份完成了！可以進行預算查詢了')


