from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("file:///Users/aaratiadhikari/mock-assesment-app/index.html")

# first input text on task field
task_input = driver.find_element(By.XPATH, '//*[@id="taskInput"]')
task_input.send_keys("eat food")

#click on add task button to create new task
add_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/button')
add_button.click()

#click on edit button
edit_button = driver.find_element(By.XPATH, '//*[@id="taskList"]/li[1]/div[2]/button[1]')
edit_button.click()

#switch to edit task popup
alert_popup = driver.switch_to.alert

#typing in edit popup
alert_popup.send_keys("eating food")
alert_popup.accept()

while True:
    pass


