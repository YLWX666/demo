import requests

proxies = {"http":"http://163.177.151.23:80"}

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}

r = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)
print(r.content.decode('utf-8'))