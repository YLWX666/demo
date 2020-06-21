# from runmethod import RunMethod
# from get_data import GetData
# from common_util import CommonUtil
# import json
# from depend_data import DependdentData
# class RunTest:
#     def __init__(self):
#         self.run_method = RunMethod()
#         self.data = GetData()
#         self.common = CommonUtil()
#
#
#     def go_on_run(self):
#         rows_count = self.data.get_case_lines()
#         for i in range(1,rows_count):
#             url = self.data.get_url(i)
#             method = self.data.get_request_method(i)
#             is_run = self.data.get_is_run(i)
#             request_data = self.data.get_data_for_json(i)
#             header = self.data.is_header(i)
#             expect = self.data.get_expcet_data(i)
#             depend_case = self.data.is_depend(i)
#             if depend_case != None:
#                 self.depend_data = DependdentData(i)
#                 depend_response_data = self.depend_data.get_data_for_key(i)
#                 depend_key = self.data.get_depend_field(i)
#                 request_data[depend_key] = depend_response_data
#             if is_run:
#                 res = self.run_method.run_main(method,url,request_data,header)
#                 list01 = json.load(res)
#                 if self.common.is_contain(expect,list01):
#                     self.data.get_result(i,"pass")
#                 else:
#                     self.data.get_result(i,"fail")

# if __name__ == '__main__':
#     run = RunTest()
#     run.go_on_run()
