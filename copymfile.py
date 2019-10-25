
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

from datetime import datetime
X =datetime.today()

cusy = X.year
cusm = X.month
cusd = X.day
idname = str(cusy)+'-'+str(cusm)+'-'+str(cusd)

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

Dir1 ='D://google 雲端硬碟//VB-預算計算//'
Dir2 ='D://google 雲端硬碟//VB-預算計算//備份//'
name1 ='鑫立財務管理 - datebase'
name2 ='鑫立財務系統_be'
name3 ='考勤薪資系統_be'
name4 ='現金應付_be'
name5 ='利息收據輸入_be'
name6 ='榮和財務系統_be'
name7 ='A-預算計算'
name8 ='借款記錄'

src1 = Dir1+name1+'.mdb'
src2 = Dir1+name2+'.mdb'
src3 = Dir1+name3+'.mdb'
src4 = Dir1+name4+'.mdb'
src5 = Dir1+name5+'.mdb'
src6 = Dir1+name6+'.mdb'
src7 = Dir1+name7+'.mdb'
src8 = Dir1+name8+'.mdb'

des1= Dir2 +name1+idname+'.mdb'
des2= Dir2 +name2+idname+'.mdb'
des3= Dir2 +name3+idname+'.mdb'
des4= Dir2 +name4+idname+'.mdb'
des5= Dir2 +name5+idname+'.mdb'
des6= Dir2 +name6+idname+'.mdb'
des7= Dir2 +name7+idname+'.mdb'
des8= Dir2 +name8+idname+'.mdb'

movefile(src1, des1)
movefile(src2, des2)
movefile(src3, des3)
movefile(src4, des4)
movefile(src5, des5)
movefile(src6, des6)
copyfile(src7, des7)
copyfile(src8, des8)

copyfile('M://vivi file//鑫立財務管理 - datebase.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('M://vivi file//鑫立財務管理//鑫立財務系統_be.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('M://vivi file//薪資系統//考勤薪資系統_be.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('M://vivi file//營業現金//現金應付_be.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('M://vivi file//利息單據管理//利息收據輸入_be.mdb','D://google 雲端硬碟//VB-預算計算//')
copyfile('Z://榮和財務系統_be.mdb','D://google 雲端硬碟//VB-預算計算//')

labwrite('檔案已經全部備份完成了！可以進行預算查詢了')


