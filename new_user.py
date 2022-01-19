import argparse
import sys
import os

def run(args):
    if args.all:
        os.system(sys.executable + ' ' + os.getcwd() + '\scripts\\users.py')
        os.system(f'powershell.exe {os.getcwd()}\scripts\\ad.ps1')
        os.system(sys.executable + ' ' + os.getcwd() + '\scripts\\exchange.py')
        os.system(sys.executable + ' ' + os.getcwd() + '\scripts\\mail.py')
    else:
        if args.generate:
            os.system(sys.executable + ' ' + os.getcwd() + '\scripts\\users.py')
        if args.ad:
            os.system(f'powershell.exe {os.getcwd()}\scripts\\ad.ps1')
        if args.exchange:
            os.system(sys.executable + ' ' + os.getcwd() + '\scripts\\exchange.py')
        if args.office:
            os.system(sys.executable + ' ' + os.getcwd() + '\scripts\\mail.py')


def main():
    parser = argparse.ArgumentParser(description="Create new users accounts")
    parser.add_argument("-generate",help="generate users data from the osoby_input.txt", action="store_true")
    parser.add_argument("-ad",help="create AD accounts", action="store_true")
    parser.add_argument("-exchange",help="create email exchange accounts", action="store_true")
    parser.add_argument("-office",help="send email, to create office365 accout", action="store_true")
    parser.add_argument("-all",help="generate, ad, exchange, office", action="store_true")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
