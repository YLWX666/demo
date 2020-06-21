
import requests

# url = 'https://www.baidu.com/s?{}'.format('刘亦菲')
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
#
#
# response = requests.get(url,headers=headers)
# print(response.content.decode())


class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "http://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {'User-Agent':'Mozilla/5.0'}
    def get_url_list(self):
        return [self.url_temp.format(i*50) for i in range(10)]

    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def save_html(self,html_str,page_num):
        file_path = "{}第{}页".format(self.tieba_name,page_num)
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(html_str)


    def main(self):
        url_list = self.get_url_list()

        for url in url_list:
            html_str = self.parse_url(url)

            page_num = url_list.index(url)+1
            self.save_html(html_str,page_num)

if __name__ == '__main__':
    ti = TiebaSpider('刘亦菲')
    ti.main()
























