
from selenium import webdriver 
import time 
browser = webdriver.Chrome("/home/student/Downloads/chromedriver_linux64/chromedriver")
d={"R180578":"OFCLR","R180580":"GACJJ"}


  
for key,value in d.items():
	browser.get("http://210.212.217.214/")
	id=browser.find_element_by_xpath("/html/body/div[2]/div/div/form/div[1]/input")
	id.send_keys(key)
	pwd=browser.find_element_by_xpath("/html/body/div[2]/div/div/form/div[2]/input")
	pwd.send_keys(value)
	login=browser.find_element_by_xpath("/html/body/div[2]/div/div/form/div[3]/button")
	login.click()
	time.sleep(2)
	browser.get('chrome://settings/')
	browser.execute_script('chrome.settingsPrivate.setDefaultZoom(0.9);')
	browser.get("http://210.212.217.214/ay1920sem2stu.php")
	browser.set_window_size(1024, 600)
	browser.maximize_window()
	time.sleep(2)
	browser.save_screenshot("dinu.png")
	

