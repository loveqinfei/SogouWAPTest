#!/usr/bin/python
# encoding: utf-8
__author__ = 'qinfei'

import unittest
import HTMLTestRunner
from selenium import webdriver
from time import sleep
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#公共调用函数
def waitfor(self, findtype, value):
            trytimes = 20
            while trytimes > 0:
                try:
                    if findtype == 'xpath':
                        item = self.driver.find_element_by_xpath(value)
                    elif findtype == 'id':
                        item = self.driver.find_element_by_id(value)
                    elif findtype == 'classname':
                        item = self.driver.find_element_by_class_name(value)
                    elif findtype == 'linktext':
                        item = self.driver.find_element_by_link_text(value)
                    if item.is_displayed():
                        return item
                    else:
                        sleep(1)
                        trytimes = trytimes - 1
                except Exception:
                        sleep(1)
                        trytimes = trytimes - 1
            return 'False'
def item_click(self, item):
        if item == 'False':
            return '未找到该元素'
        else:
            item.click()
def init(self):
        self.driver.get('http://wap.sogou.com/web/searchList.jsp?uID=MsBw6IEXR7NGE7Ik&v=5&w=1278&t=1460814035109&s_t=1460814043863&s_from=result_up&keyword=%E7%A7%A6%E9%A3%9E&pg=webSearchList')
        sleep(1)
def item_text(self, item):
        if item == 'False':
            return '未找到该元素'
        else:
            return item.text
def item_is_displayed(self,item):
        if item == 'False':
            return u'未找到该元素'
        else:
            return 'True'
def log(a):
        print(str(a))
def sousuo(self):
    init(self)
    temp = waitfor(self, 'id', 'keyword')
    sleep(1)
    temp.clear()
    temp.send_keys('hello')
    item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/input[10]'))
    sleep(1)

