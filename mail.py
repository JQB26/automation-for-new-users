import win32com.client as client
import datetime

# DANE DO MAILA
message_subject = "Test automatycznego maila"
message_content = "Proszę o założenie testowego konta...."
message_to = "lukasz.sobon@wody.gov.pl"

# stworzenie maila
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Subject = message_subject
message.To = message_to
message.GetInspector

# podpis + dodanie tresci wiadomosci
index = message.HTMLbody.find('>', message.HTMLbody.find('<body'))
message.HTMLbody = message.HTMLbody[:index + 1] + message_content + message.HTMLbody[index + 1:]

# opónienie w wyslaniu
message.DeferredDeliveryTime = datetime.datetime.now() + datetime.timedelta(minutes = 1)

message.Display()

message.Send()