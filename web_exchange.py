# coding=utf-8

import argparse
from selenium import webdriver
import time
import json
import os
import getpass
import password_generator
import csv
import sys


driver = webdriver.Firefox(executable_path=r'geckodriver.exe')


# from "http://gentle.pl/2017/07/19/usuwanie_polskich_znakow_python.html"
def removeAccents(input_text):
    strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
    ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)


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


def add_user(name, surname, password):
    alias = removeAccents(name.lower() + "." + surname.lower())
    driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

    new_user = driver.find_element_by_class_name("ToolBarButtonLnk")
    new_user.click()

    new_user2 = driver.find_element_by_xpath("//*[@id=\"ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_ToolBar_NewMailBoxSplitButton_DropDown\"]/div[1]/a")
    new_user2.click()

    time.sleep(1)

    handles = driver.window_handles
    driver.switch_to_window(handles[1])

    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxAlias", alias)
    click_id("ResultPanePlaceHolder_NewMailbox_contentContainer_rblMailboxTypeSelectNew")
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_ctl09_tbxFirstName", name)
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_ctl09_tbxLastName", surname)
    type_id("ResultPanePlaceHolder_NewMailbox_contentContainer_tbxDisplayName", name + " " + surname + " (RZGW Kraków)")
    userPrincipalName = removeAccents(name[0].lower() + surname.lower())
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


'''
    # TODO automatyczne wybieranie bazy skrzynek pocztowych

    input("Wybierz bazę danych skrzynek pocztowych i wcisnij enter")

    click_id("ResultPanePlaceHolder_ButtonsPanel_btnCommit")

    time.sleep(1)

'''


def click_id(item):
    element = driver.find_element_by_id(item)
    element.click()

def type_id(item, input):
    element = driver.find_element_by_id(item)
    element.click()
    element.clear()
    element.send_keys(input)


def run(args):
    path = os.getcwd() + "\data\web_exchange.json"
    file = open(path)
    data = json.load(file)

    driver.get(data['web_address'])
    time.sleep(1)
    login(data['login'])
    time.sleep(1)

    if args.f:
        path_osoby = os.getcwd() + "\data\osoby.csv"        
        with open(path_osoby, newline='',encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                password = password_generator.generate_password()
                print(row['imie'] + " " + row['nazwisko'] + " password:\n" + password + "\n------------------------")

                add_user(row['imie'], row['nazwisko'], password)

                what_next = input("for next person type == next ==\n to end type == exit ==\n")
                while(what_next != "next" and what_next != "exit"):
                    what_next = input("for next person type == next ==\n to end type == exit ==\n")
                
                if what_next == "exit":
                    sys.exit()

                handles = driver.window_handles
                driver.switch_to_window(handles[0])
    else:
        password = password_generator.generate_password()
        print("users password:\n", password)
        add_user(args.n, args.s, password)


def main():
    parser = argparse.ArgumentParser(description="Create exchange account")
    parser.add_argument("-f",help="data from osoby.csv", action="store_true")
    parser.add_argument("-n",help="name (imie)")
    parser.add_argument("-s",help="surname (nazwisko)")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

    

if __name__ == "__main__":
    main()