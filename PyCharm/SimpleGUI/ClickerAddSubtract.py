# Josh Bothell
# 3/19
from tkinter import *


class Application(Frame):
    """GUI Applicaton which counts button clicks."""
    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.button_clicks = 0  # Num of Button Clicks
        self.create_widget()

    def create_widget(self):
        self.label = Label(text="Total Clicks: 0")
        self.b1 = Button(self, text="+", height="1", width="1")
        self.b1["command"] = self.update_count
        self.b2 = Button(self, text="-", height="1", width="1")
        self.b2["command"] = self.update_count_subtract
        self.b2.grid()
        self.b1.grid()
        self.label.grid()

    def update_count(self):
        self.button_clicks += 1
        self.label["text"] = "Total Clicks: " + str(self.button_clicks)

    def update_count_subtract(self):
        self.button_clicks -= 1
        self.label["text"] = "Total Clicks: " + str(self.button_clicks)


root = Tk()
root.title("Click Counter")
root.geometry("500x300")
app = Application(root)
root.mainloop()
