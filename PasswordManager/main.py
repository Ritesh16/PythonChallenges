from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height= 200, width= 200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo)

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
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Button
generate_button = Button(text="Generate Button")
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
