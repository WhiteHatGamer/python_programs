from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #check for usage
import csv
import os
from string import digits, punctuation
import traceback

file_path = os.path.dirname(__file__)

#adding last name for understanding from which company this contacts are from
COMPANY = "College"

try:
    #get default profile from chrome
    profile = Options()

    ##maxim = webdriver.ChromeOptions()
    profile.add_argument(f'user-data-dir=C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data')
    profile.add_argument("--profile-directory=Profile 1")
    #initialise browser
    BrowserService = Service(executable_path='chromedriver.exe')

    driver = WebDriver(service= BrowserService, options=profile)

    #mail.google.com
    toTextXPath = '//*[@id=":17k"]'
    imgXPath = '//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div[4]/c-wiz/div/div/div/div/div/span/div[1]/div[1]/div/img'
    composeButtonXPath = '/html/body/div[8]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div'

    #contacts.google.com #old XPATH Commented for reference
    fnameXPath = '//*[@id="c21"]' #"//*[@id='c0']/div[2]/div[1]/div/div[1]/div/div[1]/input"
    lnameXPath = '//*[@id="c29"]' #"//*[@id='c0']/div[2]/div[3]/div/div[1]/div/div[1]/input"
    saveButton = '//*[@id="yDmH0d"]/c-wiz/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[2]/button'
    noteXPath = '//*[@id="c175"]/div/label' #//*[@id="c14"]/div/div[1]/div[2]/textarea'
    emailXPath = '//*[@id="c77"]' #"//*[@id='c4']/div[1]/div[1]/div/div[1]/input"
    dpXPath = '//*[@id="yDmH0d"]/c-wiz/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/button/span/div/i'

    #looping through to get mails
    count = 0
    with open(file_path+'\Mail.txt', 'r') as file:
        mails = file.readlines()
    csv_file = open(file_path+'\contact.csv','a')
    contacts_writer = csv.writer(csv_file)
    for mail in mails: #O(2n) because of removing numbers from emailid for only name
        mail = mail.replace('\n','')
        #for those mail with no user --> email id not correct
        driver.get('https://contacts.google.com/new')

        #Getting Mail and saveable Name From String
        if '<' in mail:
            email_list = mail.replace('>','<').split('<')
            email = email_list[1]
            namelist = email_list[0].split('@')
            name = ""
            for i in namelist[0]:
                if i in digits:
                    continue
                if i in punctuation:
                    name += " "
                    continue
                name += i
            name = name.strip()
        elif ',' in mail:
            email_list = mail.split(',')
            email = email_list[0]
            namelist = email.split('@')
            name = ""
            for i in namelist[0]:
                if i in digits:
                    continue
                if i in punctuation:
                    name += " "
                    continue
                name += i
            name = name.strip()
        else:
            email = mail
            namelist = email.split('@')
            name = ""
            for i in namelist[0]:
                if i in digits:
                    continue
                if i in punctuation:
                    name += " "
                    continue
                name += i
            name = name.strip()
        #entering mail in text boxes
        driver.find_element(By.XPATH, fnameXPath).send_keys(name)
        driver.find_element(By.XPATH, lnameXPath).send_keys(COMPANY)
        driver.find_element(By.XPATH, emailXPath).send_keys(email)
        driver.find_element(By.XPATH, noteXPath).send_keys("This is Selenium Generated Contact")
        driver.find_element(By.XPATH, saveButton).click()
        contacts_writer.writerow([name,email])
        count += 1
    
    #Quit Driver
    driver.quit()

    #close File
    csv_file.close()

    print(f'Total {count} contacts Added')
except:
    print("Exception Occured: ")
    traceback.print_exc()