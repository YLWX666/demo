import requests

class RunMethod:

    def post_main(self,url,data,header=None):
        if header != None:
            res = requests.post(url=url,data=data,header=header).json()
        else:
            res = requests.post(url=url,data=data).json()
        return res
    def get_main(self,url,header,data=None):
        if header != None:
            res = requests.get(url=url,data=data,header=header).json()
        else:
            res = requests.get(url=url,data=data).json()
        return res

    def run_main(self,method,url,data=None,header=None):
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res

