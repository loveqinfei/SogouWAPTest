#!/usr/bin/python
# encoding:utf-8
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
            return u'未找到该元素'
        else:
            item.click()
def init(self):
    self.driver.get('http://wap.sogou.com')
    sleep(1)
def item_text(self, item):
        if item == 'False':
            return u'未找到该元素'
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
    temp.send_keys('hello')
    item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/div[3]/input'))
    sleep(1)
    self.driver.back()

#WapHomePageTest测试类
class WapHomePageTest(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        option.add_argument('--user-agent=User-Agent: Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Redmi Note 2 Build/LRX22G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.5.729 U3/0.8.0 Mobile Safari/534.30')
        self.driver = webdriver.Chrome(chrome_options=option)
        sleep(1)
        self.driver.set_window_size(400, 850)
        init(self)
    def tearDown(self):
        self.driver.quit()
    #测试case
    def test01(self):
        '''天气测试'''
        log("Step 1：点击天气按钮")
        item_click(self, waitfor(self, 'id', 'index_weather'))
        sleep(2)
        weather_result = item_is_displayed(self, waitfor(self, 'classname', 'w-info'))
        log("Step 2：判断天气卡片是否存在："+weather_result)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual('True', weather_result)
        log("wap首页天气点击测试结果：True")
    def test02(self):
        '''登陆测试'''
        log("Step 1：点击登陆按钮")
        item_click(self, waitfor(self, 'id', 'loginText'))
        item = item_text(self, waitfor(self, 'id', 'login_qq'))
        log("Step 2：判断是否跳转登陆页面，查找元素为："+item)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual(u"QQ账号", item)
        log("登陆点击测试结果：True")
    def test03(self):
        '''suggestion是否存在测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：输入搜索词：hello")
        temp.send_keys('hello')
        suggestion = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/span[2]'))
        log("Step 3：判断是否出现了suggestion浮层："+suggestion)
        log("Step 4：比较预期结果和实际结果")
        self.assertEqual(u'继承者', suggestion)
        log("suggestion测试结果：True")
    def test04(self):
        '''suggestion上屏按钮点击上屏测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：输入查询词：hello")
        temp.send_keys('hello')
        suggestion = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/span[2]'))
        log("Step 3：点击上屏按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/a'))
        temp = waitfor(self, 'id', 'keyword')
        item =temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词："+item)
        log("Step 5：比较预期结果和实际结果")
        self.assertIn(suggestion, item)
        log("suggestion上屏按钮点击上屏测试结果: True")
    def test05(self):
        '''suggestion长按搜索测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：输入查询词：hello")
        temp.send_keys('hello')
        log("Step 3：长按suggestion搜索")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]'))
        sleep(1)
        temp = waitfor(self, 'id', 'keyword')
        item = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词："+item)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello继承者',item)
        log("suggestion长按搜索测试结果：True")
    def test06(self):
        '''suggestion点击关闭按钮测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：输入查询词：hello")
        temp.send_keys('hello')
        log("Step 3：等待sugg出现并点击关闭按钮")
        item_click(self, waitfor(self, 'linktext', '关闭'))
        sleep(1)
        item = self.driver.find_element_by_xpath('//*[@id="sug_wraper"]/ul[2]').is_displayed()
        log("Step 4：判断sugg浮层是否还存在："+str(item))
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual('False', str(item))
        log("suggestion点击关闭按钮测试结果：True")
    def test07(self):
        '''搜索按钮测试'''
        log("Step 1：点击搜索框")
        temp = waitfor(self, 'id', 'keyword')
        log("Step 2：输入查询词：hello")
        temp.send_keys('hello')
        log("Step 3：点击搜索按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="searchform"]/div/div[1]/div[3]/input'))
        temp = waitfor(self, 'id', 'keyword')
        button_text = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词："+button_text)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello', button_text)
        log("搜索按钮点击测试结果：True")
    def test08(self):
        '''历史记录是否存在测试'''
        log("Step 1：调用搜索函数，产生一条搜索记录")
        sousuo(self)
        sleep(1)
        item_click(self, waitfor(self, 'id', 'keyword'))
        item = item_text(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/span'))
        log("Step 2：获取历史记录的词："+item)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual(u'hello', item)
        log("历史记录测试结果：True")
    def test09(self):
        '''历史记录上屏按钮测试'''
        log("Step 1：调用搜索函数，产生一条搜索记录")
        sousuo(self)
        sleep(1)
        log("Step 2：点击搜索框")
        item_click(self, waitfor(self, 'id', 'keyword'))
        log("Step 3：点击历史记录中的上屏按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/a'))
        sleep(1)
        temp = waitfor(self, 'id', 'keyword')
        history_text = temp.get_attribute("value")
        log("Step 4：获取搜索框中的词："+history_text)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello', history_text)
        log("历史记录上屏按钮上屏测试结果：True")
    def test10(self):
        '''历史记录长按上屏测试'''
        log("Step 1：调用搜索函数，产生一条搜索记录")
        sousuo(self)
        sleep(1)
        log("Step 2：点击搜索框")
        item_click(self, waitfor(self, 'id', 'keyword'))
        log("Step 3：长按历史记录上屏")
        item_click(self, waitfor(self, 'xpath', '//*[@id="sug_wraper"]/ul[2]/li[1]/span'))
        temp = waitfor(self, 'id', 'keyword')
        item = temp.get_attribute("value")
        log("Step 4：获取搜索框中的查询词："+item)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(u'hello', item)
        log("历史记录长按上屏测试结果：True")
    def test11(self):
        '''历史记录点击关闭按钮测试'''
        log("Step 1：调用搜索函数，产生一条搜索记录")
        sousuo(self)
        sleep(1)
        log("Step 2：点击搜索框")
        item_click(self, waitfor(self, 'id', 'keyword'))
        log("Step 3：点击历史记录关闭按钮")
        item_click(self, waitfor(self, 'linktext', '关闭'))
        result = self.driver.find_element_by_xpath('//*[@id="sug_wraper"]/ul[2]').is_displayed()
        log("Step 4：判断历史记录框是否存在："+str(result))
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual('False', str(result))
        log("历史记录点击关闭按钮测试结果：True" )
    def test12(self):
        '''历史记录点击清除历史按钮测试'''
        log("Step 1：调用搜索函数，产生一条搜索记录")
        sousuo(self)
        sleep(1)
        item_click(self, waitfor(self, 'id', 'keyword'))
        log("Step 2：点击清除历史按钮")
        item_click(self, waitfor(self, 'linktext', '清除历史'))
        sleep(1)
        log("Step 3：点击确定清除")
        button = self.driver.switch_to_alert()
        button.accept()
        result = self.driver.find_element_by_xpath('//*[@id="sug_wraper"]/ul[2]').is_displayed()
        log("Step 4：判断历史记录框是否存在："+str(result))
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual('False', str(result))
        log("历史记录点击清除历史按钮测试结果：True")
    def test13(self):
        '''语音按钮测试'''
        log("Step 1：点击麦克风图标")
        item_click(self, waitfor(self, 'id', 'pan_sogou_mic_con'))
        item = item_text(self, waitfor(self, 'id', 'pan_sogou_butn1'))
        log("Step 2：判断是否有以后再说按钮："+item)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual(u'以后再说', item)
        log("语音按钮点击测试结果：True")
    def test14(self):
        '''语音按钮点击立即体验测试'''
        log("Step 1：点击麦克风图标")
        item_click(self, waitfor(self, 'id', 'pan_sogou_mic_con'))
        log("Step 2：点击立即体验按钮")
        item_click(self, waitfor(self, 'id', 'pan_sogou_butn2'))
        item = item_text(self, waitfor(self, 'id', 'id-pkg-size'))
        log("Step 3：判断是否到了下载页："+item)
        log("Step 4：比较预期结果和实际结果")
        self.assertIn(u'安装包大小', item)
        log("搜狗搜索推广测试结果：True")
    def test15(self):
        '''各个垂搜入口测试'''
        log("Step 1：依次点击各个垂搜入口，并存储页面标题")
        #包含明医的垂搜入口
        click_list = ['小说','微信','知乎','新闻','明医','英文','学术','图片','视频','地图','网址']
        result_list = ['首页','微信','知乎','新闻','明医','英文','学术','图片','影视','地图','网址']
        #旧版垂搜入口
        #click_list = ['小说', '微信', '知乎', '新闻', '应用', '本地', '图片', '视频', '地图', '问问', '百科', '购物', '音乐', '寻人', '网址']
        #result_list = ['首页', '微信', '知乎', '新闻', '应用', '本地生活', '图片', '影视', '地图', '问问', '百科', '首页', '音乐', '寻人', '网址']
        #新版垂搜入口
        #click_list = ['小说', '微信', '知乎', '新闻', '英文','图片', '应用', '视频', '地图','网址']
        #result_list = ['首页', '微信', '知乎', '新闻', '英文','图片', '应用', '影视', '地图', '网址']
        #没有英文垂搜的入口
        #click_list = ['小说', '微信', '知乎', '新闻','图片', '应用', '视频', '地图','网址']
        #result_list = ['首页', '微信', '知乎', '新闻','图片', '应用', '影视', '地图', '网址']
        temp_list = []
        for i in click_list:
            #if int(click_list.index(i)) > 4:
                #item_click(self, waitfor(self, 'linktext', '更多'))
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
            log(str(i) + '_垂搜测试结果：'+str(result_list[a] in temp_list[a]))
            a = a + 1
    def test16(self):
        '''本地生活卡片_八个入口点击测试'''
        log("Step 1：依次点击本地生活八个图标")
        #线下环境本地生活入口
        #list = ['电影', '团购', '外卖', '景点门票', '电话大全', '美食', 'KTV', '足疗']
        #线上环境本地生活入口
        list = ['电影', '美食', 'KTV', '足疗按摩', '外卖', '家政', '上门服务', '医疗健康']
        title = []
        for i in list:
            item_click(self, waitfor(self, 'linktext', i))
            sleep(1)
            t = self.driver.title
            title.append(t)
            if i == '电话大全':
                item_click(self, waitfor(self, 'id', 'detail_top_return'))
                item_click(self, waitfor(self, 'id', 'detail_top_return'))
                item_click(self, waitfor(self, 'id', 'detail_top_return'))
            else:
                item_click(self, waitfor(self, 'id', 'detail_top_return'))
            sleep(1)
        j = 0
        log("Step 2：比较预期结果和实际结果")
        for i in list:
            self.assertIn(i, title[j])
            log('本地生活_' + i +'_测试结果是：True' )
            j = j + 1
    def test17(self):
        '''本地生活卡片_查看更多测试'''
        log("Step 1：点击查看更多按钮")
        item_click(self, waitfor(self, 'linktext', '查看更多'))
        sleep(1)
        t = self.driver.title
        log("Step 2：获取页面标题："+t)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual(u'本地生活',t)
        log('本地生活点击更多测试结果：True')
    def test18(self):
        '''粉丝大作战_全部明星按钮测试'''
        log("Step 1：点击全部明星按钮")
        item_click(self, waitfor(self, 'linktext', '全部明星'))
        result = item_is_displayed(self, waitfor(self, 'xpath', '//*[@id="rankPage"]/header'))
        log("Step 2：判断是否跳转到全部明星list页面："+result)
        log("Step 3：比较预期结果和实际结果")
        self.assertTrue(result)
        log('全部明星按钮点击测试结果：True')
    def test19(self):
        '''粉丝大作战_现在去占楼按钮测试'''
        log("Step 1：点击现在去占楼按钮")
        item_click(self, waitfor(self, 'classname', 'js-card-star-name'))
        sleep(1)
        title = self.driver.title
        log("Step 2：获取页面标题："+title)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual(u'粉丝大作战',title)
        log('现在去占楼按钮点击测试结果：True')
    def test20(self):
        '''粉丝大作战_换一个按钮测试'''
        cardname1 = item_text(self,waitfor(self, 'classname', 'js-card-star-name'))
        log("Step 1：获取当前明星姓名："+cardname1)
        log("Step 2：点击换一个按钮")
        item_click(self, waitfor(self, 'linktext', '换一个'))
        sleep(1)
        cardname2 = item_text(self, waitfor(self, 'classname', 'js-card-star-name'))
        log("Step 3：再次获取当前明星姓名："+cardname2)
        log("Step 4：比较两次获取的姓名是否一致："+str(cardname1==cardname2))
        self.assertNotEqual(cardname1, cardname2)
        log('换一个按钮点击测试结果：True')
    def test21(self):
        '''实时热点卡片更多热词按钮测试'''
        log("Step 1：点击更多热词按钮")
        item_click(self, waitfor(self, 'linktext', '更多热词'))
        temp = waitfor(self, 'id', 'keyword')
        item = temp.get_attribute("value")
        log("Step 2：获取搜索框中的搜索词："+item)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual(u'今日热点头条', item)
        log('更多热词按钮点击测试结果：True')
    def test22(self):
        '''实时热点卡片6组热词点击测试'''
        log("Step 1：依次点击6组热词，然后比较预期结果和实际结果")
        a = 1
        b = 1
        for i in range(3):
            for j in range(2):
                hotword_data_text = self.driver.find_element_by_xpath('//*[@id="hotword_data"]/li['+str(a)+']/p['+str(b)+']/a/span').text
                self.driver.find_element_by_xpath('//*[@id="hotword_data"]/li['+str(a)+']/p['+str(b)+']/a/span').click()
                sleep(1)
                keyword_text = self.driver.find_element_by_id("keyword").get_attribute("value")
                self.assertEqual(hotword_data_text, keyword_text)
                log('实时热点_'+str(hotword_data_text)+'_点击测试结果：True')
                self.driver.back()
                b = b + 1
                sleep(2)
            b = 1
            a = a + 1
    def test23(self):
        '''实时热点卡片换一批按钮测试'''
        hotword_data_text = item_text(self, waitfor(self, 'xpath', '//*[@id="hotword_data"]/li[1]/p[1]/a/span'))
        log("Step 1：获取第一个热词内容："+hotword_data_text)
        log("Step 2：点击换一批按钮")
        item_click(self, waitfor(self, 'linktext', '换一批'))
        hotword_data_text_refresh = item_text(self, waitfor(self, 'xpath', '//*[@id="hotword_data"]/li[1]/p[1]/a/span'))
        log("Step 3：再次获取第一个热词内容："+hotword_data_text_refresh)
        log("Step 4：比较两次获取的第一个热词内容是否相同："+str(hotword_data_text==hotword_data_text_refresh))
        self.assertNotEqual(hotword_data_text, hotword_data_text_refresh)
        log('换一批按钮点击测试结果：True')
    def test24(self):
        '''常用工具卡片测试'''
        tools_list = ['万年历', '快递查询', '违章查询', '在线翻译', '周公解梦', '星座运势', '姓名测试', '单位换算']
        log("Step 1：依次点击八个常用工具按钮，并获取页面标题,然后比较预期结果和实际结果")
        for i in tools_list:
            item_click(self, waitfor(self, 'linktext', i))
            tools_text = item_text(self, waitfor(self, 'xpath', '//*[@id="detail_top"]/span'))
            if i =='快递查询':
                i = '快递'
            self.assertIn(tools_text, i)
            log('常用工具_'+i+'_点击测试结果：True')
            item_click(self, waitfor(self, 'classname', 'life-return'))
    def test25(self):
        '''搞笑段子卡片再来一个测试'''
        log("Step 1：获取搞笑段子内容")
        joke_text = item_text(self, waitfor(self, 'xpath', '//*[@id="smile"]/div[2]'))
        log("Step 2：点击再来一个按钮")
        item_click(self, waitfor(self, 'linktext', '再来一个'))
        log("Step 3：再次获取搞笑段子内容")
        joke_text_refresh = item_text(self, waitfor(self, 'xpath', '//*[@id="smile"]/div[2]'))
        log("Step 4：比较预期结果和实际结果")
        self.assertNotEqual(joke_text, joke_text_refresh)
        log("搞笑段子再来一个测试结果：True")
    def test26(self):
        '''搞笑段子卡片分享测试'''
        log("Step 1：点击分享按钮")
        item_click(self, waitfor(self, 'xpath', '//*[@id="smile"]/div[1]/a'))
        joke_result = item_is_displayed(self, waitfor(self, 'classname', 'vr-share'))
        log("Step 2：判断分享浮层是否存在："+joke_result)
        log("Step 3：比较预期结果和实际结果")
        self.assertTrue(joke_result)
        log("搞笑段子分享测试结果：True")
    def test27(self):
        '''卡片管理测试'''
        log("Step 1：点击卡片管理按钮")
        item_click(self, waitfor(self, 'linktext', '卡片管理'))
        log("Step 2：点击搞笑段子卡片的上移")
        item_click(self, waitfor(self, 'xpath', '//*[@id="control"]/div[2]/ul[1]/li[5]/div/a[1]'))
        log("Step 3：点击返回按钮")
        item_click(self, waitfor(self, 'classname', 'jscard-back'))
        log("Step 4：获取当前卡片的排序")
        card_control = ['//*[@id="locallife"]/div/div[2]/span', '//*[@id="star"]/div/span', '//*[@id="hotquery"]/div[2]/span', '//*[@id="tool"]/div[2]/span', '//*[@id="smile"]/div[1]/span']
        title_list = []
        for i in card_control:
            title_text = item_text(self, waitfor(self, 'xpath', i))
            title_list.append(title_text)
        log("Step 5：比较预期结果和实际结果")
        self.assertEqual(title_list.index('搞笑段子'),4)
        log('卡片管理_搞笑段子顺序上移测试结果：True')
    def test28(self):
        '''用户反馈测试'''
        log("Step 1：点击用户反馈按钮")
        item_click(self, waitfor(self, 'linktext', '用户反馈'))
        sleep(1)
        page_title = self.driver.title
        log("Step 2：获取页面标题："+page_title)
        log("Step 3：比较预期结果和实际结果")
        self.assertEqual(u'用户反馈', page_title)
        log("用户反馈点击测试结果：True")
    def test29(self):
        '''搜索框X按钮测试'''
        temp = waitfor(self, 'id', 'keyword')
        temp.send_keys('hello')
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
        log("搜索框X按钮测试测试结果：True")

if __name__ == "__main__":
    suite = unittest.makeSuite(WapHomePageTest)
    time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    htmlfile = 'HomePage_TestResult_'+str(time)+'.html'
    fp = file(htmlfile, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"WAP HomePage Automation Testing", description=u"通过chrome浏览器配置手机UA模拟测试" )
    runner.run(suite)
    fp.close()