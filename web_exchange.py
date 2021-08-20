# Python program to demonstrate
# selenium

from selenium import webdriver
import time
import json

driver = webdriver.Firefox(executable_path=r'C:\My Things\geckodriver.exe')

driver.get("https://poczta.kzgw.gov.pl/")

def login():
    username = driver.find_element_by_name("username")
    username.click()
    username.clear()
    username.send_keys("uzytkownik@gmail.com")

    password = driver.find_element_by_name("password")
    password.click()
    password.clear()
    password.send_keys("haslo123")

    sign_in = driver.find_element_by_class_name("signinbutton")
    sign_in.click()






def main():
    time.sleep(1)
    login()




if __name__ == "__main__":
    main()