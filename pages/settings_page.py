import tkinter as tk

class SettingsPage(tk.Frame):
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.theme = theme

        tk.Label(self, text="Settings", font=("Segoe UI", 14)).pack(pady=10)

        self.dark = tk.BooleanVar()
        tk.Checkbutton(self, text="Dark Mode 🌙",
                       variable=self.dark,
                       command=self.toggle).pack()

    def toggle(self):
        if self.dark.get():
            self.theme["bg"] = "#121212"
            self.theme["fg"] = "#FFFFFF"
        else:
            self.theme["bg"] = "#F2F2F2"
            self.theme["fg"] = "#000000"
