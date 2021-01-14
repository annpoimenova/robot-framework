from robot.api.deco import keyword
# from selenium import webdriver
from appium import webdriver

class App:

    def __init__(self):
        desired_caps = {"app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"}
        self.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps)

    def setup(self):
        return self.driver


class ComPayments(object):

    def open_app(self):
        self.driver = App().setup()
        return self.driver

    def click_calculator_button(self, str):
        self.driver.find_element_by_name(str).click()

    def getresult(self):
        display_text = self.driver.find_element_by_id("CalculatorResults").text
        display_text = display_text.strip("Display is ")
        display_text = display_text.rstrip(' ')
        display_text = display_text.lstrip(' ')
        return display_text

    def quit_app(self):
        self.driver.close()
        self.driver.quit()