import requests

headers = {'User-Agent':'Mozilla/5.0'}

post_data = {
    "query":"人生苦短，我用Python",
    "from":"zh",
    "to":"en"
}
post_url = "http://fanyi.baidu.com/basetrans"

r = requests.post(post_url,data=post_data,headers=headers)
print(r.content.decode('utf-8'))