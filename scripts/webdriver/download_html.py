from selenium import webdriver
import time



driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('kabardi.cat@gmail.com')

password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('iamarockstar')

sign_in = driver.find_element_by_xpath('//*[@id="u_0_t"]')
sign_in.click()

time.sleep(5)

driver.quit()