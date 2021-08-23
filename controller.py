#import web_exchange
from tkinter import *
from tkinter import ttk
import tkinter
import web_exchange
import os


def main():
    window = Tk()
    window.title("New user form")
    window.geometry('400x400')

    alias = tkinter.StringVar()
    imie = tkinter.StringVar()
    nazwisko = tkinter.StringVar()

    a = Label(window ,text = "Imie").grid(row = 0,column = 0)
    b = Label(window ,text = "Nazwisko").grid(row = 1,column = 0)
    c = Label(window ,text = "alias").grid(row = 2,column = 0)
    a1 = Entry(window, textvariable=imie).grid(row = 0,column = 1)
    b1 = Entry(window, textvariable=nazwisko).grid(row = 1,column = 1)
    c1 = Entry(window, textvariable=alias).grid(row = 2,column = 1)


    var_d = tkinter.IntVar
    d = tkinter.Checkbutton(window, text="mail",variable=var_d, onvalue=1, offvalue=0).grid(row=5,column=0)


    def begin():
        print("web exchange")
        web_exchange.main(alias.get() ,imie.get(), nazwisko.get())

    submit_button = ttk.Button(window ,text="Submit", command=begin).grid(row=4,column=0)
    window.mainloop()


if __name__ == "__main__":
    main()