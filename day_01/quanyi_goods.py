# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class QuanyiGoods(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.qydsc.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_quanyi_goods(self):
        driver = self.driver
        # 请求地址
        driver.get(self.base_url + "/")

        # # 鼠标悬停到控件上
        # abc = driver.find_element_by_id("JS_hide_side_menu_3>dl>dt>a")
        # ActionChains(driver).move_to_element(abc).perform()
        # time.sleep(5)
        #
        # driver.find_element_by_link_text(u"猪肉").click()
        # time.sleep(5)
        # driver.find_element_by_xpath(u"//img[@alt='一片排骨 7950-8050g/份']").click()
        # driver.find_element_by_css_selector("span.goods_add").click()
        # driver.find_element_by_css_selector("span.goods_add").click()
        # driver.find_element_by_css_selector("span.goods_cut").click()
        # driver.find_element_by_css_selector("a.buy_btn").click()
        # driver.find_element_by_xpath("//div[@id='speDiv']/div[2]/div[2]/a/img").click()
        # driver.find_element_by_link_text(u"删除").click()
        # self.assertEqual(u"您确实要把该商品移出购物车吗？", self.close_alert_and_get_its_text())
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
