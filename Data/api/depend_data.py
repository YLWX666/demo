from operation_excel import OperationExcel
from runmethod import *
from get_data import GetData
from jsonpath_rw import jsonpath,parse


class DependdentData:

    def __init__(self,case_id):
        self.opera_excel = OperationExcel()
        self.case_id = case_id
        self.data = GetData()
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)
        res = run_method.run_main(method,url,request_data,header)
        return res

    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]



