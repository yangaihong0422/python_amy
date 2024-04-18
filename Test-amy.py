from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/login")
try:
    element = driver.find_element("name",'commit')
    element.click()
    print("successfully log in")

except:
    print("login is failed")
    driver.quit()

#Entering in credentials
driver.find_element("id",'login_field').send_keys("yangaihong0422")
driver.find_element("id",'password').send_keys("123")
