from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://suninjuly.github.io/alert_accept.html")
driver.find_element_by_class_name("btn.btn-primary").click()
alert = driver.switch_to.alert
alert.accept()
x = driver.find_element_by_id("input_value").text
y = calc(x)
driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_class_name("btn.btn-primary").click()