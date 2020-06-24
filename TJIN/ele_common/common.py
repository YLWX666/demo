
import yaml,os

class Get_data:

    def __init__(self,file):
        '''

        :param file: 文件名
        '''
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
        '''

        :return: 列表
        '''
        with open(self.file_path,'r',encoding='utf-8') as f:
            data = yaml.load(f.read())
        return data

#获取登录数据
    def get_data(self,n):
        '''

        :param n: 列表序数
        :return: 新列表
        '''
        new_list = []
        data = self.yaml_data()
        for i in range(len(data)):
            if i == n:
                dicts = data[i]
                for y in dicts:
                    new_list.append(dicts[y])
                return new_list

    def data(self,n,m):
        datas =self.get_data(n)
        data = datas[m]
        return data


# if __name__ == '__main__':
#     data = Get_data('element_yaml')
#     d = data.get_data(2)
    # print(d)



