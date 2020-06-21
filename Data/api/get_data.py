from operation_excel import OperationExcel
import data_config
from operation_json import OperationJson

class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    def get_case_lines(self):
        res = self.opera_excel.get_lines()
        return res
    # 是否执行
    def get_is_run(self,row):
        flag = None
        col = data_config.get_run()
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

#     是否携带header
    def  is_header(self,row):
        col = data_config.get_header()
        headers = self.opera_excel.get_cell_value(row,col)
        if headers == 'yes':
            return data_config.get_header_value()
        else:
            return None

    def get_request_method(self,row):
        col = data_config.get_run_way()
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    def get_url(self,row):
        col = data_config.get_url()
        url = self.opera_excel.get_cell_value(row,col)
        return url
    # 请求数据
    def get_request_data(self,row):
        col = data_config.get_data()
        data = self.opera_excel.get_cell_value(row,col)
        if data =='':
            return None
        else:
            return data
    #通过关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    def get_expcet_data(self,row):
        col = data_config.get_except()
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == '':
            return None
        return expect

    def get_result(self,row,value):
        col = data_config.get_result()
        self.opera_excel.write_value(row,col,value)

    def get_depend_key(self,row):
        col = data_config.get_data_depend()
        depend_key = self.opera_excel.get_cell_value(row,col)
        if depend_key == '':
            return None
        else:
            return depend_key

    def is_depend(self,row):
        col = data_config.get_field_depend()
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    def get_depend_field(self,row):
        col = data_config.get_field_depend()
        data = self.opera_excel.get_cell_value(row,col)
        if data == "":
            return None
        else:
            return data

