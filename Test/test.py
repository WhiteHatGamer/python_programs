#mails = open('Mail.txt', 'r')
#numbers = ['0','1','2','3','4','5','6','7','8','9']
#for mail in mails:
#    email = mail.split('"')
#    namelist = email[1].split('@')
#    name = ""
#    for i in namelist[0]:
#        if i not in numbers:
#            name+=i
#    print('Email: ' + email[1])
#    print('Name: ' + name)
#mails.close()
#from selenium import webdriver
#from time import sleep
#
##profile
#profile = webdriver.ChromeOptions()
##maxim = webdriver.ChromeOptions()
##maxim.add_argument("start_maximized")
##inilialize
#driver = webdriver.Chrome(executable_path="chromedriver.exe", options=profile)
#
#profile.add_argument('user-data-dir=<Paste user data of chrome here without angle brackets>')
#profile.add_argument("--profile-directory=Default")
#
#driver.set_page_load_timeout(30)
#driver.get(r'https://www.facebook.com/')
#driver.maximize_window()
#sleep(50)
#driver.quit()

"""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

profile = Options()
profile.add_argument('user-data-dir=<Paste user data of chrome here without angle brackets>')
profile.add_argument("--profile-directory=Profile 1")
profile.add_argument("--disable-dev-shm-usage")
profile.add_argument("--no-sandbox")
BrowserService = Service(executable_path='chromedriver.exe')
driver = WebDriver(service = BrowserService, options = profile)

driver.get("https://www.instagram.com")
"""
"""l1 = [12,34,352,5,54,45]
print([i for i in l1])"""

"""from math import sqrt,floor
def prime_n(number):
    #doing sqrt method
    for n in range(2,number):
        for x in range(2,floor(sqrt(n))):
            if(n%x == 0):
                #here n is not a prime
                break
        else:
            print(f"{n} is a prime")

prime_n(1000)"""
flag = True
while flag == True:
    try:
        n1 = input("ENter first number: ")
        n2 = input("Enter secind nmber: ")
        print(f"dicvisoin : {n1/n2}")
        flag = False
    except:
        print("Zero diciiosn error")
    else:
        print("Thankyou for choosing The Program")
