

class WindowHandler():
    def __init__(self, root):
        self.root = root
        self.current_window = None

    def ChangeWindow(self, new_window):
        if(self.current_window != None):
            self.current_window.destroy()
        self.current_window = new_window(self.root)

    def GetCurWindow(self):
        return self.current_window