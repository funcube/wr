
# excell 資料讀取跟存檔 

# （1） 定義月份跟年份的函數，資料整理使用


from datetime import datetime
X =datetime.today()

cusy = X.year
cusm = X.month
cusd = X.day
idname = str(cusy)+'-'+str(cusm)+'-'

#（2）  讀取已經存在的檔案

from openpyxl import load_workbook


wb = load_workbook(filename = '10806.xlsx')

# ws = wb.active  # 正在主動的資料夾
# ws = 指定名稱資料夾

ws = wb["Sheet1"]

# （3） 將檔案存入【】中 

company = [] 
rows = ws.rows
columns = ws.columns

for row in rows:

	if '帳款含稅款'in row:
		continue

	line = [col.value for col in row] 

	 # print (line)
 
 # print ('客戶編號:',line[0] ,line [4] ,line [5]) # 打印excell資料的指定欄位

	company.append(line) #將 讀取資料存儲list 

# print (company) #打印加入company 的所有的資料


for c in company: #這個欄位是要確認我們資料處理是否正確的
		print(idname+ c[0], str(cusy), str(cusm),c[0],c[6])

filename = '信封管理'+ idname+str(cusd)+'.csv'

# (4) 將資料存成 CSV 檔案

with open(filename,'w') as f:
		for c in company:
			idn = (idname +c[0])
			iy = str(cusy)
			im = str(cusm)
			f.write(idn+','+ iy+','+ im+','+ str(c[0])+','+ str(c[6])+'\n' )


print('轉檔OK-可以複製貼上了 !!!')