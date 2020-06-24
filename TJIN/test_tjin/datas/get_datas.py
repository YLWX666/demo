

import json
import os

def get_path_file(file):
    '''

    :param file: 文件名
    :return: 文件名路径
    '''
    path = os.path.dirname(r'C:\Users\chexi\PycharmProjects\TJIN\test_tjin\datas\search_data')
    path_file = os.path.join(path,file)
    return path_file

#获取json文件
def json_data(file_name):
    '''

    :param file_name: 文件名路径
    :return: 列表
    '''
    with open(file_name,'r',encoding='utf-8') as e:
        data = json.load(e)
    return data




