from selenium import webdriver
import time
import json
import os
import getpass


driver = webdriver.Firefox(executable_path=r'C:\My Things\geckodriver.exe')


def login(username_data):
    username = driver.find_element_by_name("username")
    username.click()
    username.clear()
    username.send_keys(username_data)

    password = driver.find_element_by_name("password")
    password.click()
    password.clear()
    
    try:
        p = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
    else:
        password.send_keys(p)

    sign_in = driver.find_element_by_class_name("signinbutton")
    sign_in.click()


def add_user():
    driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

    new_user = driver.find_element_by_class_name("ToolBarButtonLnk")
    new_user.click()

    new_user2 = driver.find_element_by_xpath("//*[@id=\"ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_ToolBar_NewMailBoxSplitButton_DropDown\"]/div[1]/a")
    new_user2.click()

    time.sleep(1)

    handles = driver.window_handles
    driver.switch_to_window(handles[1])

    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxAlias", "jkowalski")

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_rblMailboxTypeSelectNew")

    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_ctl09_tbxFirstName", "Jan")

    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_ctl09_tbxLastName", "Kowalski")

    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxUserPrincipalName", "jkowalski")

    haslo = "haslo123"
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxPassword", haslo)

    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxConfirmPassword", haslo)

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxResetPasswordOnNextLogon_label")

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_listDomain")
    nazwa_logowania_sufix2 = driver.find_element_by_xpath("//*[@id=\"ResultPanePlaceHolder_NewMailbox_contentContainer_listDomain\"]/option[3]")
    nazwa_logowania_sufix2.click()

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_moreOptions_label")

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_pickerOrganizationalUnit_ctl00_browseButton")
    expand1 = driver.find_element_by_xpath("/html/body/form/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/div")
    expand1.click()
    selection = driver.find_element_by_xpath("/html/body/form/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[10]/div[1]")
    selection.click()
    click_id("dlgModalError_OK")


    

def click_id(item):
    element = driver.find_element_by_id(item)
    element.click()

def type_id(item, input):
    element = driver.find_element_by_id(item)
    element.click()
    element.clear()
    element.send_keys(input)




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