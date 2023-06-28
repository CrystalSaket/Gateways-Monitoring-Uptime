from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def loop():
    while True:
        continue

def getScreenshots():
    driver = webdriver.Edge()
    
    driver.get("https://intelli-device.apdcl.co/")
    driver.fullscreen_window()
    # driver.execute_script("document.body.style.zoom='70%'")
    # driver.execute_script("document.body.style.zoom='50%'")
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"login_email").send_keys("saket.jasuja@crystalpower.in" + Keys.ENTER)
    driver.find_element(By.ID,"login_password").send_keys("DbnbYWNTm#" + Keys.ENTER)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div[2]/div/button").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div/div[1]/nav/div[1]/a[5]").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div[1]/div[2]/div/button").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[1]/i").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/span").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/i").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/span").click()
    driver.implicitly_wait(10)
    # driver.implicitly_wait(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/span").click()
    driver.implicitly_wait(10)
    # driver.implicitly_wait(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/span").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[2]").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div/div[2]/div[2]/div/button").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/i").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[2]/div[4]/span").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[2]").click()
    driver.implicitly_wait(10)
    
    # elements = driver.find_elements(By.TAG_NAME,"tr")
    i = 0
    k = 1
    # driver.execute_script("document.body.style.zoom='70%'")
    while i <= 10:
        # driver.execute_script("document.body.style.zoom='70%'")
        if i == 10 and k == 16:
            break
        elif i == 10:
            i = 1
            k = k + 1
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[1]/div/a[9]").click()
            driver.implicitly_wait(10)
        else:
            i = i + 1
        filename = driver.find_element(By.XPATH,"/html/body/div/div[2]/table/tbody/tr[{}]/td[2]/a".format(i)).text
        uptime_percent = driver.find_element(By.XPATH,"/html/body/div/div[2]/table/tbody/tr[{}]/td[3]/div/div[2]".format(i)).text
        uptime_percent = uptime_percent.removesuffix(" %")
        if filename.find("Test",0,4) == 0 or filename.find("TEST",0,4) == 0:
            continue
        if int(uptime_percent) <= 95:
            print(filename)
            
            # path = "/html/body/div/div[2]/table/tbody/tr[{}]/td[2]".format(i)
            path = "/html/body/div/div[2]/table/tbody/tr[{}]/td[2]/a".format(i)
            print(path)
            j = 1
            while j <= 10000000:
                j = j + 1

            driver.find_element(By.XPATH,path).click()
            # driver.execute_script("document.body.style.zoom='70%'")
            # driver.execute_script("arguments[0].click();", button)
            driver.implicitly_wait(10)
            j = 1
            while j <= 10000000:
                j = j + 1
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/a[2]").click()
            # driver.execute_script("document.body.style.zoom='70%'")
            # driver.execute_script("arguments[1].click();", button)
            driver.implicitly_wait(10)
            # driver.implicitly_wait(100)/

            j = 1
            while j <= 10000000:
                j = j + 1
            # action = ActionChains(driver)

            # driver.set_window_size(1810,1500)
            driver.execute_script("document.body.style.zoom='70%'")
            driver.implicitly_wait(2)
            driver.save_screenshot(filename="C:\\Users\\Sinhal Udyog\\Excel Automation\\IntelliSmart\\Uptime 21 March 2023" + "\\" + filename + ".png")
            driver.implicitly_wait(10)
            driver.execute_script("document.body.style.zoom='100%'")
            driver.implicitly_wait(10)
            driver.back()
            driver.implicitly_wait(10)
            driver.back()
            driver.implicitly_wait(10)
            for k2 in range(1,k):
                driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[1]/div/a[9]").click()
                j = 1
                while j <= 10000000:
                    j = j + 1
            # j = 1
            # while j <= 30000000:
            #     j = j + 1
        # i = i + 1
getScreenshots()