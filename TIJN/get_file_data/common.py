
import yaml,os

class Get_data:

    def __init__(self,file=None):
        self.file_path = self.get_file_path(file)

#获取文件
    def get_file_path(self,file_name):
        '''
        :param file_name: 文件名
        :return: 文件路径
        '''
        path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(path,file_name)
        return file_path

#读取yaml文件
    def yaml_data(self):
        with open(self.file_path,'r',encoding='utf-8') as f:
            data = yaml.load(f.read())
        return data

#获取登录数据
    def login_data(self,n):
        new_list = []
        data = self.yaml_data()
        for i in range(len(data)):
            if i == n:
                dicts = data[i]
                for y in dicts:
                    new_list.append(dicts[y])
                return new_list


# if __name__ == '__main__':
#     data = Get_data('element_yaml')
#     print(data.yaml_data())




