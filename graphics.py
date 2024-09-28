import tkinter as tk
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress
import requests
import re

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
        self.yt = None
        self.resolutions = []

        tk.Label(self, text='Paste YouTube URL:').grid(row=0, column=0)
        self.entry = tk.Entry(self, width=50)
        self.entry.grid(row=0, column=1, sticky='ew', padx=20)
        self.display_url = tk.Label(self)
        self.display_url.grid(row=1, column=1)

        self.check_button= tk.Button(self, text='Check URL', command=self.url_check)
        self.check_button.grid(row=0, column=2, padx=10)

        self.directory_button = tk.Button(self, text='Browse', command=self.get_directory)
        self.directory_button.grid(row=0, column=3)


        # Will probably implement to only show a download button if the check goes through
        self.download_button = tk.Button(self, text='Download', command=self.download)
        self.download_button.grid(row=2, column=1, pady=10)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(3, weight=0)
        self.grid(row=0, column=0, padx=20)
    
    def url_check(self):
        self.url = self.entry.get()

        if re.search(r"(youtu.*be.*)\/(watch\?v=|embed\/|v|shorts|)(.*?((?=[&#?])|$))", self.url):
            response = requests.head(self.url, allow_redirects=True)
            if response.status_code == 200:
                self.display_url.config(text=f'Valid link: {self.url}')
                self.entry.delete(0, tk.END)

                self.yt = YouTube(self.url)

                self.selected_option = tk.StringVar(self)
                self.selected_option.set("144p")

                for stream in self.yt.streams.filter(only_video=True):
                    if stream.resolution not in self.resolutions:
                        self.resolutions.append(stream.resolution)
                
                self.resolution_menu = tk.OptionMenu(self, self.selected_option, *self.resolutions)
                self.resolution_menu.grid(row=2, column=0)
        else:
            self.display_url.config(text="No URL was entered or invalid YouTube video link")
            self.entry.delete(0, tk.END)
    
    def get_directory(self):
        self.directory = filedialog.askdirectory(title='Select a folder')
        self.display_directory = tk.Label(self, text=self.directory)
        self.display_directory.grid(row=3, column=1)

    def download(self):
        if self.yt is None:
            self.url_check()
        else:
            stream = self.yt.streams.get_by_resolution()

class Progress_Bar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(row=1, column=0)



