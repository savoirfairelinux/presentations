# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Lego(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://shop.lego.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_lego(self):
        driver = self.driver
        driver.get(self.base_url + "/fr-CA/")
        try: self.assertEqual("Du Nouveau", driver.find_element_by_xpath("//a[contains(text(),'Du Nouveau')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath(u"//a[contains(text(),'Thèmes')]").click()
        try: self.assertEqual(u"Star Wars™ (118)", driver.find_element_by_xpath(u"//div[@id='Star Wars™']/label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("a.test-AE0F776D-FD75-4DB9-9DAD-AD4852EC41F3 > img.main-image.test-theme-image").click()
        try: self.assertEqual(u"Recréez les aventures de Star Wars™ avec des figurines d'action et des jouets inspirés des films classiques et récents. Que vous soyez fan de Luke Skywalker™, Yoda™ ou même Darth Vader™, nos jouets Star Wars vous permettent de concevoir le combat ultime. Magasinez notre grande variété de figurines, de modèles et d'accessoires Star Wars pour revivre les moments passionnants de cette galaxie lointaine.", driver.find_element_by_id("longDescription").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("(//a[contains(text(),'4')])[4]").click()
        driver.find_element_by_css_selector(u"img[alt=\"Red Five X-wing Starfighter™\"]").click()
        try: self.assertEqual("10240", driver.find_element_by_css_selector("li.item.test-item > em").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
