# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SelenPython(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://schorrmedia.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_selen_python(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Automation").click()
        driver.find_element_by_link_text("Websites").click()
        driver.find_element_by_link_text("Video").click()
        driver.find_element_by_link_text("About Us").click()
        driver.find_element_by_link_text("Blog").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Logging with Log4j2')])[2]").click()
        driver.find_element_by_id("author").clear()
        driver.find_element_by_id("author").send_keys("nancy")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("nancy")
        driver.find_element_by_id("url").clear()
        driver.find_element_by_id("url").send_keys("nancy")
    
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
