import tkinter as tk
from frame_url import Frame_URL

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('YouTube Converter')

        # Min size doesn't work on my computer, I can still resize the window to less than 800x600
        self.minsize(800, 600)

        self.frame_url = Frame_URL(self)

        self.columnconfigure(0, weight=1)

        self.mainloop()


