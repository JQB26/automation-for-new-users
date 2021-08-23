import win32com.client as client
import datetime
import json
import os


def main():
    # DANE DO MAILA
    path = os.getcwd() + "\data\mail.json"
    file = open(path)
    data = json.load(file)

    message_subject = data['message_subject']
    message_content = data["message_content"]
    message_to = data['adresat']

    # stworzenie maila
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.Subject = message_subject
    message.To = message_to
    message.GetInspector

    # podpis + dodanie tresci wiadomosci
    index = message.HTMLbody.find('>', message.HTMLbody.find('<body'))
    message.HTMLbody = message.HTMLbody[:index + 1] + message_content + message.HTMLbody[index + 1:]


    message.Display()
    
    message.Send()

if __name__ == "__main__":
    main()
