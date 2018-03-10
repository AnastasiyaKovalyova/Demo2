from selenium import webdriver
from time import sleep


user_email_xpath = '//*[@id="user_email"]'
user_password_xpath = '//*[@id="user_password"]'
login_button_xpath = '//*[@id="new_user"]/div[2]/div[3]/button'
users_button_xpath = '//div[2]/div[1]/ul[2]/li[5]/a'
all_users_xpath = '//*[@id="pane2"]/div[2]/div'
employee2_xpath = '//*[@id="pane2"]/div[2]/div[3]/div/div[2]/a[1]'
info_employee1_xpath = '//*[@id="pane3"]/div'
admin_button_xpath = '//div[2]/div[1]/ul[3]/li[1]/a'
user_settings_button_xpath = '//*[@id="pane3"]/div/div[1]/div[2]/a/div'
user_settings_delete_xpath = '//*[@id="drop1"]/li[2]/a'
oath_applications_button = '//div[2]/div[1]/ul[2]/li[8]/a'
employee_information_opened = '//*[@id="pane3"]/div/div[1]/div[4]/div'
fluxday_page_logo = '//*[@id="new_user"]/h2/div'
delete_edit_options = '//*[@id="drop1"]'
users_list = '//*[@id="pane2"]/div[2]/div'


#create new Chrome session
driver = webdriver.Chrome()
driver.maximize_window()


#navigate to demo page
browser = driver.get("http://demo.fluxday.io")
sleep(2)
page_demo = driver.find_element_by_xpath(fluxday_page_logo)
assert page_demo.is_displayed(), 'Step 1 --> Fail'


#log in as admin
search_field = driver.find_element_by_xpath(user_email_xpath)
search_field.send_keys("admin@fluxday.io")
sleep(2)
search_field = driver.find_element_by_xpath(user_password_xpath)
search_field.send_keys("password")
sleep(1)
search_field = driver.find_element_by_xpath(login_button_xpath).click()
sleep(2)
assert driver.find_element_by_xpath(admin_button_xpath).text.find('Admin') > -1, 'Step 2 --> Fail'
assert driver.find_element_by_xpath(oath_applications_button).text.find('OAuth applications') > -1, 'Step 2 --> Fail'


#find and click on Users button
search_field = driver.find_element_by_xpath(users_button_xpath).click()
sleep(1)
users = driver.find_elements_by_xpath(all_users_xpath)
assert len(users)> 0, 'Step 3 --> Fail'


#find and click on any user e.g 'Employee1'
users = driver.find_element_by_xpath(employee2_xpath).click()
sleep(1)
assert driver.find_element_by_xpath(info_employee1_xpath).is_displayed() is True, 'Not displayed'
assert driver.find_element_by_xpath(employee_information_opened).text.find('Employee 2') > -1, 'Step 4 --> Fail'


#find and click on 'Settings' button
search_field = driver.find_element_by_xpath(user_settings_button_xpath).click()
sleep(1)
assert driver.find_element_by_xpath(delete_edit_options).is_displayed() is True, 'Step 5 --> Fail'


#choose the 'Delete' option
search_field = driver.find_element_by_xpath(user_settings_delete_xpath).click()
sleep(2)
alert = driver.switch_to.alert
alert_message = driver.switch_to.alert.text.find('Are you sure you want to archive this employee?')
assert alert_message > -1, 'Step 6 --> Fail'


#accept the alert
alert.accept()
assert driver.find_element_by_xpath(employee2_xpath).text != 'Employee 2', 'Step 7 --> Fail'
sleep(3)
driver.close()
