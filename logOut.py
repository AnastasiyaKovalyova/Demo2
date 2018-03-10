from selenium import webdriver
from time import sleep

fluxday_page_logo = '//*[@id="new_user"]/h2/div'
user_email_xpath = '//*[@id="user_email"]'
user_password_xpath = '//*[@id="user_password"]'
login_button_xpath = '//*[@id="new_user"]/div[2]/div[3]/button'
logout_button_xpath = '//div[2]/div[1]/ul[3]/li[2]/a'
admin_button_xpath = '//div[2]/div[1]/ul[3]/li[1]/a'
oath_applications_button = '//div[2]/div[1]/ul[2]/li[8]/a'


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

#find and click on log out button
search_field = driver.find_element_by_xpath(logout_button_xpath).click()
sleep(2)
assert driver.find_element_by_xpath(fluxday_page_logo).is_displayed(), 'Step 3 --> Fail'
sleep(1)
driver.close(), 'Close Failed'

