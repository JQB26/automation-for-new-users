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


def add_user():
    driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
    new_user = driver.find_element_by_class_name("ToolBarButtonLnk")
    new_user.click()

    new_user2 = driver.find_element_by_xpath("//*[@id=\"ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_ToolBar_NewMailBoxSplitButton_DropDown\"]/div[1]/a")
    new_user2.click()

    time.sleep(0.1)

    handles = driver.window_handles
    driver.switch_to_window(handles[1])

    alias = driver.find_element_by_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxAlias")
    alias.click()
    alias.send_keys("jkowalski")

    nowy_uzytkownik_button = driver.find_element_by_id("ResultPanePlaceHolder_NewMailbox_contentContainer_rblMailboxTypeSelectNew")
    nowy_uzytkownik_button.click()

    imie = driver.find_element_by_id("ResultPanePlaceHolder_NewMailbox_contentContainer_ctl09_tbxFirstName")
    imie.click()
    imie.send_keys("Jan")

    nazwisko = driver.find_element_by_id("ResultPanePlaceHolder_NewMailbox_contentContainer_ctl09_tbxLastName")
    nazwisko.click()
    nazwisko.send_keys("Kowalski")

    nazwa_logowania = driver.find_element_by_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxUserPrincipalName")
    nazwa_logowania.click()
    nazwa_logowania.send_keys("jkowalski")

    haslo = "haslo123"
    nowe_haslo = driver.find_element_by_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxPassword")
    nowe_haslo.click()
    nowe_haslo.send_keys(haslo)

    potwierdz_haslo = driver.find_element_by_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxConfirmPassword")
    potwierdz_haslo.click()
    potwierdz_haslo.send_keys(haslo)

    wymagaj_zmiany_hasla = driver.find_element_by_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxResetPasswordOnNextLogon_label")
    wymagaj_zmiany_hasla.click()





def main():
    path = os.getcwd() + "\data\web_exchange.json"
    file = open(path)
    data = json.load(file)

    driver.get(data['web_address'])
    time.sleep(0.2)
    login(data['login'])
    time.sleep(1)

    add_user()





if __name__ == "__main__":
    main()