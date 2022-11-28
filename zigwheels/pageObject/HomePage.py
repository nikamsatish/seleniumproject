from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, "#bymakeid53").click()
    honda = (By.CSS_SELECTOR, "#bymakeid53")

    #w = Select(self.driver.find_element(By.ID, "maxPrice"))

    drop = (By.ID, "maxPrice")

    #list = self.driver.find_elements(By.TAG_NAME, "strong")
    ls =(By.TAG_NAME, "strong")

    # list1=self.driver.find_elements(By.XPATH, "//div[@class='clr-bl p-5']")
    ls1 = (By.XPATH, "//div[@class='clr-bl p-5']")

    def gethonda(self):
        return self.driver.find_element(*HomePage.honda)

    def getdrop(self):
        return Select(self.driver.find_element(*HomePage.drop))
    def get_list(self):
        return self.driver.find_elements(*HomePage.ls)

    def get_list1(self):
        return self.driver.find_elements(*HomePage.ls1)







