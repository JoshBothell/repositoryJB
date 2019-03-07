# Josh Bothell
# 3/19
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create three buttons that do nothing"""
        # First Button
        self.b1 = Button(self, text="I am useless")
        self.b1.grid()
        # Second Button
        self.b2 = Button(self, text="me too..")
        self.b2.grid()
        # Third Button
        self.b3 = Button(self)
        self.b3.grid()
        self.b3["text"] = "same here"


root = Tk()
root.title("Lazy Buttons 2")
root.geometry("500x300")
app = Application(root)
root.mainloop()
