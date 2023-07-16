import tkinter as tk
import tkinter.ttk as ttk

def show_screen(screen):
    screen.tkraise()
    screen.pack()
    for widget in screen.winfo_children():
        if isinstance(widget, tk.Label):
            widget.pack()
        elif isinstance(widget, tk.Button):
            widget.pack()

def create_screen1(root):
    screen1 = tk.Frame(root)
    label1 = tk.Label(screen1, text="Screen 1")
    label1.pack()
    button1 = tk.Button(screen1, text="Switch to Screen 2", command=lambda: show_screen(screen2))
    button1.pack()
    return screen1

def create_screen2(root):
    screen2 = tk.Frame(root)
    label2 = tk.Label(screen2, text="Screen 2")
    label2.pack()
    button2 = tk.Button(screen2, text="Switch to Screen 1", command=lambda: show_screen(screen1))
    button2.pack()
    return screen2

root = tk.Tk()

screen1 = create_screen1(root)
screen2 = create_screen2(root)

show_screen(screen1)

switch_button = tk.Button(root, text="Switch Screens")
switch_button["command"] = lambda: ttk.destroy(root.focus_get()) if switch_button["text"] == "Switch to Screen 2" else ttk.destroy(screen1)
switch_button.pack()

root.mainloop()
