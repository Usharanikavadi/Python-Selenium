import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
def setUpModule():
    print("setupmodule")
def tearDownModule():
    print("tearDownmodule")

driver = webdriver.Chrome("D:\\chromedriver.exe")

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Open application")

    @classmethod
    def setUp(self):
        driver.get("file:///C:/Mini%20project-Rehuba%20Itc%20Airlines/loginpage.html")
        driver.maximize_window()
        print("something")

    def test_loginvalid(self):
        driver.find_element(By.CLASS_NAME, "username").send_keys("Usharani")
        driver.find_element(By.ID, "password").send_keys("Kavadi1234")
        driver.find_element(By.ID, "login").click()
        obj = driver.switch_to.alert
        obj.accept()


    def test_logininvalid(self):
        driver.find_element(By.CLASS_NAME, "username").send_keys("Gurudevi123")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "login").click()
        #obj = driver.switch_to.alert
        #obj.accept()


    def test_logininvalid1(self):
        driver.find_element(By.CLASS_NAME, "username").send_keys("Usha")
        driver.find_element(By.ID, "password").send_keys("usha12234")
        driver.find_element(By.ID, "login").click()
        #obj = driver.switch_to.alert
        #obj.accept()


    @classmethod
    def tearDown(self):
        #driver.quit(self)
        print("complete")

    @classmethod
    def tearDownClass(cls):
        driver.quit()
        print("Close the apllication")

if __name__=="__main__":
    unittest.main()
