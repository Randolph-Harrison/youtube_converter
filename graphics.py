import tkinter as tk
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('YouTube Converter')
        self.minsize(800, 600)

        self.mainloop()
        
class Frame_URL(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, pady=20)
        tk.Label(self, text='Paste YouTube URL:').grid(row=0, column=0)
        self.entry = tk.Entry(self).grid(row=0, column=1, sticky='nsew', padx=20)

        self.url_buttom = tk.Button(self, text='Submit').grid(row=0, column=2)



        self.grid(row=0, column=0)
        self.url = None
    
    def entry_get(self):
        self.url = self.entry.get()
        print(self.url)



    



