from selenium import webdriver

email = input('\nEnter your facebook email')
password = input('\nEnter your facebook password')

browser = webdriver.Chrome("C:\\Users\\amann\\Downloads\\driver\\chromedriver")
browser.get('http://www.facebook.com')

elem = browser.find_element_by_id('email')
elem.send_keys(email)

elem = browser.find_element_by_id('pass')
elem.send_keys(password)

elem = browser.find_element_by_id('loginbutton')
elem.click()
