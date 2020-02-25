from selenium import webdriver
import time

driver = webdriver.Chrome()

test1= ["a@a.a", ""] 
test2= ["aaa@a.a", "aA1aaaaa"]
test3= ["a@a.com", "aToast!1"]
test4= ["completelydifferentemailthing@emailthing.com", "TacoTown@2"] 
test5= ["", ""]

class CreateUser:
    def __init__(self, comp, nameF, nameL, username, password):
        self.comp = comp
        self.nameF = nameF
        self.nameL = nameL
        self.username = username
        self.password = password

    def makeUser(self):
        driver.set_page_load_timeout(30)
        driver.get("https://www.securitymetrics.com/create-account")
        driver.find_element_by_class_name("create-account-input ng-pristine ng-valid").send_keys(self.comp)
        driver.find_element_by_class_name("create-account-input ng-pristine ng-valid").send_keys(self.nameF)
        driver.find_element_by_class_name("create-account-input ng-pristine ng-valid").send_keys(self.nameL)
        driver.find_element_by_class_name("create-account-input ng-pristine ng-valid").send_keys(self.username)
        driver.find_element_by_class_name("create-account-input ng-pristine ng-valid").send_keys(self.password)
        driver.find_element_by_class_name("create-account-btn").click()
        driver.quit()
    

CreateUser("Scrub Co.", "Kayden", "Clark", "Kaydenclark725@gmil.com", "MikeMan8!")