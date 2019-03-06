import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import random as r

funnyword = ["Kurdupel", "Mordoklejka", "Wiktor", "Siusiak", "Dyskietka", "Prezydent", "Cymes", "Kalabrak", "Bunczuczny", "Ancymonek", "Krnabry", "Dynks", "Papcie", "Bimbaj", "Kotlet"]

sGui = tk.Tk()

def showMessage():
    sExit = mb.askyesno(title = "Close", message = "Are you sure?")
    if sExit == 1:
        sGui.destroy()
        return

def showRandom():
    word = r.choice(funnyword)
    print(word)

def s_open():
    sOpen = fd.askopenfile()

def s_save():
    sSave = fd.asksaveasfile()

#ustawienia okna
sGui.geometry("400x400")
sGui.title("Sing up")

#przyciski
sButton_close = tk.Button(text = "Close", command = showMessage).place(x = 20, y = 350)
sButton_random = tk.Button(text = "Click Here!", command = showRandom).place(x = 170, y = 200)

sLabel_acc = tk.Label(text = "Create your account", fg = "blue", font = 20).place(x = 20, y = 20)
sLabel_log = tk.Label(text = "Login").place(x = 20, y = 60)
sLabel_pas = tk.Label(text = "Password").place(x = 20, y = 120)

sEntry_log = tk.Entry().place(x = 20, y = 80)
sEntry_pas = tk.Entry().place(x = 20, y = 140)

menubar = tk.Menu(sGui)
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Open", command = s_open)
filemenu.add_command(label = "Save", command = s_save)
filemenu.add_command(label = "Settings")
filemenu.add_command(label = "Exit", command = showMessage)

menubar.add_cascade(label = "File", menu = filemenu)

sGui.config(menu = menubar)

sGui.mainloop()