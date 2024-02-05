from tkinter import *
from tkinter import messagebox
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message= "Please add valid website or password")
    else:
        is_ok = messagebox.askokcancel(title=website, message= f"You have entered the following:\nEmail: {email}\nPassword: {password}")

        if is_ok:
            existing_passwords = get_all_passwords()
            existing_passwords[website] = f"{email}|{password}"

            remove_file()
            print(existing_passwords)
            with open("data.txt", "a") as file:
                for item in existing_passwords:
                    file.write(f"{item}|{existing_passwords[item]}" + "\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)


def get_all_passwords():
    list = {}

    if not os.path.exists("data.txt"):
        return list

    with open("data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line not in (None, ""):
                data = line.split('|')
                list[data[0].strip()] = data[1] + "|" + data[2]

    return list

def remove_file():
    if os.path.exists("data.txt"):
        os.remove("data.txt")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height= 200, width= 200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

canvas.grid(row = 0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column = 0)
email_label = Label(text="Email/UserName:")
email_label.grid(row=2, column = 0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width= 35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ritesh@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Button
generate_button = Button(text="Generate Button")
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
