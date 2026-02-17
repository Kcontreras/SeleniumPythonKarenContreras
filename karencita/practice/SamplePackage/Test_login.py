from xml.parsers.expat import errors
from practice.SamplePackage.BaseTest import BaseTest
from selenium import webdriver
from selenium.webdriver.common.by import By
from practice.Utilities import ExcelUtilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pytest

class TestLogin(BaseTest):

    @pytest.mark.parametrize("email, password", ExcelUtilities.get_data("practice/excel_file/Python_course.xlsx","Hoja1"))
    def test_login_with_valid_credentials(self, email, password):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password    )
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        # después de click Login
        errors = self.driver.find_elements(By.CSS_SELECTOR, ".alert-danger, .text-danger")
        if errors:
            raise AssertionError("Login failed: " + " | ".join(e.text for e in errors if e.text.strip()))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit your account information"))
        )
        assert True #self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()


    def test_login_with_invalid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        time.sleep(2)  # Wait for the warning message to appear
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
        time.sleep(2)

