
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):

    wait = WebDriverWait(self.driver, 10)
    self.vars["email"] = "testing@testing.com"
    self.vars["password"] = "testing"

    self.driver.get("https://getloanr.com/dashboard/loan-board/request")
    self.vars["isLogin"] = self.driver.find_element(By.CSS_SELECTOR, ".MuiTypography-root > p").text
    print("{}".format(self.vars["isLogin"]))
    self.driver.find_element(By.ID, "email").send_keys(self.vars["email"])
    self.driver.find_element(By.ID, "password").send_keys(self.vars["password"])
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type=\'submit\']")))
    button.click()
    time.sleep(6)
    self.driver.get("https://getloanr.com/dashboard/loan-board/request")
    while True:
        try:
            requestedAmount = int(input("Please enter amount. Request must be less than $1,000: "))
            if requestedAmount >= 0 and requestedAmount < 1001:
                break
            else:
                print("Request must be less than $1,000")
        except ValueError:
            print("Reques must be only number. Try again.")
    self.vars["requestedAmount"] = requestedAmount

    while True:
        try:
            payback = int(input("Please enter Payback amount, greater than or equal to requested amount: "))
            if payback >= requestedAmount:
                break
            else:
                print("Payback must be greater than or equal to requested amount")
        except ValueError:
            print("Payback must be only number. Try again.")
    self.vars["paybackAmount"] = payback  
    while True:
        try:
            date = input("Please enter date in format mm-dd-yyyy: ")
            if len(date) == 10:
                break
            else:
                print("Date must be in format mm-dd-yyyy")
        except ValueError:
            print("Date must be in format mm-dd-yyyy")
    self.vars["date"] = date
    while True:
        try:
            borrowerLocation = input("Please enter location: ")
            if len(borrowerLocation) > 0:
                break
            else:
                print("Location must be greater than 0 characters")
        except ValueError:
            print("Location must be greater than 0 characters")
    self.vars["borrowerLocation"] = borrowerLocation
    while True:
        try:
            titleColateral = input("Please enter Colateral title: ")
            if len(titleColateral) > 0:
                break
            else:
                print("Title must be greater than 0 characters")
        except ValueError:
            print("Title must be greater than 0 characters")
    self.vars["titleColateral"] = titleColateral
    while True:
        try:
            descriptionColateral = input("Please enter description, min. length 10 characters: ")
            if len(descriptionColateral) > 9:
                break
            else:
                print("Description must be greater than 10 characters")
        except ValueError:
            print("Description must be greater than 0 characters")
    self.vars["descriptionColateral"] = descriptionColateral
    options = {
    "A": "Cameras & Photo",
    "B": "Cell Phones & Accessories",
    "C": "Collectibles",
    "D": "Computers/Tablets",
    "E": "Consumer Electronics",
    "F": "Jewelry & Watches",
    "G": "Musical Instruments & Gear",
    "H": "Rent",
    "I": "Tools/Equipment",
    "J": "Video Games & Consoles",
    "K": "Other"}

    while True:
        print("Please select a category: ")
        for key, value in options.items():
            print(f"{key}: {value}")
        category = input("Please enter category: ")
        if category.upper() in options:
            categoryColateral = options[category.upper()]
            break
        else:
            print("Please enter a valid category")
    self.vars["categoryColateral"] = categoryColateral            
    while True:
        try:
            fullName = input("Please enter full name: ")
            if len(fullName) > 0:
                break
            else:
                print("Please enter a valid name")
        except ValueError:
            print("Please enter a valid name")
    self.vars["fullName"] = fullName

    button22 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-1b401o0")))
    button22.click()
    self.driver.find_element(By.ID, "requestedAmount").send_keys(self.vars["requestedAmount"])

    self.driver.find_element(By.ID, "paybackAmount").send_keys(self.vars["paybackAmount"])
    self.driver.find_element(By.ID, "date").send_keys(self.vars["date"])
    self.driver.find_element(By.ID, "borrowerLocation").send_keys(self.vars["borrowerLocation"])
    self.driver.find_element(By.XPATH, "//div[@id=\'collateral\']/div/div/button").click()
    self.driver.find_element(By.ID, "title").send_keys(self.vars["titleColateral"])
    self.driver.find_element(By.ID, "description").send_keys(self.vars["descriptionColateral"])
    self.driver.find_element(By.ID, "mui-component-select-category").click()
    self.driver.find_element(By.XPATH, f"//li[contains(.,'{self.vars['categoryColateral']}')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedPrimary").click()
    self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#mui-4").send_keys(self.vars["fullName"])
    self.driver.find_element(By.XPATH, "//input[@type=\'checkbox\']").click()
    self.driver.find_element(By.XPATH, "//button[contains(.,'Confirm')]").click()
    print("Success")
    '''
     else:
      self.driver.find_element(By.ID, "requestedAmount").send_keys(self.vars["requestedAmount"])
      self.driver.find_element(By.ID, "paybackAmount").send_keys(self.vars["paybackAmount"])
      self.driver.find_element(By.ID, "date").send_keys(self.vars["date"])
      self.driver.find_element(By.ID, "borrowerLocation").send_keys(self.vars["borrowerLocation"])
      self.driver.find_element(By.XPATH, "//div[@id=\'collateral\']/div/div/button").click()
      self.driver.find_element(By.ID, "title").send_keys(self.vars["titleColateral"])
      self.driver.find_element(By.ID, "description").send_keys(self.vars["descriptionColateral"])
      self.driver.find_element(By.ID, "mui-component-select-category").click()
      self.driver.find_element(By.XPATH, "//li[contains(.,\'self.vars[\"categoryColateral\"]\')]").click()
      self.driver.find_element(By.XPATH, "//div[@id=\'collateral-form\']/div/div[8]/button[2]").click()
      self.driver.find_element(By.XPATH, "//button[contains(.,\'Publish Request\')]").click()
      self.driver.find_element(By.XPATH, "//div[2]/div[3]/div/div/input").send_keys(self.vars["fullName"])
      self.driver.find_element(By.XPATH, "//input[@type=\'checkbox\']").click()
      self.driver.find_element(By.XPATH, "(//button[@type=\'button\'])[15]").click()
      print("Success") >>>
  '''
if __name__ == "__main__":
  test = TestLogin()
  test.test_login()
