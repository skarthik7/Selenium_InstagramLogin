from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time

def open_web(service,username,pw):
  print("HI")
  service={'gmail':'gmail.com'}
  driver = webdriver.Chrome(r"./chromedriver2")
  
  driver.get("https://www.instagram.com/?hl=en")
  driver.maximize_window()
  
  inputElement = driver.find_element_by_name("username")
  inputElement.send_keys(username)

  inputElement2 = driver.find_element_by_name("password")
  inputElement2.send_keys(pw)
  
  inputElement2.send_keys(Keys.ENTER)

  time.sleep(10000)


def main():
 
  username = input("username: ")
  pw = getpass.getpass('Password: ', stream=None) 

  open_web('',username,pw)
main()
