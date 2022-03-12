from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://www.amazon.com/")
driver.maximize_window()

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys('dress', Keys.ENTER)

expected_text = '"dress"'
# actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
actual_text = driver.find_element(By.CSS_SELECTOR, ".a-color-state.a-text-bold").text

assert expected_text == actual_text, f'Error. Expected text: {expected_text}, but actual_text: {actual_text}'

driver.quit()