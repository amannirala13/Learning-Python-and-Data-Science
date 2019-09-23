#Automation of facebook login process using Selenium for Google Chrome Web Browser

from selenium import webdriver                      #import library

driver_path = input('\nEnter the path of the chrome driver: ')
email = input('\nEnter your facebook email: ')
password = input('\nEnter your facebook password: ')

browser = webdriver.Chrome(driver_path)             #Launches Chrome in automation test mode
browser.get('http://www.facebook.com')              #Loads facebook website in Chrome

elem = browser.find_element_by_id('email')          #Finds the email feild using its HTML id
elem.send_keys(email)                               #Sets the email that the user input to the email textfield

elem = browser.find_element_by_id('pass')           #Finds the password feild using its HTML id
elem.send_keys(password)                            #Sets the password that the user input to the password textfield

elem = browser.find_element_by_id('loginbutton')    #Finds the login button using its HTML id
elem.click()                                        # Clicks the login button
