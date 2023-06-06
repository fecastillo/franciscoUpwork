import time
import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestCreateUser():
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
  
  def test_createUser(self):
    self.driver.get("https://getloanr.com/sign-up")
    while True:
        try:
            self.vars["name"] = input("Please enter your name: ")
            if self.vars["name"] != "":
                break
            else:
                print("Name cannot be empty")
        except ValueError:
            print("Name cannot be empty")

    while True:
        try:
            nameUser = input("Please enter your username. Min. length - 3 chars. Max Length 10: ")
            if len(nameUser) >= 3 and len(nameUser) <= 10:
                break
            else:
                print("Username must be between 3 and 10 chars")
        except ValueError:
            print("Username must be between 3 and 10 chars")
    self.vars["username"] = nameUser
    email_regex = r"[^@]+@[^@]+\.[^@]+"

    while True:
      email = input("Please enter your email: ")
      if re.match(email_regex, email):
        break
    else:
        print("Invalid email. Please try again.")
    self.vars["email"] = email
    while True:
        try:
            phone = input("Please enter phone. Min 10 chars: ")
            if len(phone) >= 10:
                break
            else:
                print("Please enter phone. Min 10 chars")
        except ValueError:
            print("Please enter phone. Min 10 chars")
    self.vars["phone"] = phone
    while True:
        try:
            password = input("Please enter password. Min 4 chars: ")
            if len(password) >= 4:
                break
            else:
                print("Please enter password. Min 4 chars")
        except ValueError:
            print("Please enter password. Min 8 chars")
    self.vars["password"] = password
    self.driver.find_element(By.ID, "name").send_keys(self.vars["name"])
    self.driver.find_element(By.ID, "username").send_keys(self.vars["username"])
    self.driver.find_element(By.ID, "email").send_keys(self.vars["email"])
    self.driver.find_element(By.ID, "phone-input").send_keys(self.vars["phone"])
    self.driver.find_element(By.ID, "password").send_keys(self.vars["password"])
    self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    optionsId = {
       "A" : "Id card",
        "B" : "Passport"
    }
    while True:
        print("Please select your ID type: ")
        for key, value in optionsId.items():
            print(f"{key}: {value}")
        idType = input("Please enter your ID type: ")
        if idType.upper() in optionsId.keys():
            break
        else:
            print("Please select a valid option")
    self.vars["id_type"] = optionsId[idType.upper()]

    if self.driver.execute_script("return (arguments[0] == \"Id card\")", self.vars["id_type"]):
      while True:
        try:
            idCard = input("Please enter your ID card number: ")
            if len(idCard) >= 1:
                break
            else:
                print("Please enter your ID card number.")
        except ValueError:
            print("Please enter your ID card number.")

      self.vars["idCard"] = idCard
      self.driver.find_element(By.XPATH, "//label[1]/span/input").click()
      self.driver.find_element(By.ID, "number").send_keys(self.vars["idCard"])
      self.driver.find_element(By.ID, "policy").click()
      self.driver.find_element(By.XPATH, "(//button[@type=\'submit\'])[2]").click()
      print("Successfully created user.")
    else:
      while True:
          country = input("Please enter your country: ")
          if country != "":
              break
          else:
              print("Please enter your country")
      self.vars["country"] = country.title()
      while True:
        try:
            passportId = input("Please enter your Passport ID number: ")
            if len(passportId) >= 1:
                break
            else:
                print("Please enter your Passport ID number.")
        except ValueError:
            print("Please enter your Passport ID number.")
      self.vars["passportId"] = passportId
      while True:
        try:
            passportExpiry = input("Please enter your Passport Expiry date in format dd-mm-yyyy: ")
            if len(passportExpiry) == 10:
                break
            else:
                print("Date must be in format dd-mm-yyyy.")
        except ValueError:
            print("Date must be in format dd-mm-yyyy")
      self.vars["passportExpiry"] = passportExpiry
      self.driver.find_element(By.XPATH, "//label[2]/span/input").click()
      self.driver.find_element(By.XPATH, "//div[@id=\'country\']").click()
      self.driver.find_element(By.XPATH, f"//li[contains(.,'{self.vars['country']}')]").send_keys(self.vars["country"])
      self.driver.find_element(By.XPATH, f"//li[contains(.,'{self.vars['country']}')]").click()
      self.driver.find_element(By.ID, "number").send_keys(self.vars["passportId"])
      self.driver.find_element(By.ID, "expiry").send_keys(self.vars["passportExpiry"])
      self.driver.find_element(By.ID, "policy").click()
      self.driver.find_element(By.XPATH, "(//button[@type=\'submit\'])[2]").click()
      print("Successfully created user.")
  
if __name__ == "__main__":
  test = TestCreateUser()
  test.test_createUser()