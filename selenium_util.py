import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import constants


def connect_to_portal():
    options = Options()
    options.binary_location = r"C:\Users\Arthu\AppData\Local\Google\Chrome\Application\chrome.exe" 
    driver = webdriver.Chrome(executable_path="D:\\downloads\\Vacancy-Finder-main\\chromedriver.exe", options=options)
    driver = webdriver.Chrome(options=options)
    driver.get(constants.PORTAL_URL)
    return driver


def close_portal(driver):
    if driver is not None:
        driver.close()


def login_to_portal(driver):
    username_field = driver.find_element_by_id('Ecom_User_ID')
    username_field.send_keys(constants.USERNAME)

    password_field = driver.find_element_by_id('Ecom_Password')
    password_field.send_keys(constants.PASSWORD)

    password_field.send_keys(Keys.RETURN)


def click_registration(driver):
    registration_iframe = driver.find_element_by_id("contentAreaFrame")
    driver.switch_to.frame(registration_iframe)

    xpath = "//div[4]//ul[1]//li[3]//a[1]"
    registration_button = driver.find_element_by_xpath(xpath)
    registration_button.click()


def click_semester_reg(driver, semester_num):
    semester_iframe = driver.find_element_by_id("isolatedWorkArea")
    driver.switch_to.frame(semester_iframe)

    semester_id = f"aaaa.ProgramView.BookingButton.{semester_num}"
    semester_button = driver.find_element_by_id(semester_id)
    semester_button.click()


def click_course_reg(driver, course_num):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_id("contentAreaFrame"))
    driver.switch_to.frame(driver.find_element_by_id("isolatedWorkArea"))

    course_field = driver.find_element_by_id("aaaa.ModuleBasketView.short_smInp")
    course_field.clear()
    course_field.send_keys(course_num)
    course_field.send_keys(Keys.RETURN)

    time.sleep(2)

    course_checkbox = driver.find_element_by_id("aaaa.ModuleBasketView.Choose.0")
    course_checkbox.click()

    time.sleep(2)

    driver.find_element_by_id("aaaa.ModuleBasketView.NextButton").click()
    
def click_another(driver, course_num):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_id("contentAreaFrame"))
    driver.switch_to.frame(driver.find_element_by_id("isolatedWorkArea"))

    course_field = driver.find_element_by_id("aaaa.ModuleBasketView.short_smInp")
    course_field.clear()
    course_field.send_keys(course_num)
    course_field.send_keys(Keys.RETURN)
    
    time.sleep(2)
    course_checkbox = driver.find_element_by_id("aaaa.ModuleBasketView.Choose.0")
    course_checkbox.click()
    time.sleep(2)

def try_reg_to_course_another(driver,num):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_id("contentAreaFrame"))
    driver.switch_to.frame(driver.find_element_by_id("isolatedWorkArea"))

    # check if course is free
    driver.find_element_by_id("aaaa.EventsView.short_sm_0_0_editor."+ str(num)).click()
    time.sleep(2)
    free_spaces = driver.find_element_by_id("aaaa.EventPackageSelectionView.se_freeCap_0_editor.0").text
    if free_spaces != "0":
        print("Found Space!!!")
        driver.find_element_by_id("aaaa.EventPackageSelectionView.bookingButton").click()

        time.sleep(2)

        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_id("URLSPW-0"))

        time.sleep(2)

        driver.find_element_by_id("aaaa.RegistrationErrorView.exitButton").click()

        time.sleep(2)

        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_id("contentAreaFrame"))
        driver.switch_to.frame(driver.find_element_by_id("isolatedWorkArea"))

    time.sleep(2)

    course_checkbox = driver.find_element_by_id("aaaa.ModuleBasketView.Choose.0")
    course_checkbox.click()
    time.sleep(2)

    # in either case, return back
    #driver.find_element_by_id("aaaa.EventsView.BackButton").click()

def try_reg_to_course(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_id("contentAreaFrame"))
    driver.switch_to.frame(driver.find_element_by_id("isolatedWorkArea"))

    # check if course is free
    free = driver.find_element_by_id("aaaa.EventPackageSelectionView.se_freeCap_0_editor.1").text
    free_spaces = driver.find_element_by_id("aaaa.EventPackageSelectionView.se_freeCap_0_editor.0").text
    if free_spaces != "0" or free!= "0":
        print("Found Space!!!")
        driver.find_element_by_id("aaaa.EventPackageSelectionView.bookingButton").click()
        
        time.sleep(2)

        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_id("URLSPW-0"))

        time.sleep(2)

        driver.find_element_by_id("aaaa.RegistrationErrorView.exitButton").click()

        time.sleep(2)

        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_id("contentAreaFrame"))
        driver.switch_to.frame(driver.find_element_by_id("isolatedWorkArea"))

    time.sleep(2)

    # in either case, return back
    #driver.find_element_by_id("aaaa.EventsView.BackButton").click()


def uncheck_first_checkbox(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_id("contentAreaFrame"))
    driver.switch_to.frame(driver.find_element_by_id("isolatedWorkArea"))

    time.sleep(2)

    course_checkbox = driver.find_element_by_id("aaaa.ModuleBasketView.Choose.0")
    course_checkbox.click()


def print_all_text(driver):
    print(driver.find_element_by_xpath("/html/body").text)
