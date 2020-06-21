import xlrd

data = xlrd.open_workbook(r'C:\Users\Admin\Desktop\自动化测试用例.xls')
table = data.sheets()[0]
print(table.nrows)
print(table.cell_value(0,'1'))