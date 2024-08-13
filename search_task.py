from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("file:///Users/aaratiadhikari/mock-assesment-app/index.html")

#adding multiple tasks at onece
task = ["eat food", "eat", "drink", "drinking"]
for tasks in task:
 task_input = driver.find_element(By.XPATH, '//*[@id="taskInput"]')

 #clearing previously added tasks
 task_input.clear()
 task_input.send_keys(tasks)

 #click on add task button to create new task
 add_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/button')
 add_button.click()

#searching tasks
search_task = driver.find_element(By.XPATH,'//*[@id="taskSearch"]')
search_task.send_keys("d")
search_task.send_keys(Keys.ENTER)

while True:
    pass