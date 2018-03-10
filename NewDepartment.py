from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


user_email_xpath = '//*[@id="user_email"]'
user_password_xpath = '//*[@id="user_password"]'
login_button_xpath = '//*[@id="new_user"]/div[2]/div[3]/button'
departments_button_xpath = '//div[2]/div[1]/ul[2]/li[3]/a'
all_departments_list_xpath = '//*[@id="pane2"]/div[2]/a'
create_department_button_xpath = '//*[@id="pane2"]/div[2]/a[1]'
department_title_textbox = '//*[@id="project_name"]'
department_code_textbox = '//*[@id="project_code"]'
department_url_textbox = '//*[@id="project_website"]'
department_description_textbox = '//*[@id="project_description"]'
department_managers_dropdown = '//*[@id="s2id_project_user_ids"]'
departments_managers_dropdown_teamlead = '//*[@id="select2-drop"]'
departments_save_button = '//*[@id="new_project"]/div[3]/div[2]/input'
fluxday_page_logo = '//*[@id="new_user"]/h2/div'
oath_applications_button = '//div[2]/div[1]/ul[2]/li[8]/a'
admin_button_xpath = '//div[2]/div[1]/ul[3]/li[1]/a'
create_department_info = '//*[@id="new_project"]/div[3]/div[1]'
managers_list = '//*[@id="select2-drop"]/ul/li'
team_lead_added_ = '//*[@id="s2id_project_user_ids"]/ul/li[1]/div'
department_title = '//*[@id="pane2"]/div[2]/a/div/div[2]/div[1]'

#create new Chrome session
driver = webdriver.Chrome()
driver.maximize_window()


#navigate to demo page
driver.get("http://demo.fluxday.io"), 'step1 --> Fail'
sleep(2)
page_demo = driver.find_element_by_xpath(fluxday_page_logo)
assert page_demo.is_displayed(), 'Step 1 --> Fail'


#log in as Admin
search_field = driver.find_element_by_xpath(user_email_xpath)
search_field.send_keys("admin@fluxday.io")
sleep(2)
search_field = driver.find_element_by_xpath(user_password_xpath)
search_field.send_keys("password")
sleep(1)
search_field = driver.find_element_by_xpath(login_button_xpath).click(), 'Step 2 --> Fail'
sleep(2)
assert driver.find_element_by_xpath(admin_button_xpath).text.find('Admin') > -1, 'Step 2 --> Fail'
assert driver.find_element_by_xpath(oath_applications_button).text.find('OAuth applications') > -1, 'Step 2 --> Fail'


#find and click on departments button
search_field = driver.find_element_by_xpath(departments_button_xpath).click(), 'Step 3 --> Fail'
sleep(2)
departments = driver.find_elements_by_xpath(all_departments_list_xpath)
assert len(departments) > 0

#find and click on create department button
search_field = driver.find_element_by_xpath(create_department_button_xpath).click(),
sleep(2)
assert driver.find_element_by_xpath(create_department_info).is_displayed() is True, 'Step 4 --> Fail'


#enter title 'Logistics'
search_field = driver.find_element_by_xpath(department_title_textbox).send_keys('Development'), 'Step 5 --> Fail'
sleep(2)
#enter code 'ENG'
search_field = driver.find_element_by_xpath(department_code_textbox).send_keys('ESP'), 'Step 6 --> Fail'
sleep(2)
# enter url 'demo.fluxday.io'
search_field = driver.find_element_by_xpath(department_url_textbox).send_keys('http://demo.fluxday.io'), 'Step 7 --> Fail'
sleep(2)
#enter description 'log'
search_field = driver.find_element_by_xpath(department_description_textbox).send_keys('dev'), 'Step 8 --> Fail'
sleep(2)
#find and click on mnagers drop-down menu
select_manager = driver.find_element_by_xpath(department_managers_dropdown)
select_manager.click()
sleep(1)
all_managers = driver.find_elements_by_xpath(managers_list)
assert len(all_managers) > 0, 'Step 9 --> Fail'

#choose Team Lead
search_field = driver.find_element_by_xpath(departments_managers_dropdown_teamlead).click()
sleep(2)
assert driver.find_element_by_xpath(team_lead_added_).is_displayed() is True, 'Step 10 --> Fail'


#click on 'Save' button
search_field = driver.find_element_by_xpath(departments_save_button).click()
sleep(3)
assert driver.find_element_by_xpath(department_title).text.find('Development'), 'Step 11 - >> Fail'

#close the window
driver.close()
