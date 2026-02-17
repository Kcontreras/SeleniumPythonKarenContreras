
from practice.SamplePackage import BaseTest
from practice.Utilities import ExcelUtilities
import pytest
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from practice.SamplePackage.BaseTest import BaseTest

class TestRegister(BaseTest):

    def test_create_an_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Testing")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Test")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generating_emails())
        print(self.generating_emails())
        time.sleep(2)  # Wait to ensure email is processed
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("123456")
        self.driver.find_element(By.ID, "input-confirm").send_keys("123456")
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        assert self.driver.find_element(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']").is_displayed()

    def test_create_an_account_with_all_fields(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Testing")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Test")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generating_emails())
        print(self.generating_emails())
        time.sleep(2)  # Wait to ensure email is processed
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("123456")
        self.driver.find_element(By.ID, "input-confirm").send_keys("123456")
        self.driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()  # Subscribe to newsletter
        time.sleep(2)  # Wait to ensure newsletter option is processed
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        assert self.driver.find_element(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']").is_displayed() 
    def generating_emails(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "Test" + timestamp + "@example.com"


        
