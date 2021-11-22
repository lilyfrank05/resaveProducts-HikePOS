from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import load_workbook
import time


account = input('Please enter the Hike account ID: ')
username = input('Please enter the Hike username: ')
password = input('Please enter the password: ')
filePath = input("Where's the file? ")

driver = webdriver.Chrome(ChromeDriverManager().install())
# Log into the store and navigate to the product listing page
driver.get("https://my.hikeup.com/")
driver.set_window_size(1920, 1080)
driver.find_element(By.NAME, "tenancyName").send_keys(account)
driver.find_element(By.NAME, "usernameOrEmailAddress").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/button[1]").click()
wait = WebDriverWait(driver, 20)
element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                       '/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')))
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[11]/a[1]").click()
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[11]/ul[1]/li[1]/a[1]").click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                       '/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')))


def resave_product(sku):
    #filter for the product by SKU
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").click()
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
        sku)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                           '/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[2]/li[1]/a[1]')))
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[2]/li[1]/a[1]").click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                           '/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/span[1]')))
    #click into the product profile
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/span[1]").click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                           '/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/input[1]')))
    time.sleep(3)
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[2]/div[3]/div[2]/div[1]/div[2]")).perform()
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/button[2]/span[1]").click()
    #clear the filter
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                           '/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/a[1]/i[1]')))
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/a[1]/i[1]").click()
    time.sleep(5)

#read SKU List from the file
wb = load_workbook(filePath)
ws = wb.active
column = ws['A']
skuList = [column[x].value for x in range(len(column))]
#resave the products
for sku in skuList:
    resave_product(sku)
    print(sku)

driver.close()