from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("file:///Users/aaratiadhikari/mock-assesment-app/index.html")

# first input text on task field
task_input = driver.find_element(By.XPATH, '//*[@id="taskInput"]')
task_input.send_keys("eat food")

#select priority 
priority_task = Select(driver.find_element(By.XPATH, '//*[@id="taskPriority"]'))
priority_task.select_by_visible_text("High")

#select due date
due_date= driver.find_element(By.XPATH,'//*[@id="taskDueDate"]')
due_date.send_keys("08/08/2024")

#click on add task button to create new task
add_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/button')
add_button.click()

while True:
    pass

