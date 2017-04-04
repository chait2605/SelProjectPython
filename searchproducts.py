from selenium import webdriver

#create a new firefox gecko driver session
driver = webdriver.Firefox(executable_path=r'C:\Users\SRIKUCHAITU\PycharmProjects\PracticeSelProject\geckodriver.exe')
driver.maximize_window()

#navigate to the application
driver.get("http://www.yahoo.com")
assert 'Yahoo' in driver.title

driver.close()
driver.quit()
