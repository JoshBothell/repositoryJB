# Josh Bothell
# 3/19
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text="Enter password for the secret of life")
        self.inst_lbl.grid(row=0, column=1, columnspan=2, sticky=W)
        self.pw_lbl = Label(self, text="Password")
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        self.pw_ent = Entry(self, show="*")
        self.pw_ent.grid(row=1, column=1, sticky=W)



root = Tk()
root.title("Secret of Life")
root.geometry("500x300")
app = Application(root)
root.mainloop()
