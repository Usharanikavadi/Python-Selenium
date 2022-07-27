import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Registertest(unittest.TestCase):
    def test_reg(self):
        driver=webdriver.Chrome("D:\\chromedriver.exe")
        driver.get("file:///C:/Mini%20project-Rehuba%20Itc%20Airlines/Register.html")
        driver.maximize_window()
        driver.find_element(By.ID,"fname").send_keys("Usharani")
        driver.find_element(By.ID,"lname").send_keys("Kavadi")
        sel = Select (driver.find_element(By.ID,"country"))
        sel.select_by_index (1)
        driver.find_element(By.ID,"female").click()
        driver.find_element(By.ID,"mob").send_keys("9160201736")
        driver.find_element(By.ID,"email").send_keys("usha@gmail.com")
        driver.find_element(By.ID,"aadhar").send_keys("911203655272")
        driver.find_element(By.ID,"username").send_keys("Usharani12")
        driver.find_element(By.ID,"password").send_keys("Usha12345")
        driver.find_element(By.ID,"confirm-password").send_keys("Usha12345")
        driver.find_element(By.ID,"checkbox").click()
        driver.find_element(By.ID,"register").click()
        obj = driver.switch_to.alert
        obj.accept()
        driver.close()