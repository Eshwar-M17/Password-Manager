from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [choice(letters) for _ in range(randint(8, 10))]
    password_list2 = [choice(symbols) for _ in range(randint(2, 4))]
    password_list3 = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_list1 + password_list2 + password_list3
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #


def search():
    try:
        with open("data.json") as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(title="Error", message="no data file found.")
    else:
        if website_input.get() in data:
            email = data[website_input.get()]["email"]
            password = data[website_input.get()]["password"]
            messagebox.showinfo(title=website_input.get(), message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Oops", message=f"{website_input.get()} is missing!")
        website_input.delete(0, "end")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        website_input.get():{
            "email":email_username_input.get(),
            "password":password_input.get()
        }
    }
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showwarning(title="Oops", message="Some of your fields are empty?")
    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"These are the details that you have entered\nemail: {email_username_input.get()}\npassword: {password_input.get()}\nif your sure? Then press ok")
        if is_ok:
            try:
                with open("data.json", 'r') as file:
                    data = json.load(file)
            except json.decoder.JSONDecodeError:
                with open("data.json", 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, "end")
                password_input.delete(0, "end")
        else:
            website_input.delete(0, "end")
            password_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


# labels
website_label = Label(text="Website:", font=("arial", 9))
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:", font=("arial", 9))
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("arial", 9))
password_label.grid(row=3, column=0)


# buttons
add_button = Button(text="Add", width=45, font=("arial", 9), command=save)
add_button.grid(row=4, column=1, columnspan=2)

gen_pswd_button = Button(text="Generate Password", font=("arial", 9), command=password_generator)
gen_pswd_button.grid(row=3, column=2)

search_button = Button(text="Search", font=("arial", 9), width=16, command=search)
search_button.grid(row=1, column=2)


# inputs
website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()




email_username_input = Entry(width=53)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, "danudanee9@gmail.com")


password_input = Entry(width=33)
password_input.grid(row=3, column=1)


window.mainloop()
