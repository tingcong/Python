#coding=utf-8
import xlrd  #读数据


data=xlrd.open_workbook('C:\\Users\\htc\\Desktop\\iResearch20170317.xlsx')
sheet_A=data.sheet_by_index(0)
sheet_B=data.sheet_by_index(1)
sheet_C=data.sheet_by_index(2)
# print sheet_A.name
# print sheet_A.ncols
# print sheet_A.nrows
# print sheet_A.cell(1,1).value
AppName=[]

for i in range(100):
	print int(sheet_A.cell(i+2,0).value)
	for j in range(100):
		if str(sheet_A.cell(i+3,1).value) ==sheet_B.cell(j+3,1).value:
# 			if sheet_A.cell(i+3,0).value-sheet_B.cell(j+3,0).value>50 :
# 				AppName.append(sheet_A.cell(i+3,1))
# 				print sheet_A.cell(i+3,1)

#for z in range(len(AppName)):
#	print AppName[z].decode("utf-8")
