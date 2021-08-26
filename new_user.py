import argparse
import mail
import sys
import json
import os


def get_input():
    path = os.getcwd() + "\data\\temp_data.json"
    if os.path.exists(path):
        os.remove(path)
    user = {'alias': input("alias: "),
            'imie': input("imie: "),
            'nazwisko': input("nazwisko: "),
            'grupa': input("grupa: ")}
    with open(path, 'w') as json_file:
        json.dump(user, json_file)

def print_data():
    with open(os.getcwd() + "\data\\temp_data.json") as json_file:
        data = json.load(json_file)
        print(data)


def run(args):
    if args.addData:
        get_input()
    if args.showData:
        print_data()
    if args.office365:
        mail.main()
        print("mail sent")
    if args.exchange:
        if os.path.exists(os.getcwd() + "\data\\temp_data.json"):
            file = open(os.getcwd() + "\data\\temp_data.json")
            data = json.load(file)

            command = sys.executable + ' web_exchange.py ' + data['alias'] + ' ' + data['imie'] + ' ' + data['nazwisko'] + ' ' + data['grupa']
            os.system(command)

            print("exchange account created")
        else:
            print("No data for the new user. addData first")
    



def main():
    parser = argparse.ArgumentParser(description="Add a new user")
    parser.add_argument("-addData",help="add data about adding person", action="store_true")
    parser.add_argument("-showData",help="show data about adding person", action="store_true")
    parser.add_argument("-exchange",help="create email exchange account", action="store_true")
    parser.add_argument("-office365",help="send email, to create office365 accout", action="store_true")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()