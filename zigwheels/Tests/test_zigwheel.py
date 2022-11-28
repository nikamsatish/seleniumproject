
import time

from logging import info

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class Testone(BaseClass):
    '''@pytest.fixture(params=HomePageData.getTestData)
    def getData(self, request):
        return request.param'''
    def test_e2e(self):

        log = self.test_getloget()
        self.driver.implicitly_wait(100)

        # creat homepage object
        homePage = HomePage(self.driver)

        #click on honda icon
        homePage.gethonda().click()
        log.info("click on Honda check box")

        #Select less than 4 Lakh
        homePage.getdrop().select_by_visible_text("4 Lakh")
        log.info("less than 4 lakh bikes filter apply")

        #wait = WebDriverWait(self.driver, 30)
        #wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "strong"))
        time.sleep(7)

        #collect Honda List
        list=homePage.get_list()
        for i in list:
            print(i.text)
            assert "Honda" in i.text



       #collect price list 1
        list1 = homePage.get_list1()
        for j in list1:
            #print(j.text)
            #
            if "Lakh" in j.text:
                a = j.text.index("L") - 5
                b = j.text.index("L") - 1
                log.info(j.text[a:b] + " Lakh")
                if (float(j.text[a:b])<4):
                    assert (float(j.text[a:b]) < 4)

            else:
                #replace coma in between price eg.70,000-85,000
                if "-" in j.text:
                    log.info("Rs. " +j.text[13:19].replace(",", ""))
                    if (float(j.text[13:19].replace(",","")) < 400000):
                        assert (float(j.text[13:19].replace(",", "")) < 400000)

                #replace coma Rs.75,000
                else:
                    log.info("Rs. " +j.text[4:10].replace(",", ""))
                    if (float(j.text[4:10].replace(",", "")) < 400000):
                        assert (float(j.text[4:10].replace(",", "")) < 400000)

    def test_e2e2(self):

        log = self.test_getloget()

        homePage = HomePage(self.driver)

        homePage.gethonda().click()
        log.info("click on Honda check box")

        # Select less than 4Lakh
        homePage.getdrop().select_by_visible_text("4 Lakh")
        log.info("less than 4 lakh bikes filter apply")

        # wait = WebDriverWait(self.driver, 30)
        # wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "strong"))
        time.sleep(7)

        # collect Honda List
        list = homePage.get_list()
        for i in list:
            print(i.text)
            assert "hero" in i.text
            #self.driver.save_screenshot(r"C:\Users\Admin\zigwheels\screenshots\heroscreenshort.png")



        # collect list 1
        list1 = homePage.get_list1()
        for j in list1:
            # print(j.text)
            if "Lakh" in j.text:
                if (float(j.text) < 4):
                    assert (float(j.text) < 4)
                   # self.driver.save_screenshot(r"C:\Users\Admin\zigwheels\screenshots\img.png")

            else:
                if "-" in j.text:
                    log.info("Rs. " + j.text[13:19].replace(",", ""))
                    if (float(j.text[13:19].replace(",", "")) < 400000):
                        assert (float(j.text[13:19].replace(",", "")) < 400000)


                else:
                    log.info("Rs. " + j.text[4:10].replace(",", ""))
                    if (float(j.text[4:10].replace(",", "")) < 400000):
                        assert (float(j.text[4:10].replace(",", "")) < 400000)
