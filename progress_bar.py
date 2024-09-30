import tkinter as tk
from tkinter import ttk

class Progress_Bar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.progress_bar = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=500, mode='determinate')
        self.progress_bar.grid(row=0, column=0)

        self.grid(row=1, column=0)


