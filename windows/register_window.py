from collections.abc import Callable, Sequence
import tkinter as tk
import tkinter.messagebox
from typing import Any
from GameConstants import *
from SignInConstants import *
from screen import Screen

class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(f"{REGISTER_WINDOW_WIDTH}x{REGISTER_WINDOW_HEIGHT}")
        self.title("Register")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        
        self.username_label = tk.Label(self, text="Username", font=LOGIN_TXT_FONT)
        self.username_entry = tk.Entry(self, width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.password_label = tk.Label(self, text="Password", font=LOGIN_TXT_FONT)
        self.password_entry = tk.Entry(self, show="●", width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.password_confirm_label = tk.Label(self, text="Confirm Password", font=LOGIN_TXT_FONT)
        self.password_confirm_entry = tk.Entry(self, show="●", width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.email_label = tk.Label(self, text="Email", font=LOGIN_TXT_FONT)
        self.email_entry = tk.Entry(self, width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.register_button = tk.Button(self, text="Register", command=self.register)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.password_confirm_label.pack()
        self.password_confirm_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.register_button.pack()



    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()
        email = self.email_entry.get()

        if(not check_credential(password, password_confirm, username, email)):
            self.password_entry.delete(0, tk.END)
            self.password_confirm_entry.delete(0, tk.END)
            return
        
        respond = write_to_db(username, password, email)

        if(respond):
            tkinter.messagebox.showinfo("Success", "Account created successfully")
            self.destroy()
        else:
            tkinter.messagebox.showerror("Error", "An error occured in writing to database")
            return

def check_credential(password, password_confirm, username, email):

    if(len(password) < PASSWORD_MIN_LENGTH):
        tkinter.messagebox.showerror("Password Too Short", f"Password must be at least {PASSWORD_MIN_LENGTH} characters long")
        return False

    for i in INVALID_CHARACTERS:
        if(i in username or i in password or i in email):
            tkinter.messagebox.showerror("Invalid Caracters", f"Username and password cannot contain\n{str(INVALID_CHARACTERS)}")
            return False
    
    if("@" not in email or ".com" not in email):
        tkinter.messagebox.showerror("Invalid Email", "Email Invalid")
        return False

    if(password != password_confirm):
        tkinter.messagebox.showerror("Password Mismatch", "Passwords do not match")
        return False
    
    res = read_db()
    if(res != False):
        for i in res:
            cur_username, cur_email = i.split(";")[0], i.split(";")[2].strip()
            if(username == cur_username):
                tkinter.messagebox.showerror("Username Taken", "Username already taken")
                return False
            if(email == cur_email):
                tkinter.messagebox.showerror("Email Taken", "Email already taken")
                return False
    else:
        tkinter.messagebox.showerror("Error", "An error occured in reading database")
        return False

    return True

def read_db():
    try:
        with open(PATH_TO_DB, "r") as f:
            return f.readlines()
    except Exception as e:
        print(e)
        return False

def write_to_db(username, password, email):
    try:
        with open(PATH_TO_DB, "a") as f:
            f.write(f"{username};{password};{email}\n")
            return True
    except Exception as e:
        print(e)
        return False
