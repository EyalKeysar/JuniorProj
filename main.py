import tkinter as tk
from SignInConstants import *
from GameConstants import *
from screen import Screen
from windows.login_window import LoginWindow
from windows.register_window import RegisterWindow
import time

def main_screen():
    screen = Screen()
    
    screen.add_widget(
        tk.Label(text="Disconnected", bg="#FF0000", width=SCREEN_WIDTH, height=CONNECTIONSTATUSBARHEIGHT))
    screen.add_widget(
        tk.Label(text = SIGNINTITLETXT, bg = TITLEBGCLR, width=SCREEN_WIDTH, height=SIGNINTITLETXTHEIGHT, font = SIGNINTXTFONT))
    screen.add_widget(
        tk.Button(text = "Login", command=lambda: LoginWindow(screen), font=BTNFONT, bg=BTNBGCLR, width=SIGNINBUTTONWIDTH, height=SIGNINBUTTONHEIGHT, activebackground=BTNCLR_ON_CLICK))
    screen.add_widget(
        tk.Button(text = "Register",command=lambda: RegisterWindow(screen) , font=BTNFONT, bg=BTNBGCLR, width=SIGNINBUTTONWIDTH, height=SIGNINBUTTONHEIGHT, activebackground=BTNCLR_ON_CLICK))

    def network_check():
        screen.after(100, network_check)

    screen.after(100, network_check)
    screen.show()
    screen.mainloop()
    
if __name__ == "__main__":
    # chan
    main_screen() 