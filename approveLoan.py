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

class TestApproveLoan():
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
  
  def test_approveLoan(self):
    wait = WebDriverWait(self.driver, 10)
    self.vars["email"] = "testing2@testing2.com"
    self.vars["password"] = "testing2"
    self.driver.get("https://getloanr.com/dashboard/loan-board")
    self.vars["isLogin"] = self.driver.find_element(By.CSS_SELECTOR, ".MuiTypography-root > p").text
    print("{}".format(self.vars["isLogin"]))
    self.driver.find_element(By.ID, "email").send_keys(self.vars["email"])
    self.driver.find_element(By.ID, "password").send_keys(self.vars["password"])
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type=\'submit\']"))).click()
   # time.sleep(6)
    self.driver.implicitly_wait(10)
    self.driver.get("https://getloanr.com/dashboard/loan-board")
    button22 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-1b401o0")))
    button22.click()
    self.vars["isLoan"] = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".css-177gxwv"))).text
    self.vars["loansApproved"] = 0
    print("Searching loans")
  
    while(self.vars["isLoan"] == "Grant a Loan"):
      self.driver.find_element(By.XPATH, "//div[2]/div[2]/div/div[3]/button[2]").click()
      wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type=\'submit\']"))).click()
      self.driver.find_element(By.XPATH, "//input[@type=\'checkbox\']").click()
      self.driver.find_element(By.XPATH, "//button[contains(.,'Confirm Request')]").click()
      self.driver.get("https://getloanr.com/dashboard/loan-board")
      self.vars["loansApproved"] = self.vars["loansApproved"] + 1
      print("Loan number: {}".format(self.vars["loansApproved"]))
      # time.sleep(6)
      self.driver.implicitly_wait(10)
      self.vars["isLoan"] = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".css-177gxwv"))).text
    print("Loans approved: {}".format(self.vars["loansApproved"]))

if __name__ == "__main__":
  test = TestApproveLoan()
  test.test_approveLoan()