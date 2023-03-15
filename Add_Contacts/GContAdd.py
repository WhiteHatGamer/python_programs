from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #check for usage
import traceback
from time import sleep

numbers = ['0','1','2','3','4','5','6','7','8','9']

try:
    #get default profile from chrome
    profile = Options()

    ##maxim = webdriver.ChromeOptions()
    profile.add_argument('user-data-dir=C:\\Users\\Thahir\\AppData\\Local\\Google\\Chrome\\User Data')
    profile.add_argument("--profile-directory=Profile 1")

    #initialise browser
    BrowserService = Service(executable_path='chromedriver.exe')

    driver = WebDriver(service= BrowserService, options=profile)

    #mail.google.com
    toTextXPath = '//*[@id=":17k"]'
    imgXPath = '//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div[4]/c-wiz/div/div/div/div/div/span/div[1]/div[1]/div/img'
    composeButtonXPath = '/html/body/div[8]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div'

    #contacts.google.com
    fnameXPath = "//*[@id='c0']/div[2]/div[1]/div/div[1]/div/div[1]/input"
    lnameXPath = "//*[@id='c0']/div[2]/div[3]/div/div[1]/div/div[1]/input"
    saveButton = '//*[@id="yDmH0d"]/c-wiz/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[2]/button'
    noteXPath = '//*[@id="c14"]/div/div[1]/div[2]/textarea'
    emailXPath = "//*[@id='c4']/div[1]/div[1]/div/div[1]/input"
    dpXPath = '//*[@id="yDmH0d"]/c-wiz/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/button/span/div/i' 

    #looping through to get mails
    count = 0
    mails = open('Add_Contacts\Mail.txt', 'r')
    #contacts = open('Add_Contacts\contact.txt', 'w')
    for mail in mails:
        driver.get('https://contacts.google.com/new')
        email = mail.split('"')
        namelist = email[1].split('@')
        name = ""
        for i in namelist[0]:
            if i not in numbers:
                name+=i

        #entering mail in text boxes
        driver.find_element(By.XPATH, fnameXPath).send_keys(name)
        driver.find_element(By.XPATH, lnameXPath).send_keys("ASAP")
        driver.find_element(By.XPATH, emailXPath).send_keys(email[1])
        driver.find_element(By.XPATH, noteXPath).send_keys("This is Selenium Generated Contact")
        driver.find_element(By.XPATH, saveButton).click()
        #contacts.write(f"Name: {name} Email: {email[1]}\n")
        count += 1
    
    #Quit Driver
    driver.quit()

    #close File
    mails.close()
    #contacts.close()

    print(f'Total {count} contacts Added')
except:
    print("Exception Occured: ")
    traceback.print_exc()