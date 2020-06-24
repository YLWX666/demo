import time
import unittest
import ddt
from element_step.step import StepElement



#可以把所有用例的数据存在json里，用ddt来处理重复代码
datas=({
    'js':'window.scrollTo(0,2200)',
    'element':'//*[@class="showImgs"]/a[1]',
    'href':'https://tj.qa.heywind.cn/blue-light-filter?int=hpcp1'
},{
    'js':'window.scrollTo(0,2200)',
    'element':'//*[@class="showImgs"]/a[2]',
    'href':'https://tj.qa.heywind.cn/eco-friendly?int=hpcp2'
    },{
    'js':'window.scrollTo(0,2200)',
    'element':'//*[@class="showImgs"]/a[3]',
    'href':'https://tj.qa.heywind.cn/misha-polished-black?int=hpcp3'
})

@ddt.ddt()
class TestImgUrl(unittest.TestCase):
    '''测试首页图片跳转链接'''

    def setUp(self) -> None:
        self.driver = StepElement()
        self.driver.open_url('https://tj.qa.heywind.cn')
        self.driver.by_xpath('//*[@class="cm_close"]').click()
    def tearDown(self) -> None:
        self.driver.close_web()

    def test_img_url(self):
        '''测试首页大图链接'''
        time.sleep(4)
        js = 'document.getElementsByClassName("vjs-poster")[0].click()'
        self.driver.action_js(js)
        time.sleep(2)
        url = self.driver.currenturl()
        self.assertEqual(url,'https://tijneyewear.com/duncan-light-khaki?int=hpfp',msg='路由不正确')

    @ddt.data(*datas)
    def test_img_url_summer(self,datas):
        '''测试summer perfection模块下3张图链接'''
        time.sleep(2)
        self.driver.action_js(datas['js'])
        time.sleep(4)
        href = self.driver.by_xpath(datas['element']).get_attribute('href')
        self.assertEqual(href,datas['href'],msg='路由不正确')

    def test_optical_img_url(self):
        '''optical模块左侧图链接'''
        time.sleep(2)
        self.driver.action_js('window.scrollTo(0,2550)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][5]/div[1]/a').get_attribute('href')
        self.assertEqual(href,'https://tj.qa.heywind.cn/optical?int=hpp',msg='路由不正确')

    def test_sunwear_img_url(self):
        '''sunwear模块右侧图链接'''
        time.sleep(4)
        self.driver.action_js('window.scrollTo(0,3200)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][6]/div[1]/a').get_attribute('href')
        self.assertEqual(href,'https://tj.qa.heywind.cn/sunwear?int=hpp',msg='路由不正确')

    def test_bluelight_img_url(self):
        '''bluelightfilter模块左侧图链接'''
        time.sleep(4)
        self.driver.action_js('window.scrollTo(0,4100)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][7]/div[1]/a').get_attribute('href')
        self.assertEqual(href,'https://tj.qa.heywind.cn/blue-light-filter?int=hpp',msg='路由不正确')

    def test_like_url(self):
        '''they all like模块右侧图链接'''
        time.sleep(4)
        self.driver.action_js('window.scrollTo(0,4900)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][8]/div[1]/a').get_attribute('href')
        self.assertEqual(href,'https://tj.qa.heywind.cn/maaike-amber?int=hpp',msg='路由不正确')

    def test_classic_url(self):
        '''its classic模块左侧图链接'''
        time.sleep(4)
        self.driver.action_js('window.scrollTo(0,5900)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][9]/div[1]/a').get_attribute('href')
        self.assertEqual(href,'https://tj.qa.heywind.cn/henk-gold-color?int=hpp',msg='路由不正确')

    def test_standout_url(self):
        '''standout now模块右侧图链接'''
        time.sleep(4)
        self.driver.action_js('window.scrollTo(0,6800)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][10]/div[1]/a').get_attribute('href')
        self.assertEqual(href,'https://tj.qa.heywind.cn/mitchel-opal-tortoise?int=hpp',msg='路由不正确')

    def test_trend_url(self):
        '''on trend模块左侧图链接'''
        time.sleep(4)
        self.driver.action_js('window.scrollTo(0,7700)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][11]/div[1]/a').get_attribute('href')
        self.assertEqual(href,'https://tijneyewear.com/federica-tortoise?int=hpp',msg='路由不正确')

    def test_tijn_sunwear_url(self):
        '''TIJN SUNWEAR模块左侧图链接'''
        time.sleep(4)
        self.driver.action_js('window.scrollTo(0,8500)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][12]/div[1]/a[1]').get_attribute('href')
        self.assertEqual(href,'https://tijnsunwear.com/?int=tjh_ts',msg='路由不正确')

    def test_walkon_url(self):
        '''WALK ON模块右侧图链接'''
        time.sleep(4)
        self.driver.action_js('window.scrollTo(0,8500)')
        time.sleep(4)
        href = self.driver.by_xpath('//*[@class="View_edit_tijn"][12]/div[1]/a[2]').get_attribute('href')
        self.assertEqual(href,'https://tijnhome.com/?int=tijn-hp',msg='路由不正确')



# if __name__ == "__main__":
#     unittest.main()