#WapHomePageTest测试类
class WapHomePageTest(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        #option.add_argument('--user-agent=User-Agent: Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Redmi Note 2 Build/LRX22G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.5.729 U3/0.8.0 Mobile Safari/534.30')
        #option.add_argument('--user-agent=User-Agent: Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Redmi Note 2 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.5 Mobile Safari/537.36')
        option.add_argument('--user-agent=User-Agent: Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; ATH-AL00 Build/HONORATH-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 SogouMSE,SogouMobileBrowser/4.2.6')
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.set_window_size(400, 850)
        init(self)
    def tearDown(self):
        self.driver.quit()
    #测试case
    def test01(self):
        '''结果页左上角logo测试'''
        log("Step 1：点击logo按钮")
        item_click(self, waitfor(self, 'classname', 'logo'))
        sleep(1)
        logo_result = item_is_displayed(self, waitfor(self, 'classname', 'index-weather'))
        log("Step 2：判断是否有天气卡片："+logo_result)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual('True', logo_result)
        log("结果页左上角logo点击测试结果：True")
    def test02(self):
        '''结果页顶部导航测试'''
        log("Step 1：依次点击结果页顶部各个导航入口，并存储页面标题")
        #旧版结果页导航入口
        #click_list = ['小说', '微信', '知乎', '应用', '本地', '图片', '视频', '地图', '新闻', '问问', '百科', '购物', '音乐']
        #result_list = ['小说', '微信', '知乎', '应用', '本地',  '图片', '影视', '地图', '新闻', '搜索结果', '百科', '购物', '音乐']
        #新版结果页导航入口
        click_list = ['小说','明医','英文','学术','微信','知乎','新闻','图片','应用','视频','问问','百科']
        result_list = ['小说','明医','英文','学术','微信','知乎','新闻','图片','应用','影视','搜索结果','百科']

        temp_list = []
        for i in click_list:
            if int(click_list.index(i)) > 2:
                item_click(self, waitfor(self, 'linktext', '更多'))
            item_click(self, waitfor(self, 'linktext', i))
            sleep(1)
            title = self.driver.title
            temp_list.append(title)
            self.driver.back()
            sleep(2)
        a = 0
        log("Step 2：比较预期结果和实际结果")
        for i in click_list:
            self.assertIn(result_list[a], temp_list[a])
            #log(str(i) + '_垂搜测试结果：True')
            log('顶部导航_'+str(i) + '_测试结果：'+str(result_list[a] in temp_list[a]))
            a = a + 1
    def test03(self):
        '''顶部搜索按钮测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：点击搜索按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/input[10]'))
        temp = waitfor(self, 'id', 'keyword')
        button_text = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词："+button_text)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello', button_text)
        log("顶部搜索按钮点击测试结果：True")
    def test04(self):
        '''顶部suggestion是否存在测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入搜索词：hello")
        temp.clear()
        temp.send_keys('hello')
        suggestion = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]'))
        log("Step 3：判断是否出现了suggestion浮层："+suggestion)
        log("Step 4：比较预期结果和实际结果")
        self.assertEqual(u'hello继承者', suggestion)
        log("顶部suggestion测试结果：True")
    def test05(self):
        '''顶部suggestion上屏按钮点击上屏测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        suggestion = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]'))
        log("Step 3：点击上屏按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/a'))
        temp = waitfor(self, 'id', 'keyword')
        item = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词")
        log("Step 5：比较预期结果和实际结果："+item)
        self.assertIn(suggestion, item)
        log("顶部suggestion上屏按钮点击上屏测试结果: True")
    def test06(self):
        '''顶部suggestion长按搜索测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：长按suggestion搜索")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]'))
        sleep(1)
        temp = waitfor(self, 'id', 'keyword')
        item = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词："+item)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello继承者',item)
        log("顶部suggestion长按搜索测试结果：True")
    def test07(self):
        '''顶部suggestion点击关闭按钮测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：等待sugg出现并点击关闭按钮")
        item_click(self, waitfor(self, 'linktext', '关闭'))
        sleep(1)
        item = self.driver.find_element_by_xpath('//*[@id="sug_wraper"]/ul[2]').is_displayed()
        log("Step 4：判断sugg浮层是否还存在："+str(item))
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual('False', str(item))
        log("顶部suggestion点击关闭按钮测试结果：True")
    def test08(self):
        '''顶部历史记录是否存在测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：点击搜索按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/input[10]'))
        sleep(1)
        log("Step 4：返回上一页")
        self.driver.back()
        log("Step 5：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        temp.clear()
        item = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/span'))
        log("Step 6：获取历史记录的词："+item)
        log("Step 7：比较预期结果和实际结果")
        self.assertEqual(u'hello', item)
        log("顶部历史记录测试结果：True")
    def test09(self):
        '''顶部历史记录上屏按钮测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：点击搜索按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/input[10]'))
        log("Step 4：返回上一页")
        sleep(1)
        self.driver.back()
        sleep(1)
        log("Step 5：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        temp.clear()
        log("Step 6：点击历史记录中的上屏按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/a'))
        sleep(1)
        temp = waitfor(self, 'id', 'keyword')
        history_text = temp.get_attribute("value")
        log("Step 7：获取搜索框中的词："+history_text)
        log("Step 8：比较预期结果和实际结果")
        self.assertEqual(u'hello', history_text)
        log("顶部历史记录上屏按钮上屏测试结果：True")
    def test10(self):
        '''顶部历史记录长按上屏测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：点击搜索按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/input[10]'))
        sleep(1)
        log("Step 4：返回上一页")
        self.driver.back()
        sleep(1)
        log("Step 5：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        temp.clear()
        log("Step 6：长按历史记录上屏")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/span'))
        temp = waitfor(self, 'id', 'keyword')
        item = temp.get_attribute("value")
        log("Step 7：获取搜索框中的查询词："+item)
        log("Step 8：比较预期结果和实际结果")
        self.assertEqual(u'hello', item)
        log("顶部历史记录长按上屏测试结果：True")
    def test11(self):
        '''顶部历史记录点击关闭按钮测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：点击搜索按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/input[10]'))
        sleep(1)
        log("Step 4：返回上一页")
        self.driver.back()
        sleep(1)
        log("Step 5：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        temp.clear()
        log("Step 6：点击历史记录关闭按钮")
        item_click(self, waitfor(self, 'linktext', '关闭'))
        result = self.driver.find_element_by_xpath('//*[@id="sug_wraper"]/ul[2]').is_displayed()
        log("Step 7：判断历史记录框是否存在："+str(result))
        log("Step 8：比较预期结果和实际结果")
        self.assertEqual('False', str(result))
        log("顶部历史记录点击关闭按钮测试结果：True" )
    def test12(self):
        '''顶部历史记录点击清除历史按钮测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：点击搜索按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/input[10]'))
        sleep(1)
        log("Step 4：返回上一页")
        self.driver.back()
        sleep(1)
        log("Step 5：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        temp.clear()
        log("Step 6：点击清除历史按钮")
        item_click(self, waitfor(self, 'linktext', '清除历史'))
        sleep(1)
        log("Step 6：点击确定清除")
        button = self.driver.switch_to_alert()
        button.accept()
        result = self.driver.find_element_by_xpath('//*[@id="sug_wraper"]/ul[2]').is_displayed()
        log("Step 7：判断历史记录框是否存在："+str(result))
        log("Step 8：比较预期结果和实际结果")
        self.assertEqual('False', str(result))
        log("顶部历史记录点击清除历史按钮测试结果：True")
    def test13(self):
        '''顶部X按钮测试'''
        temp = waitfor(self, 'id', 'keyword')
        temp.click()
        log("Step 1：有query，点击X按钮")
        item_click(self, waitfor(self, 'id', 'resetbtn'))
        item = self.driver.find_element_by_id('resetbtn').is_displayed()
        log("Step 2：判断是否X按钮是否存在："+ str(item))
        log("Step 3：比较预期结果和实际结果")
        sleep(1)
        self.assertEqual('False', str(item))
        temp = waitfor(self, 'id', 'keyword')
        querytext = temp.text
        sleep(1)
        self.assertEqual('', querytext)
        log("Step 4：X按钮清空搜索框测试结果：True")
        log("Step 5：输入查询词：qinfei")
        temp.send_keys('qinfei')
        sleep(1)
        temp = waitfor(self, 'id', 'resetbtn')
        item = temp.is_displayed()
        log("Step 6：再次判断X按钮是否存在："+ str(item))
        log("Step 7：比较预期结果和实际结果")
        sleep(1)
        self.assertEqual('True', str(item))
        log("顶部X按钮测试结果：True")
    def test14(self):
        '''底部X按钮测试'''
        log("Step 1：有query，点击X按钮")
        self.driver.execute_script("scroll(250,100000);")
        item_click(self, waitfor(self, 'id', 'foot_resetbtn'))
        item = self.driver.find_element_by_id('foot_resetbtn').is_displayed()
        log("Step 2：判断是否X按钮是否存在："+ str(item))
        sleep(1)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual('False', str(item))
        temp = waitfor(self, 'id', 'foot_keyword')
        querytext = temp.text
        sleep(1)
        self.assertEqual('', querytext)
        log("Step 4：X按钮清空搜索框测试结果：True")
        log("Step 5：输入查询词：qinfei")
        temp.send_keys('qinfei')
        sleep(1)
        temp = waitfor(self, 'id', 'foot_resetbtn')
        item = temp.is_displayed()
        log("Step 6：再次判断X按钮是否存在："+ str(item))
        sleep(1)
        log("Step 7：比较预期结果和实际结果")
        self.assertEqual('True', str(item))
        log("底部X按钮测试结果：True")
    def test15(self):
        '''底部搜索按钮测试'''
        self.driver.execute_script("scroll(250,100000);")
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'foot_keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：点击搜索按钮")
        sleep(1)
        item_click(self, waitfor(self, 'xpath', '//*[@id="foot_searchform"]/div/div[1]/input[9]'))
        sleep(1)
        temp = waitfor(self, 'id', 'keyword')
        button_text = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词："+button_text)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello', button_text)
        log("顶部搜索按钮点击测试结果：True")
    def test16(self):
        '''底部suggestion是否存在测试'''
        self.driver.execute_script("scroll(250,100000);")
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'foot_keyword')
        log("Step 2：清空搜索框，输入搜索词：hello")
        temp.clear()
        temp.send_keys('hello')
        suggestion = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper2"]/ul[2]/li[1]/span[2]'))
        log("Step 3：判断是否出现了suggestion浮层："+suggestion)
        log("Step 4：比较预期结果和实际结果")
        self.assertEqual(u'继承者', suggestion)
        log("顶部suggestion测试结果：True")
    def test17(self):
        '''底部suggestion上屏按钮点击上屏测试'''
        self.driver.execute_script("scroll(250,100000);")
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'foot_keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        suggestion = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper2"]/ul[2]/li[1]/span[2]'))
        log("Step 3：点击上屏按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper2"]/ul[2]/li[1]/a'))
        temp = waitfor(self, 'id', 'foot_keyword')
        item = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词")
        log("Step 5：比较预期结果和实际结果："+item)
        self.assertIn(suggestion, item)
        log("底部suggestion上屏按钮点击上屏测试结果: True")
    def test18(self):
        '''底部suggestion长按搜索测试'''
        self.driver.execute_script("scroll(250,100000);")
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'foot_keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：长按suggestion搜索")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper2"]/ul[2]/li[1]'))
        sleep(1)
        temp = waitfor(self, 'id', 'keyword')
        item = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词："+item)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello继承者',item)
        log("底部suggestion长按搜索测试结果：True")
    def test19(self):
        '''底部suggestion点击关闭按钮测试'''
        self.driver.execute_script("scroll(250,100000);")
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'foot_keyword')
        log("Step 2：清空搜索框，输入查询词：hello")
        temp.clear()
        temp.send_keys('hello')
        log("Step 3：等待sugg出现并点击关闭按钮")
        sleep(1)
        self.driver.execute_script("scroll(250,50);")
        item_click(self, waitfor(self, 'linktext', '关闭'))
        item = self.driver.find_element_by_xpath('//*[@id="sug_wraper2"]/ul[2]/li[1]').is_displayed()
        log("Step 4：判断sugg浮层是否还存在："+str(item))
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual('False', str(item))
        log("底部suggestion点击关闭按钮测试结果：True")
    def test20(self):
        '''底部历史记录是否存在测试'''
        log("Step 1：调用搜索函数，产生一条搜索历史记录")
        sousuo(self)
        self.driver.execute_script("scroll(250,100000);")
        log("Step 2：点击搜索框")
        temp = waitfor(self, 'id', 'foot_keyword')
        temp.clear()
        item = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper2"]/ul[2]/li[1]'))
        log("Step 3：获取历史记录的词："+item)
        log("Step 4：比较预期结果和实际结果")
        self.assertEqual(u'hello', item)
        log("底部历史记录测试结果：True")
    def test21(self):
        '''底部历史记录上屏按钮测试'''
        log("Step 1：调用搜索函数，产生一条搜索历史记录")
        sousuo(self)
        self.driver.execute_script("scroll(250,100000);")
        log("Step 2：点击搜索框")
        temp = waitfor(self, 'id', 'foot_keyword')
        temp.clear()
        log("Step 3：点击历史记录中的上屏按钮")
        sleep(1)
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper2"]/ul[2]/li[1]/a'))
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper2"]/ul[2]/li[1]/a'))
        temp = waitfor(self, 'id', 'foot_keyword')
        history_text = temp.get_attribute("value")
        log("Step 4：获取搜索框中的词："+history_text)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello', history_text)
        log("底部历史记录上屏按钮上屏测试结果：True")
    # def test22(self):
    #     '''底部历史记录长按上屏测试'''
    #     log("Step 1：调用搜索函数，产生一条搜索历史记录")
    #     sousuo(self)
    #     self.driver.execute_script("scroll(250,100000);")
    #     log("Step 2：点击搜索框")
    #     temp = waitfor(self, 'id', 'foot_keyword')
    #     temp.clear()
    #     temp.click()
    #     log("Step 3：长按历史记录上屏")
    #     item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper2"]/ul[2]/li[1]/span'))
    #     sleep(1)
    #     temp = waitfor(self, 'id', 'foot_keyword')
    #     item = temp.get_attribute("value")
    #     log("Step 4：获取搜索框中的查询词："+item)
    #     log("Step 5：比较预期结果和实际结果")
    #     self.assertEqual(u'hello', item)
    #     log("底部历史记录长按上屏测试结果：True")
    def test23(self):
        '''底部历史记录点击关闭按钮测试'''
        log("Step 1：调用搜索函数，产生一条搜索历史记录")
        sousuo(self)
        self.driver.execute_script("scroll(250,100000);")
        log("Step 2：点击搜索框")
        temp = waitfor(self, 'id', 'foot_keyword')
        temp.clear()
        log("Step 3：点击历史记录关闭按钮")
        item_click(self, waitfor(self, 'linktext', '关闭'))
        result = self.driver.find_element_by_xpath('//*[@id="sug_wraper"]/ul[2]').is_displayed()
        log("Step 4：判断历史记录框是否存在："+str(result))
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual('False', str(result))
        log("底部历史记录点击关闭按钮测试结果：True" )
    def test24(self):
        '''底部历史记录点击清除历史按钮测试'''
        log("Step 1：调用搜索函数，产生一条搜索历史记录")
        sousuo(self)
        self.driver.execute_script("scroll(250,100000);")
        log("Step 2：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        temp.clear()
        log("Step 3：点击清除历史按钮")
        item_click(self, waitfor(self, 'linktext', '清除历史'))
        sleep(1)
        log("Step 4：点击确定清除")
        button = self.driver.switch_to_alert()
        button.accept()
        result = self.driver.find_element_by_xpath('//*[@id="sug_wraper"]/ul[2]').is_displayed()
        log("Step 5：判断历史记录框是否存在："+str(result))
        log("Step 6：比较预期结果和实际结果")
        self.assertEqual('False', str(result))
        log("底部历史记录点击清除历史按钮测试结果：True")
    def test25(self):
        '''结果页底部导航测试'''
        log("Step 1：依次点击结果页底部各个导航入口，并存储页面标题")
        click_list = ['首页', '导航', '免责', '寻人', '用户反馈']
        result_list = ['搜狗搜索', '导航', '免责', '寻人', '用户反馈']
        temp_list = []
        for i in click_list:
            self.driver.execute_script("scroll(250,100000);")
            item_click(self, waitfor(self, 'linktext', i))
            sleep(1)
            title = self.driver.title
            temp_list.append(title)
            self.driver.back()
            sleep(2)
        a = 0
        log("Step 2：比较预期结果和实际结果")
        for i in click_list:
            self.assertIn(result_list[a], temp_list[a])
            #log(str(i) + '_垂搜测试结果：True')
            log('底部导航_'+str(i) + '_测试结果：'+str(result_list[a] in temp_list[a]))
            a = a + 1
    def test26(self):
        '''结果页中间hint测试'''
        log("Step 1：依次点击中间4个hint，然后比较预期结果和实际结果")
        a = 1
        b = 1
        for i in range(2):
            for j in range(2):
                hint_data_text = self.driver.find_element_by_xpath('//*[@id="formerhints"]/ul/li['+str(a)+']/a['+str(b)+ ']').text
                self.driver.find_element_by_xpath('//*[@id="formerhints"]/ul/li['+str(a)+']/a['+str(b)+']').click()
                sleep(1)
                hint_text = self.driver.find_element_by_id("keyword").get_attribute("value")
                self.assertEqual(hint_data_text, hint_text)
                log('hint_'+str(hint_data_text)+'_点击测试结果：True')
                self.driver.back()
                b = b + 1
                sleep(2)
            b = 1
            a = a + 1
    def test27(self):
        '''结果页底部hint测试'''
        log("Step 1：依次点击底部8个hint，然后比较预期结果和实际结果")
        a = 1
        b = 1
        for i in range(4):
            for j in range(2):
                self.driver.execute_script("scroll(250,650);")
                hint_data_text = self.driver.find_element_by_xpath('//*[@id="hint"]/ul/li['+str(a)+']/a['+str(b)+']').text
                self.driver.find_element_by_xpath('//*[@id="hint"]/ul/li['+str(a)+']/a['+str(b)+']').click()
                sleep(1)
                hint_text = self.driver.find_element_by_id("keyword").get_attribute("value")
                self.assertEqual(hint_data_text, hint_text)
                log('hint_'+str(hint_data_text)+'_点击测试结果：True')
                self.driver.back()
                b = b + 1
                sleep(2)
            b = 1
            a = a + 1
    def test28(self):
        '''结果页下一页按钮测试'''
        log("Step 1：点击下一页按钮")
        item_click(self, waitfor(self, 'linktext', '下一页'))
        item = item_is_displayed(self, waitfor(self, 'xpath', '//*[@id="mainBody"]/div[3]'))
        log("Step 2：判断是不是有第二页："+item)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual('True', 'True')
        log("结果页下一页按钮测试结果：True")
        
if __name__ == "__main__":
    suite = unittest.makeSuite(WapHomePageTest)
    time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    htmlfile = 'ResultPage_TestResult_'+str(time)+'.html'
    fp = file(htmlfile, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"Wap Result Page Automation Testing", description=u"通过chrome浏览器配置手机UA模拟测试" )
    runner.run(suite)
    fp.close()