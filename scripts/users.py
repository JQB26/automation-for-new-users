# coding=utf-8

import os
import csv
import password_generator


# from "http://gentle.pl/2017/07/19/usuwanie_polskich_znakow_python.html"
def removeAccents(input_text):
    strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
    ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'
    translator=str.maketrans(strange,ascii_replacements)
    return input_text.translate(translator)


path_new_users = os.getcwd()[:-8] + "\data\\new_users.csv"
result = open(path_new_users, "w", newline='', encoding="utf-8")

path_osoby_input = os.getcwd()[:-8] + "\data\\osoby_input.csv"
file = open(path_osoby_input, newline='', encoding="utf-8")
reader = csv.reader(file, delimiter=';')


i = 0
for row in reader:
    if i == 0:
        data = ""
        for el in row:
            data += el + ";"
        data = data[:-1]
        result.write(data + "\n")
    else:
        sammaccountname = row[0]
        name = row[1]
        givenname = name.split(' ', 1)[0]
        surname = name.split(' ', 1)[1][:len(name.split(' ', 1)[1]) - 6]
        userprincipialname = sammaccountname + "@krakow.rzgw.gov.pl"
        department_code = name.split(' ', 1)[1][-4:-1]
        ou = "OU=" + department_code + ",OU=BIURO,OU=RZGW,DC=krakow,DC=rzgw,DC=gov,DC=pl"
        #department
        path_department = os.getcwd()[:-8] + "\data\\decode_department.csv"
        with open(path_department, newline='', encoding="utf-8") as department_file:
            decode = csv.reader(department_file, delimiter=';')
            for dep in decode:
                if dep[0] == department_code:
                    department = dep[1]


        #
        Company = "RZGW Kraków"
        emailaddress = removeAccents(givenname.lower()) + "." + removeAccents(surname.lower()) + "@wody.gov.pl"
        password = password_generator.generate_password()

        result.write(sammaccountname + ";" + name + ";" + givenname + ";" + surname + ";" + userprincipialname + ";" + ou + ";"
        + Company + ";" + emailaddress + ";" + department +  ";;" + password + "\n")
        
    i += 1


result.close()
file.close()