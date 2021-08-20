from selenium import webdriver
import time
import json
import os


driver = webdriver.Firefox(executable_path=r'C:\My Things\geckodriver.exe')


def login(username_data):
    username = driver.find_element_by_name("username")
    username.click()
    username.clear()
    username.send_keys(username_data)

    password = driver.find_element_by_name("password")
    password.click()
    password.clear()
    password_input = input("Enter a password for web_exchange:\n")
    password.send_keys(password_input)

    sign_in = driver.find_element_by_class_name("signinbutton")
    sign_in.click()


def main():
    path = os.getcwd() + "\data\web_exchange.json"
    file = open(path)
    data = json.load(file)

    driver.get(data['web_address'])


    time.sleep(0.1)
    login(data['login'])




if __name__ == "__main__":
    main()