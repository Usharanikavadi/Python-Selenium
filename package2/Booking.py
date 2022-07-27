import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Bookingtest(unittest.TestCase):
    def test_book(self):
        driver=webdriver.Chrome("D:\\chromedriver.exe")
        driver.get("file:///C:/Mini%20project-Rehuba%20Itc%20Airlines/bookingusha.html")
        driver.maximize_window()
        sel = Select (driver.find_element(By.ID,"input-group"))
        sel.select_by_index (2)
        sel = Select (driver.find_element(By.ID,"input-group1"))
        sel.select_by_index (3)
        sel = Select (driver.find_element(By.ID,"input-group2"))
        sel.select_by_index (2)
        sel = Select (driver.find_element(By.ID,"input-group3"))
        sel.select_by_index (3)
        sel = Select (driver.find_element(By.ID,"adult"))
        sel.select_by_index (10)
        driver.find_element(By.XPATH,"//input[@id=\"Arrival\"]").send_keys("12022022")
        driver.find_element(By.XPATH,"//input[@id=\"Departure\"]").send_keys("27022022")
        driver.find_element(By.XPATH,"//input[@id=\"dob\"]").send_keys("19091999")
        driver.find_element(By.ID,"radio1").click()
        driver.find_element(By.ID,"fname").send_keys("Usharani");
        driver.find_element(By.ID,"lname").send_keys("Kavadi");
        driver.find_element(By.CLASS_NAME,"phone").send_keys("9160201736");
        driver.find_element(By.CLASS_NAME,"email").send_keys("usha@gmail.com");
        driver.find_element(By.ID,"sub").click();
        driver.quit()