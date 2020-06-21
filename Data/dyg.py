import re
import requests

url = 'https://www.doudada.com/rank/celebrity/total'
headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'

def get_html():
    html = requests.get(url,headers).text

    # html = html.decode('utf-8')
    print(html)
    return html

html = get_html()



def parse_html(html):
    p = re.compile('<tr class="rank text-red" data-v-42019572>(.*?).*?<a href=.*?>(.*?)<td calss=.*?>(.*?).*?</tr>',re.S)
    r_list = p.findall(html)
    print(r_list)
    r_dict = {}
parse_html(html)

#
#     for rt in r_list:
#         r_dict['排名'] = rt[0].strip()
#         r_dict['名星'] = rt[1].strip()
#         r_dict['粉丝'] = rt[2].strip()
#         print(r_dict)



# if __name__ == "__main__":
#     dou = DouYin('https://www.doudada.com/rank/celebrity/total')
#     dou.get_html()
