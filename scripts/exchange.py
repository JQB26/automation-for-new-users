# coding=utf-8

from selenium import webdriver
import time
import json
import os
import getpass
import csv
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

geckodriver_path = os.getcwd()[:-8] + "\drivers\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=geckodriver_path)


# from "http://gentle.pl/2017/07/19/usuwanie_polskich_znakow_python.html"
def removeAccents(input_text):
    strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
    ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)


# login with correction loop
def loginSuccessful():
    time.sleep(1)
    try:
        driver.find_element_by_id("signInErrorDiv")
        return False
    except:
        return True

def password_login():
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


def login(username_data):
    username = driver.find_element_by_name("username")
    username.click()
    username.clear()
    username.send_keys(username_data)

    password_login()

    time.sleep(1)

    while not(loginSuccessful()):
        password_login()


def add_user(userPrincipalName, name, surname, password):
    alias = removeAccents(name.lower() + "." + surname.lower())
    driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

    new_user = driver.find_element_by_class_name("ToolBarButtonLnk")
    new_user.click()

    new_user2 = driver.find_element_by_xpath("//*[@id=\"ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_ToolBar_NewMailBoxSplitButton_DropDown\"]/div[1]/a")
    new_user2.click()

    time.sleep(1)

    # main input data part

    handles = driver.window_handles
    driver.switch_to_window(handles[1])

    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxAlias", alias)
    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_rblMailboxTypeSelectNew")
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_ctl09_tbxFirstName", name)
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_ctl09_tbxLastName", surname)
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxDisplayName", name + " " + surname + " (RZGW Kraków)")
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxUserPrincipalName", userPrincipalName)
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxPassword", password)
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxConfirmPassword", password)
    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxResetPasswordOnNextLogon_label")

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_listDomain")
    nazwa_logowania_sufix2 = driver.find_element_by_xpath("//*[@id=\"ResultPanePlaceHolder_NewMailbox_contentContainer_listDomain\"]/option[3]")
    nazwa_logowania_sufix2.click()

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_moreOptions_label")

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_pickerOrganizationalUnit_ctl00_browseButton")

    time.sleep(1)

    expand1 = driver.find_element_by_xpath("/html/body/form/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/div")
    expand1.click()
    selection = driver.find_element_by_xpath("/html/body/form/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[10]/div[1]")
    selection.click()
    click_id("dlgModalError_OK")

    time.sleep(0.5)

    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_pickerMailboxDatabase_ctl00_browseButton")
    time.sleep(1)

    handles = driver.window_handles
    driver.switch_to_window(handles[2])

    actions1 = ActionChains(driver)
    actions1.send_keys(Keys.TAB * 4)
    actions1.perform()
    time.sleep(0.5)
    actions2 = ActionChains(driver) 
    actions2.send_keys(Keys.DOWN * 4)
    actions2.perform()
    actions3 = ActionChains(driver) 
    actions3.send_keys(Keys.ENTER)
    actions3.perform()

    time.sleep(0.5)

    driver.switch_to_window(handles[1])

    time.sleep(1)

    click_id("ResultPanePlaceHolder_ButtonsPanel_btnCommit")


def add_attributes(mail, phone, department, position):
    driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

    action_tab = ActionChains(driver)
    action_tab.send_keys(Keys.TAB)

    action_enter = ActionChains(driver)
    action_enter.send_keys(Keys.ENTER)

    action_down = ActionChains(driver) 
    action_down.send_keys(Keys.DOWN)

    for i in range(3):
        action_tab.perform()

    action_enter.perform()

    actions1 = ActionChains(driver)
    actions1.send_keys(mail)
    actions1.perform()
    action_enter.perform()

    for i in range(7):
        action_tab.perform()
        time.sleep(0.1)

    action_down.perform()

    time.sleep(2)

    action_enter.perform()

    time.sleep(2)

    handles = driver.window_handles
    driver.switch_to_window(handles[1])

    # 10 attribute
    click_id("ResultPanePlaceHolder_Mailbox_NameAndAccount_contentContainer_NameAndAccountPlaceHolder_moreOptions_label")

    edit_pen = driver.find_element_by_xpath("/html/body/form/div[3]/div/div[3]/div/div/div[1]/div/div/div[7]/div/div/div[1]/div/div/a")
    edit_pen.click()

    time.sleep(1)

    N = 9
    action1 = ActionChains(driver) 
    action1.send_keys(Keys.TAB * N)
    action1.perform()

    action2 = ActionChains(driver)
    action2.send_keys("Biuro")
    action2.perform()

    action3 = ActionChains(driver)
    action3.send_keys(Keys.ENTER)
    action3.perform()

    # end

    information_tab = driver.find_element_by_xpath("//*[@id=\"bookmarklink_2\"]")
    information_tab.click()

    time.sleep(1)

    type_id("ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_ctl00_tbxCity", "Kraków")
    type_id("ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_tbxPhone", phone)

    organization_tab = driver.find_element_by_xpath("//*[@id=\"bookmarklink_3\"]")
    organization_tab.click()

    time.sleep(1)

    type_id("ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxTitle", position)
    type_id("ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxDepartment", department)
    type_id("ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxCompany", "RZGW Kraków")

    click_id("ResultPanePlaceHolder_ButtonsPanel_btnCommit")



# help nav functions
def click_id(item):
    element = driver.find_element_by_id(item)
    element.click()

def type_id(item, input):
    element = driver.find_element_by_id(item)
    element.click()
    element.clear()
    element.send_keys(input)


def run():
    path = os.getcwd()[:-8] + "\data\web_exchange.json"
    file = open(path)
    data = json.load(file)

    driver.get(data['web_address'])
    time.sleep(1)
    login(data['login'])
    time.sleep(1)

    path_osoby = os.getcwd()[:-8] + "\data\\new_users.csv"
    with open(path_osoby, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            add_user(row['sammaccountname'], row['givenname'], row['surname'], row['password'])

            handles = driver.window_handles
            driver.switch_to_window(handles[0])

            add_attributes(row['emailaddress'], row['telephoneNumber'], row['department'], row['title'])

            handles = driver.window_handles
            driver.switch_to_window(handles[0])
        sys.exit()

def main():
    run()


if __name__ == "__main__":
    main()