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
        self.b1 = Button(self, text="Total Clicks: 0")
        self.b1["command"] = self.update_count
        self.b1.grid()

    def update_count(self):

        self.button_clicks += 1
        self.b1["text"] = "Total Clicks: " + str(self.button_clicks)


root = Tk()
root.title("Click Counter")
root.geometry("200x50")
app = Application(root)
root.mainloop()
