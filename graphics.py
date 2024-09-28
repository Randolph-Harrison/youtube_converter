import tkinter as tk
from tkinter import filedialog

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

class Frame_URL(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, pady=20)
        self.url = None
        self.directory = None
        tk.Label(self, text='Paste YouTube URL:').grid(row=0, column=0)

        self.entry = tk.Entry(self, width=50)
        self.entry.grid(row=0, column=1, sticky='ew', padx=20)
        self.display_url = tk.Label(self)
        self.display_url.grid(row=1, column=1)

        self.check_button= tk.Button(self, text='Check URL', command=self.entry_get)
        self.check_button.grid(row=0, column=2, padx=10)

        self.directory_button = tk.Button(self, text='Browse', command=self.get_directory)
        self.directory_button.grid(row=0, column=3)

        # Will probably implement to only show a download button if the check goes through
        self.download_button = tk.Button(self, text='Download')
        self.download_button.grid(row=2, column=1, pady=10)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(3, weight=0)
        self.grid(row=0, column=0, padx=20)
    
    def entry_get(self):
        self.url = self.entry.get()

        if self.url:
            self.display_url.config(text=self.url)
            self.entry.delete(0, tk.END)
        else:
            self.display_url.config(text="No URL was entered")
            self.entry.delete(0, tk.END)
    
    def get_directory(self):
        self.directory = filedialog.askdirectory(title='Select a folder')
        self.display_directory = tk.Label(self, text=self.directory)
        self.display_directory.grid(row=3, column=1)

class Progress_Bar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=1, column=0)



