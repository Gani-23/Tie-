import selenium 
import time 
from selenium import webdriver 
import selenium.webdriver.common.keys as Keys
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import pynput
from pynput.mouse import Button, Controller
mouse = Controller



opt = webdriver.ChromeOptions()
opt.add_argument("--disable-infobars")
opt.add_argument(" --disable-notifications")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
opt.add_argument("no-sandbox")
opt.add_argument("--disable-gpu")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--disable-xss-auditor")
opt.add_argument("--disable-web-security")
opt.add_argument("--allow-running-insecure-content")
opt.add_argument("--disable-setuid-sandbox")
opt.add_argument("--disable-webgl")
opt.add_argument("--disable-popup-blocking")



driver = webdriver.Chrome(chrome_options=opt)
driver.get('https://takeiteasyengineers.com/')
driver.maximize_window()
time.sleep(3)
print("Make a choice")
print("NOTE : CHOOSE BRANCH NAMES AND GIVE INPUT OF BRANCH NAME PROVIDED BELOW (CASE SENSITIVE) ")
print("options availabe \n1.cse \n2.science \n3.eee \n4.ece \n5.mech \n6.civil \n7.maths \n8.query")
a = input()
if(a=='query'):
    search = driver.find_element_by_xpath("//a[@aria-label='Search']//*[name()='svg']").click()
    nquery = input()
    squeries = driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(nquery)
    driver.find_element_by_xpath("//button[@aria-label='Search button']").click()


elif(a == 'science'):
        sce = driver.find_element_by_xpath('//*[@id="post-563"]/div/div/div/div/section/div/div/div/div/div/section[1]/div/div/div[1]/div/div/div/div/div/a/img')
        sce.click()
        time.sleep(3)
        try:
            keyboard.press('esc')
        finally:
            print("check Contents")


elif(a == 'cse'):
        cse = driver.find_element_by_xpath('//*[@id="post-563"]/div/div/div/div/section/div/div/div/div/div/section[1]/div/div/div[2]/div/div/div/div/div/a/img')
        cse.click()
        time.sleep(3)
        try:
            keyboard.press('esc')
        finally:
            print("check Contents")

elif(a == 'eee'):
    elec = driver.find_element_by_xpath('//*[@id="post-563"]/div/div/div/div/section/div/div/div/div/div/section[4]/div/div/div/div/div/div/div/div/a/img')
    elec.click()
    time.sleep(3)
    try:
        keyboard.press('esc')
    finally:
            print("check Contents")

elif(a == 'ece'):
    ecee = driver.find_element_by_xpath('//*[@id="post-563"]/div/div/div/div/section/div/div/div/div/div/section[2]/div/div/div[1]/div/div/div/div/div/a/img')
    ecee.click()
    time.sleep(3)
    try:
        keyboard.press('esc')
    finally:
            print("check Contents")

elif(a == 'mech'):
        mecha = driver.find_element_by_xpath('//*[@id="post-563"]/div/div/div/div/section/div/div/div/div/div/section[2]/div/div/div[2]/div/div/div/div/div/a/img')
        mecha.click()
        time.sleep(3)
        try:
            keyboard.press('esc')
        finally:
            print("check Contents")

elif(a == 'civil'):
        civ = driver.find_element_by_xpath('//*[@id="post-563"]/div/div/div/div/section/div/div/div/div/div/section[3]/div/div/div[1]/div/div/div/div/div/a/img')
        civ.click()
        time.sleep(3)
        try:
            keyboard.press('esc')
        finally:
            print("check Contents")

elif(a == 'maths'):
        math = driver.find_element_by_xpath('//*[@id="post-563"]/div/div/div/div/section/div/div/div/div/div/section[3]/div/div/div[2]/div/div/div/div/div/a/img')
        math.click()
        time.sleep(3)
        try:
            keyboard.press('esc')
        finally:
            print("check Contents")
else:
    driver.close()



