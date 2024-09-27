import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Youtube Converter")
        self.geometry("800x600")
        self.frame_url = AppFrame(self)
        self.frame_url.grid(row=0, column=0)

        self.frame_file_path = AppFrame(self)
        self.frame_file_path.grid(row=1, column=0)

        self.frame_progress_bar = AppFrame(self)
        self.frame_progress_bar.grid(row=2, column=0)

        self.mainloop()

class AppFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.button1 = AppButton(self)

        self.button1.grid(row=0, column=0)

class AppButton(tk.Button):
    def __init__(self, frame):
        super().__init__(frame, text='button1')





    



