# Script to sign in and compose an email on gmail
#Author: Aman Nirala | Social Handels: amanirala13

from selenium import webdriver                                                              #importing web drivers
from selenium.common.exceptions import NoSuchElementException
import time as TIME


FOUND_LOGIN_PAGE = True                                                                     #Flag to see if the user is logged in or not

browser = webdriver.Chrome('C:\\Users\\amann\\Downloads\\driver\\chromedriver')             #Opening chrome browser by creating instance of the driver. Pass the path of the driver file in the argument
browser.get('http://www.gmail.com')                                                         #Loading Gmail in the Chrome browser

def login_into_google(email, password):                                                     # Function to log into the gmail account

    NO_LOGIN_INTERRUPTION = True                                                            #Flag to see if the any exception takes place in login process

    try:
        elem = browser.find_element_by_id('identifierId')                                   #Finds the email/phone field on the login page
        elem.send_keys(email)                                                               #Sets the email/phone value in the field

        elem = browser.find_element_by_class_name('CwaK9').click()                          #Clicks the next button

        browser.implicitly_wait(5)                                                          #Standby for 5 sec to give time to the password frame to load

        elem = browser.find_element_by_name('password')                                     #Finds the password field on the login page
        elem.send_keys(password)                                                            #Sets the password value in the field

                                                                                            #In line 26: #Finds the Next button
        elem = browser.find_element_by_xpath("/html[@class='CMgTXc']/body[@id='yDmH0d']/div[@class='H2SoFe LZgQXe TFhTPc']/div[@id='initialView']/div[@class='xkfVF']/div[@id='view_container']/div[@class='zWl5kd']/div[@class='DRS7Fe bxPAYd k6Zj8d']/div[@class='pwWryf bxPAYd']/div[@class='Wxwduf Us7fWe JhUD8d']/div[@class='zQJV3']/div[@class='dG5hZc']/div[@class='qhFLie']/div[@id='passwordNext']/span[@class='CwaK9']")
        elem.click()                                                                        #Clicks the next button

        elem = browser.find_element_by_class_name("z0")                                     #Finds the compose button to create an exception and stop email sending process if login has failed for any reason

    except:
        print('>>>> Login failed!')                                                         #Login faliure message
        NO_LOGIN_INTERRUPTION = False                                                       #Updating the flag

    return NO_LOGIN_INTERRUPTION                                                            #returning the success/failure value


def compose_email():                                                                        #Function the sends the email

    email_to = input("\n Enter the recipient's email: ")                                     #Input the email of the recipient
    email_subject = input("\n Enter the Email Subject: ")                                   #Input the subject of the email
    email_body = input("\n Enter your message: ")                                           #Input the body of the email

    browser.implicitly_wait(5)                                                              #Go to standby for 5 sec to give time to the frames to load

    elem = browser.find_element_by_class_name("z0")                                         #Find the compose button
    elem.click()                                                                            #Click the compose button

    elem = browser.find_element_by_name('to')                                               #Find the recipient email field
    elem.send_keys(email_to)                                                                #Fill the field with the email input by the user

    elem = browser.find_element_by_name("subjectbox")                                       #Find the subject of the email field
    elem.send_keys(email_subject)                                                           #Fills in the field with the subject input by the user

    elem = browser.find_element_by_class_name("Am.Al.editable.LW-avf.tS-tW")                #Find the body of the email field
    elem.send_keys(email_body)                                                              #Fills in the field with the email body input by the user

    elem = browser.find_element_by_class_name('J-J5-Ji.btA')                                #Finds the Send button
    elem.click()                                                                            #Clicks the send button and sends the email

    TIME.sleep(5)                                                                           #Takes the code to stand by for 5 sec
    browser.quit()                                                                          #Quits the broswer before ending the program

try:
    elem = browser.find_element_by_id('identifierId')                                       #Checks if the user needs to be signed in by creating an exception
except:
     print("Login page not found")                                                          #Exception Created and the the user need not to be logged in, printing the message of the same
     FOUND_LOGIN_PAGE = False                                                               #Updating the flag

if FOUND_LOGIN_PAGE:                                                                        #Checking if we need to login or compose_email
    gmail_email = input("\n Enter your email for Gmail: ")                                  #We need to login, Input user's google email into which he/she wants to login
    gmail_password = input("\n Enter your password for Gmail:")                             #Input user's google account password into which he/she wants to login

    LOGIN_USER = login_into_google(email = gmail_email, password = gmail_password)          #Calling the login function

    if LOGIN_USER:                                                                          #Checking if login was successful
        compose_email();                                                                    #Login was successful, calling compose email function to send email

else:                                                                                       #If user is already loggedin
   print('No login found!')                                                                 #Show message
   compose_email                                                                            #Calling compose email function to send email
