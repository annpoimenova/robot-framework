from robot.api.deco import keyword
# from selenium import webdriver
from appium import webdriver
import time

class App:

    def __init__(self):
        desired_caps = {"app": "C:\Program Files (x86)\Poimenov\CommunalPayments\CommunalPayments.WPF.exe"}
        self.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps)

    def setup(self):
        return self.driver


class ComPayments(object):

    def open_app(self):
        self.driver = App().setup()
        return self.driver

    def click_menu_payments(self):
        self.driver.find_element_by_class_name("Menu").click()
        self.driver.find_element_by_name("Payments").click()
        self.driver.find_element_by_name("New Payment").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("ComboBox").click()
        self.driver.find_element_by_name("116665635, УЛ ГЕРОЕВ ТРУДА , 28А/36").click()
        self.driver.find_element_by_class_name("TextBox").send_keys("Комментарий Тестовый")



    def quit_app(self):
        self.driver.quit()
        # self.driver.close()
