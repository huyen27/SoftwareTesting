from selenium import webdriver

driver = webdriver.Chrome(executable_path = 'venv/chromedriver.exe')

driver.get('https://nxbkimdong.com.vn/')

print(driver.title)

driver.close()