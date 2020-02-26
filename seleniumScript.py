from selenium import webdriver
from selenium.webdriver.common.keys import Keys

test1= ["a@a.a", ""] #it will fail due to no password "all fields required"
test2= ["aaa@a.a", "aA1aaaaa"] #it will pass
test3= ["a@a.com", "aToast!1"] # it will fail due to "email already in use"
test4= ["completelydifferentemailthing@emailthing.com", "TacoTown@2"] #it will pass
test5= ["", ""] #it will fail due to no entry "all fields required"

tests = [test1, test2, test3, test4, test5] #place all test into an array so that they can be looped through

class CreateUser:
    def __init__(self, comp, nameF, nameL, username, password): #all fields are required so I added a company, first and last name to the list
        self.comp = comp
        self.nameF = nameF
        self.nameL = nameL
        self.username = username
        self.password = password

    def makeUser(self, shootnum): #added a shoot Number so that the results may be recoreded
        driver = webdriver.Chrome() #opens a chrome window
        driver.set_page_load_timeout(30) #sets how long a window is open so if an error happens the window will still close
        driver.get("https://www.securitymetrics.com/create-account")
        """        
        Looking at the code in Javascript they use the ng-pristine to determine if the input field has had any
        interaction, therfore once I have sent that input field keys it changes to ng-dirty and thus I can 
        target the ng-pristine over and over to fill out the form
        """
        driver.find_element_by_class_name("ng-pristine").send_keys(self.comp)
        driver.find_element_by_class_name("ng-pristine").send_keys(self.nameF)
        driver.find_element_by_class_name("ng-pristine").send_keys(self.nameL)
        driver.find_element_by_class_name("ng-pristine").send_keys(self.username)
        driver.find_element_by_class_name("ng-pristine").send_keys(self.password)
        driver.find_element_by_class_name("ng-pristine").send_keys(self.password)
        driver.find_element_by_class_name("create-account-btn").click()
        driver.get_screenshot_as_file(f".\\screenshots\\shoot{shootnum}.png")
        # assert "accountCtrl.result_type" in driver.find_elements_by_tag_name("body") == AssertionError

        driver.quit()
    
for i in range(len(tests)):
    CreateUser("Test Co.", "Kayden", "Clark", tests[i][0], tests[i][1]).makeUser(i)
    

    """
    If I had more python experience or more time to more fully explore the technology, 
    I would incorporate a fail safe in the makeUser() function so if one testcase fails
    it does not end the whole program.
    """