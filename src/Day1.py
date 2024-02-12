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
    print("pass",actual_newuser_text)

driver.find_element(By.XPATH,"//input[@type = 'text']").send_keys("chaitanya") 
driver.find_element(By.XPATH,"//input[@data-qa = 'signup-email']").send_keys("zxcv@gmail.com")
driver.find_element(By.XPATH,"//button[@data-qa = 'signup-button']").click()
signup_page_heading = driver.find_element(By.XPATH, "//b[contains(text(), 'Enter')]").text

if(signup_page_heading == "ENTER ACCOUNT INFORMATION"):
    print("pass",signup_page_heading)


driver.find_element(By.XPATH,"//input[@id = 'id_gender1']").click()
driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys("Abcd1234")

days = driver.find_element(By.XPATH,"//select[@id = 'days']")
days.send_keys("14")
month = driver.find_element(By.XPATH,"//select[@id = 'months']")
month.send_keys("August")
years = driver.find_element(By.XPATH,"//select[@id = 'years']")
years.send_keys("2000")

checkboxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox']")
for i in checkboxes:
    i.click()

driver.find_element(By.XPATH,"//label[@for = 'first_name']") 
driver.find_element(By.XPATH,"//input[@id = 'first_name']").send_keys("abc")
driver.find_element(By.ID,"last_name").send_keys("zxc")
driver.find_element(By.ID,"company").send_keys("nvbg")
driver.find_element(By.ID,"address1").send_keys("dfghfk 345")


