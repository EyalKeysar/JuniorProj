import tkinter as tk
from SignInConstants import *
from GameConstants import *
from TkScreen import TkScreen


def main_screen():
    new_screen = TkScreen(
                            widget1=tk.Label(text="Disconnected", bg="#FF0000", width=SCREEN_WIDTH, height=CONNECTIONSTATUSBARHEIGHT),
                            widget2=tk.Label(text = SIGNINTITLETXT, bg = TITLEBGCLR, width=SCREEN_WIDTH, height=SIGNINTITLETXTHEIGHT, font = SIGNINTXTFONT),
                            widget3=tk.Button(text = "Login", font=BTNFONT, bg=BTNBGCLR, width=SIGNINBUTTONWIDTH, height=SIGNINBUTTONHEIGHT, activebackground=BTNCLR_ON_CLICK),
                            widget4=tk.Button(text = "Register", font=BTNFONT, bg=BTNBGCLR, width=SIGNINBUTTONWIDTH, height=SIGNINBUTTONHEIGHT, activebackground=BTNCLR_ON_CLICK)
                          )
    new_screen.start()
    

main_screen() 