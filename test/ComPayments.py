from robot.api.deco import keyword
# from selenium import webdriver
from appium import webdriver
import time

from selenium.webdriver import ActionChains


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
        datagridcell = self.driver.find_elements_by_class_name("DataGridCell")
        list_grid = []
        for e in datagridcell:
            list_grid.append(e.text)
        id = list_grid[::8]
        service = list_grid[1::8]
        period_from = list_grid[2::8]
        period_to = list_grid[3::8]
        previous_counter = list_grid[4::8]
        current_counter = list_grid[5::8]
        difference = list_grid[6::8]
        amount = list_grid[7::8]

        self.driver.find_element_by_name("Save").click()
        self.driver.find_element_by_name("Payments").click()
        self.driver.find_element_by_name("Payments").click()
        self.driver.find_element_by_class_name("ComboBox").click()
        self.driver.find_element_by_name("116665635, УЛ ГЕРОЕВ ТРУДА , 28А/36").click()
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element_by_name("Комментарий Тестовый")).perform()
        self.driver.find_element_by_name("Export to Html").click()
        file_path = "C:/Users/Anna_Poimenova/AppData/Local/poimenov/CommunalPayments/Reports/221.html"
        file_expected = ""
        with open('file1.html') as file1, open('file2.html') as file2:
            for file1Line, file2Line in zip(file1, file2):
                if file1Line != file2Line:
                    print(file1Line.strip('\n'))
                    print(file2Line.strip('\n'))


    def quit_app(self):
        self.driver.quit()
        # self.driver.close()
