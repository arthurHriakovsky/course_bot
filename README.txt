1. Install selenium library
2. Install Chreome driver
3. Install Gecko driver
4. For Google Chrome using you need to delete your Chrome verion and install 93.0.4577.63 version.
5. In constants.py to change USERNAME, PASSWORD, SEMESTER (1 for ב and 0 for א), (if you have english course - add 3 to semester number), and COURSES
6. In selenium_util.connect_to_portal change options.binary_location to your Chrome version (93.0.4577.63) exe file
7. In selenium_util.connect_to_portal change driver = webdriver.Chrome(executable_path = "path to chrome driver file") - this file should be in the directory folder
8. change registration hours in main.py
9. 