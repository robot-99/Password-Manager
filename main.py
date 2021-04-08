from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(4, 6))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 3))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 3))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    for char in password_list:
        password += char

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def data_save():

    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": password,
        }
    }
    if len(web) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty Fields", message="Please make sure you have left any fields empty!")
    else:
        try:
            with open("data.json", "r") as my_data:
                # json.dump(new_data, my_data, indent=4)
                data = json.load(my_data)
        except FileNotFoundError:
            with open("data.json", "w") as my_data:
                json.dump(new_data, my_data, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as my_data:
                json.dump(data, my_data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Password Saved", message="Your password and username has been successfully saved")


def find_password():
    web_search = website_entry.get().title()
    try:
        with open("data.json", "r") as my_data:
            data = json.load(my_data)
            if web_search in data:
                email = data[web_search]["email"]
                password = data[web_search]["password"]
                messagebox.showinfo(title="Your details", message=f"Your details for {web_search}:\nEmail: {email} \nPassword: {password}")
            else:
                messagebox.showinfo(title="Entry not found", message=f"No entry for website {web_search} found.")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="There are no entries in your password manager")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
picture = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:", font=("Calibri", "14"))
website_label.grid(row=1, column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()

email_label = Label(text="Email/Username:", font=("Calibri", "14"))
email_label.grid(row=2, column=0)

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=3, stick=W)
email_entry.insert(0, "cameron.christian.samson@gmail.com")

password_label = Label(text="Password:", font=("Calibri", "14"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

generate_pwd_button = Button(text="Generate Password", font=("Calibri", "12"), width=21, command=generate_password)
generate_pwd_button.grid(row=3, column=2, sticky=E)

addtolib_button = Button(text="Add", font=("Calibri", "12"), width=12, command=data_save)
addtolib_button.grid(row=4, column=1)

search_button = Button(text="Search", font=("Calibri", "12"), width=16, command=find_password)
search_button.grid(row=1, column=2, stick=E)

window.mainloop()
