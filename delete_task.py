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

#delete button element
delete_button = driver.find_element(By.XPATH, '//*[@id="taskList"]/li[1]/div[2]/button[2]')
delete_button.click()

while True:
    pass