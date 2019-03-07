# Josh Bothell
# 3/19

from tkinter import *

root = Tk()
root.title("Labels")
root.geometry("750x750")


app = Frame(root)
app.grid()


def change_color():
    lbl.config(text="You are going to regret that...", fg="red", cursor="X_cursor")
    root.config(bg="black")
    lbl.config(bg="black")
    checkbox.grid_remove()
    app.config(bg="black")


lbl = Label(app, text="Please do not click the Checkbox :)", fg="Blue")
checkbox = Checkbutton(app, command=change_color)
lbl.grid()
checkbox.grid()

root.mainloop()
