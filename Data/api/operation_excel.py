import xlrd
from xlutils.copy import copy
# data = xlrd.open_workbook(r'C:\Users\Admin\Desktop\自动化测试用例.xls')
# tables = data.sheets()[0]
# print(tables.cell_value(1,1))

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            # self.data = self.get_data()
        else:
            self.file_name = r'C:\Users\Admin\Desktop\api.xls'
            self.sheet_id = 0
            self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
         res = self.data.nrows
         return res
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

#     写入数据
    def write_value(self,row,col,value):
        read = xlrd.open_workbook(self.file_name)
        write_data = copy(read)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data


    # 根据对应的caseid找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data():
            if case_id in col_data:
                return num
            else:
                num += 1
            return num

    #根据行号，找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data
    # 获取某一列的内容
    def  get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

# if __name__ == '__main__':
#     opers = OperationExcel()
#     print(opers.get_data().cell_value(1,0))