# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# # def test_driver_manager_chrome():
# service = ChromeService(executable_path=ChromeDriverManager().install())

# driver = webdriver.Chrome(service=service)

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://amazon.com")

# time.sleep(15)
# driver.quit()
