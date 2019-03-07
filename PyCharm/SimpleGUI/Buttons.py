# Josh Bothell
# 3/19
from tkinter import *

color1 = "#D7DBDD"
color2 = "#AED6F1"
color3 = "#17202A"
root = Tk()

root.title("Buttons")
root.geometry("1920x1080")
root.config(bg=color1)

mainframe = Frame(root)
mainframe.grid()
root.config(bg=color1)
mainframe.config(bg=color1)

label = Label(mainframe, text="This is a button:", bg=color1, fg=color3)
label.grid()

button1 = Button(mainframe, text="Button #1", bg=color2, fg=color3)
button1.grid()

button2 = Button(mainframe)
button2.grid()
button2.config(text="Button #2", bg=color2, fg=color3)

button3 = Button(mainframe)
button3.grid()
button3["text"] = "Button #3"
button3["bg"] = color2


root.mainloop()
