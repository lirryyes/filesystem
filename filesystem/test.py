import xlrd
file = xlrd.open_workbook("/Users/liuchun/PycharmProjects/filesystem/表格.xlsx")
#获取所有excel表格的名字
name = file.sheet_names()
xlsx = file.sheets()
file.nsheets
print(xlsx)