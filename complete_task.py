from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///Users/aaratiadhikari/mock-assesment-app/index.html")

# first input text on task field
task_input = driver.find_element(By.XPATH, '//*[@id="taskInput"]')
task_input.send_keys("eat food")

#click on add task button to create new task
add_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/button')
add_button.click()

#select checkbox element
checkbox = driver.find_element(By.XPATH, '//*[@id="taskList"]/li[1]/div[2]/input')
checkbox.click()

#checking if checkbox is selected
if checkbox.is_selected():
    print("checkbox is selected")
    
#if checkbox is not selected, select the checkbox
if not checkbox.is_selected():
    checkbox.click()

while True:
    pass