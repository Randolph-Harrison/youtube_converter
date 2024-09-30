import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pytubefix import YouTube
import requests
import re
import os

class Frame_URL(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, pady=20)
        self.url = None
        self.directory = None
        self.yt = None
        self.resolutions = ['144p']
        self.resolution_menu = None

        self.selected_option = tk.StringVar(self)
        self.selected_option.set("144p")

        tk.Label(self, text='Paste YouTube URL:').grid(row=0, column=0)
        self.entry = tk.Entry(self, width=50)
        self.entry.grid(row=0, column=1, padx=20)
        self.display_url = tk.Label(self)
        self.display_url.grid(row=1, column=1)

        self.check_button= tk.Button(self, text='Check URL', command=self.url_check)
        self.check_button.grid(row=0, column=2, padx=5)

        self.directory_button = tk.Button(self, text='Browse', command=self.get_directory)
        self.directory_button.grid(row=0, column=3, padx=5, sticky='e')
        self.display_directory = tk.Label(self)
        self.display_directory.grid(row=3, column=1)

        self.download_button = tk.Button(self, text='Download', command=self.download, state='disabled')
        self.download_button.grid(row=2, column=1, pady=10)

        self.progress_bar = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=450, mode='determinate')
        self.progress_bar.grid(row=4, column=1)
        self.progress_label = tk.Label(self)
        self.progress_label.grid(row=5, column=1)

        self.grid(row=1, column=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.grid(row=0, column=0, padx=20)
    
    def url_check(self):
        self.url = self.entry.get()

        if re.search(r"(youtu.*be.*)\/(watch\?v=|embed\/|v|shorts|)(.*?((?=[&#?])|$))", self.url):
            response = requests.head(self.url, allow_redirects=True)
            if response.status_code == 200:
                self.display_url.config(text=f'Valid link: {self.url}')
                self.entry.delete(0, tk.END)

                self.yt = YouTube(self.url, on_progress_callback=self.on_progress)

                for stream in self.yt.streams.filter(only_video=True).desc():
                    if stream.resolution not in self.resolutions:
                        self.resolutions.append(stream.resolution)
                
                self.download_button.config(state='normal')
                self.resolution_menu = tk.OptionMenu(self, self.selected_option, *self.resolutions)
                self.resolution_menu.grid(row=2, column=0)
        else:
            if self.resolution_menu is not None:
                self.resolution_menu.grid_forget()
            self.download_button.config(state='disabled')
            self.display_url.config(text="No URL was entered or invalid YouTube video link")
            self.entry.delete(0, tk.END)
    
    def get_directory(self):
        self.directory = filedialog.askdirectory(title='Select a folder')
        self.display_directory.config(text=self.directory)
    
    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percent_complete = (bytes_downloaded / total_size) * 100

        self.progress_bar['value'] = percent_complete
        self.update_idletasks()

    def download(self):
        if self.yt is None:
            self.url_check()
        if self.directory is None:
            self.display_directory.config(text='No directory selected')
        else:
            self.progress_label.config(text='Downloading...')
            self.progress_bar['value'] = 0

            resolution = self.selected_option.get()
            audio_stream = self.yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            audio_stream.download(output_path=self.directory, filename='audio.mp4')

            video_stream = self.yt.streams.filter(progressive=False, only_video=True, res=resolution).first()
            video_stream.download(output_path=self.directory, filename='video.mp4')

            self.progress_label.config(text='Finishing up...')
            os.chdir(self.directory)
            os.system(f"ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac -shortest '{self.yt.title}.mp4'")
            if os.name == 'posix':
                os.system('rm video.mp4 audio.mp4')
            else:
                os.system('del video.mp4 audio.mp4')
            
            self.progress_label.config(text='Complete')

