from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create a new firefox gecko driver session
driver = webdriver.Firefox(executable_path=r'C:\Users\SRIKUCHAITU\PycharmProjects\PracticeSelProject\geckodriver.exe')
driver.maximize_window()

#navigate to the application
driver.get("http://www.yahoo.com")
assert 'Yahoo' in driver.title

elem = driver.find_element_by_name('p')
elem.send_keys('seleniumhq' + Keys.RETURN)

driver.refresh()

driver.close()
driver.quit()
