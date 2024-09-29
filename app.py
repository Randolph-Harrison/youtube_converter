import tkinter as tk
from frame_url import Frame_URL
from progress_bar import Progress_Bar

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('YouTube Converter')

        # Min size doesn't work on my computer, I can still resize the window to less than 800x600
        self.minsize(800, 600)

        Frame_URL(self)
        Progress_Bar(self)

        self.columnconfigure(0, weight=1)

        self.mainloop()


