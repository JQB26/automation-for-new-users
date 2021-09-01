from tkinter import *
from tkinter import ttk
import tkinter
import mail
import sys
import os


def main():
    window = Tk()
    window.title("New user form")
    window.geometry('400x400')

    imie = tkinter.StringVar()
    nazwisko = tkinter.StringVar()

    a = Label(window ,text = "Imie").grid(row = 0,column = 0)
    b = Label(window ,text = "Nazwisko").grid(row = 1,column = 0)
    a1 = Entry(window, textvariable=imie).grid(row = 0,column = 1)
    b1 = Entry(window, textvariable=nazwisko).grid(row = 1,column = 1)


    var_ad = tkinter.IntVar()
    active_directory = tkinter.Checkbutton(window, text="active directory",variable=var_ad, onvalue=1, offvalue=0).grid(row=5,column=0)
    var_exchange = tkinter.IntVar()
    exchange = tkinter.Checkbutton(window, text="exchange",variable=var_exchange, onvalue=1, offvalue=0).grid(row=6,column=0)
    var_office = tkinter.IntVar()
    office365 = tkinter.Checkbutton(window, text="office365",variable=var_office, onvalue=1, offvalue=0).grid(row=7,column=0)


    def begin():
        if var_ad.get() == 1:
            print("ad")
            # subprocess.run(['powershell.exe', 'active_directory.ps1 arg1 @('])
        if var_office.get() == 1:
            mail.main()
            print("mail sent")
        if var_exchange.get() == 1:
            command = sys.executable + ' web_exchange.py ' + ' -n ' + imie.get() + ' -s ' + nazwisko.get()
            os.system(command)

            print("exchange account created")
        

    submit_button = ttk.Button(window ,text="Submit", command=begin).grid(row=8,column=0)
    window.mainloop()


if __name__ == "__main__":
    main()