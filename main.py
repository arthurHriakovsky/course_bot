import time
from datetime import datetime
import constants
import selenium_util


def main():
    start_hour = 22
    end_hour = 7
    curr_hour = int(datetime.now().time().hour)
    while curr_hour < start_hour:
        curr_hour = int(datetime.now().time().hour)
        time.sleep(30)

    driver = None
    try:
        driver = selenium_util.connect_to_portal()
        selenium_util.login_to_portal(driver)
        time.sleep(20)
        print(curr_hour)

        #registration
        selenium_util.click_registration(driver)
        time.sleep(10)

        #semester
        selenium_util.click_semester_reg(driver, constants.SEMESTER)
        time.sleep(5)
                
        for course_index,course_num in enumerate(constants.COURSES):
            selenium_util.click_another(driver, course_num)
            time.sleep(2)
                
        driver.find_element_by_id("aaaa.ModuleBasketView.NextButton").click()
        time.sleep(5)
            
        while (curr_hour < end_hour) or (curr_hour >= start_hour):
            for course_index,course_num in enumerate(constants.COURSES):

                driver.find_element_by_id("aaaa.EventsView.short_sm_0_0_editor."+ str(course_index)).click()
                time.sleep(0.5)
                selenium_util.try_reg_to_course(driver)
    

        time.sleep(15)
    finally:
        selenium_util.close_portal(driver)
        

if __name__ == '__main__':
    main()

