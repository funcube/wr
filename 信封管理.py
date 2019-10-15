
# 信封.csv 的數值必須全部選為通用 ，就是不能有‘ ，’，這個必須跟育靜特別交代。
# 這個是用於信封檔案轉貼用

cus = []

from datetime import datetime
X =datetime.today()

cusy = X.year
cusm = X.month
cusd = X.day
idname = str(cusy)+'-'+str(cusm)+'-'

print(idname)



with open('信封.csv', 'r') as f:
	for line in f:
		for line in f:
		 B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10 = line.strip().split(',')
		 cus.append([ B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10])

# print (cus)

for c in cus:
	print(idname+ c[0], str(cusy), str(cusm),c[0],c[6])



filename = '信封管理'+ idname+str(cusd)+'.csv'

with open(filename,'w') as f:
		for c in cus:
			idn = (idname +c[0])
			iy = str(cusy)
			im = str(cusm)
			f.write(idn+','+ iy+','+ im+','+ c[0]+','+ c[6]+'\n' )


print('轉檔OK-可以複製貼上了 !!!')

