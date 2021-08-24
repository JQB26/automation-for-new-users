from tkinter import *
from tkinter import ttk
import tkinter
import web_exchange
import mail


def main():
    window = Tk()
    window.title("New user form")
    window.geometry('400x400')

    alias = tkinter.StringVar()
    imie = tkinter.StringVar()
    nazwisko = tkinter.StringVar()
    grupa = tkinter.StringVar()

    a = Label(window ,text = "Imie").grid(row = 0,column = 0)
    b = Label(window ,text = "Nazwisko").grid(row = 1,column = 0)
    c = Label(window ,text = "alias").grid(row = 2,column = 0)
    d = Label(window, text = "grupa").grid(row = 3, column = 0)
    a1 = Entry(window, textvariable=imie).grid(row = 0,column = 1)
    b1 = Entry(window, textvariable=nazwisko).grid(row = 1,column = 1)
    c1 = Entry(window, textvariable=alias).grid(row = 2,column = 1)
    d1 = Entry(window, textvariable=grupa).grid(row = 3, column = 1)


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
        if var_exchange.get() == 1:
            print("exchange")
            web_exchange.main(alias.get() ,imie.get(), nazwisko.get(), grupa.get())
        if var_office.get() == 1:
            print("office")
            mail.main()

    submit_button = ttk.Button(window ,text="Submit", command=begin).grid(row=8,column=0)
    window.mainloop()


if __name__ == "__main__":
    main()