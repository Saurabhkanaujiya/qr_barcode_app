import tkinter as tk
from PIL import Image, ImageTk
from pages.qr_page import QRPage
from pages.barcode_page import BarcodePage
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR & Barcode Generator")
        self.root.geometry("420x620")
        self.root.minsize(380, 560)
        self.root.configure(bg="#ADD8E6")

        # Icon
        icon = ImageTk.PhotoImage(Image.open(resource_path("assets/logo.png")))
        self.root.iconphoto(False, icon)
        self._icon_ref = icon  # prevent garbage collection

        # Header
        self.header = tk.Frame(self.root, height=60, bg="#263238")
        self.header.pack(fill="x")

        logo_img = ImageTk.PhotoImage(Image.open(resource_path("assets/logo.png")).resize((32, 32)))
        logo = tk.Label(self.header, image=logo_img, bg="#263238")
        logo.image = logo_img
        logo.pack(side="left", padx=10)

        tk.Label(self.header, text="QR & Barcode Generator",
                 font=("Segoe UI", 16, "bold"),
                 fg="white", bg="#263238").pack(side="left")

        # Nav
        self.nav = tk.Frame(self.root, bg="#37474F")
        self.nav.pack(fill="x")

        # Content
        self.content = tk.Frame(self.root)
        self.content.pack(fill="both", expand=True)

        # Pages
        self.qr_page = QRPage(self.content)
        self.barcode_page = BarcodePage(self.content)

        tk.Button(self.nav, text="QR", fg="white", bg="#455A64",
                  relief="flat", command=lambda: self.switch_page(self.qr_page.frame)
                  ).pack(side="left", expand=True, fill="x")

        tk.Button(self.nav, text="Barcode", fg="white", bg="#455A64",
                  relief="flat", command=lambda: self.switch_page(self.barcode_page.frame)
                  ).pack(side="left", expand=True, fill="x")

        # Footer
        self.footer = tk.Frame(self.root, height=30, bg="#263238")
        self.footer.pack(fill="x")

        tk.Label(self.footer, text="© Python Desktop App",
                 fg="white", bg="#263238",
                 font=("Segoe UI", 9)).pack(pady=6)

        self.switch_page(self.qr_page.frame)

    def switch_page(self, page):
        self.qr_page.frame.pack_forget()
        self.barcode_page.frame.pack_forget()
        page.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()
