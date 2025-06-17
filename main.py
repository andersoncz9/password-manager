from tkinter import *
<<<<<<< HEAD
import random


# PASSWORD GENERATOR
def GeneratePassword():
    """This will generate a password with 10 random characters"""
    password_entry.delete(0, END)
    password = ''
    chars = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "^", "&", "*"]
    for i in range(0, 10):
        password += random.choice(chars)
    password_entry.insert(0, password)

# SAVE PASSWORD 
def SavePassword():
    """This will save the info in to a file."""
    if len(email_entry.get()) <= 0:
        popupInfo("Please, insert an email.")
    elif len(password_entry.get()) < 8:
        popupInfo("Password should be at least 8 characteres long.\n Try using the generate password button.")
    else:
        with open(r"D:/ADS/python/Password Manager/passwords.txt", "a") as doc: 
            doc.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        popupInfo("Password Saved")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.delete(0, END)

# UI 
def popupInfo(texto):
    win2 = Toplevel()
    win2.title("Password Manager")
    win2.config(padx=20, pady=20)
    l = Label(win2, text=texto).grid(row=0, column=1, pady=10)
    b = Button(win2, text="OK", command=win2.destroy, padx=20).grid(row=1, column=1)
    
# Janela principal
window = Tk()
window.title("Password Manager")
window.geometry("550x400")
window.config(padx=20, pady=20)

# Configurar colunas para expandir
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=1)

# Logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo = PhotoImage(file="D:/ADS/python/Password Manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=1, pady=(0, 20))

# Labels e Entradas
website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1, sticky="e", padx=(10, 5), pady=5)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w", pady=5)
website_entry.focus()

email_lbl = Label(text="Email/User:")
email_lbl.grid(column=0, row=2, sticky="e", padx=(10, 5), pady=5)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w", pady=5)

password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3, sticky="e", padx=(10, 5), pady=5)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w", pady=5)

generate_button = Button(text="Generate Password", width=15, command=GeneratePassword)
generate_button.grid(column=2, row=3, sticky="w", padx=(5, 0))

# Botão Add
add_button = Button(text="Add", width=36, command=SavePassword)
add_button.grid(column=0, row=4, columnspan=4, pady=15)
=======

window = Tk()
window.title("Password Manager")







>>>>>>> bef1b4bdc9316d36fadd123ef192d2f09d01abd6

window.mainloop()
