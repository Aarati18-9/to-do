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

#pin task
pin_task = driver.find_element(By.XPATH, '//*[@id="taskList"]/li[1]/div[2]/button[3]')
pin_task.click()

#to see pinned task label changing from 'pin' to 'unpin'
driver.refresh()

while True:
    pass
