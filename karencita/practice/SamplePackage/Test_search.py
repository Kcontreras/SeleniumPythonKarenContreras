from practice.SamplePackage.BaseTest import BaseTest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure


@allure.severity(allure.severity_level.NORMAL)
class TestSearch(BaseTest):

    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)  # Wait for search results to load
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    def test_search_for_an_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)  # Wait for search results to load
        expected_message = "There is no product that matches the search criteria."
        actual_message = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        assert actual_message.__eq__(expected_message)

    def test_search_with_empty_input(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)  # Wait for search results to load
        expected_message = "There is no product that matches the search criteria."
        actual_message = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        assert actual_message.__eq__(expected_message)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_search_with_empty_input", attachment_type=allure.attachment_type.PNG)