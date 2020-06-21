import json

# with open(r'\Users\Admin\Desktop\a.json','r') as fp:
#     data = json.load(fp)
#     print(data)
class OperationJson:

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open(r'C:\Users\Admin\Desktop\a.json','r') as fp:
            data = json.load(fp)
            return data

    def get_data(self,id):
        return self.data[id]

# if __name__ == '__main__':
#     opjson = OperationJson()

