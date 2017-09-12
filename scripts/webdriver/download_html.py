from selenium import webdriver
import time



driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

email = driver.find_element_by_xpath('//*[@id="wpName1"]')
email.send_keys('kabardi.cat@gmail.com')

password = driver.find_element_by_xpath('//*[@id="wpPassword1"]')
password.send_keys('E3pqArtPyCat')

sign_in = driver.find_element_by_xpath('//*[@id="u_0_t"]')
sign_in.click()

time.sleep(5)

friends = driver.find_elements_by_class_name("fsl")

for friend in friends:
    print(driver.find_elements_by_class_name("js_ja"))

driver.quit()