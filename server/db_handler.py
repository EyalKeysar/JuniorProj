from constants import *



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
        return False, 
    
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