import unittest

from selenium import webdriver
#from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def test_log(self):
        driver = webdriver.Chrome("D:\\chromedriver.exe")
        driver.get("file:///C:/Mini%20project-Rehuba%20Itc%20Airlines/loginpage.html")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "username").send_keys("Usharani")
        driver.find_element(By.ID, "password").send_keys("Kavadi1234")
        driver.find_element(By.ID, "login").click()
        obj = driver.switch_to.alert
        obj.accept()
        driver.close()


if __name__=="__main__":
    unittest.main()