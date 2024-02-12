import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
login_signup = "//a[@href = '/login']"
driver.find_element(By.XPATH,login_signup).click()
time.sleep(5)
actual_newuser_text = driver.find_element(By.XPATH,"//h2[text() = 'New User Signup!']").text

if(actual_newuser_text == "New User Signup!"):
    print("pass")

driver.find_element(By.XPATH,"//input[@type = 'text']").send_keys("chaitanya") 
driver.find_element(By.XPATH,"//input[@data-qa = 'signup-email']").send_keys("zxcv@gmail.com")
driver.find_element(By.XPATH,"//button[@data-qa = 'signup-button']").click()
signup_page_heading = driver.find_element(By.XPATH, "//b[contains(text(), 'Enter')]").text

if(signup_page_heading == "ENTER ACCOUNT INFORMATION"):
    print("pass")


driver.find_element(By.XPATH,"//input[@id = 'id_gender1']").click()
driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys("Abcd1234")

days = driver.find_element(By.XPATH,"//select[@id = 'days']")
days.send_keys("14")
