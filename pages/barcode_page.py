import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
import os

class BarcodePage:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

        tk.Label(self.frame, text="Barcode Generator",
                 font=("Segoe UI", 14, "bold")).pack(pady=10)

        self.entry = tk.Entry(self.frame, font=("Segoe UI", 12), justify="center")
        self.entry.pack(fill="x", padx=40)

        self.label = tk.Label(self.frame)
        self.label.pack(pady=15)

        self.barcode_img = None

        btns = tk.Frame(self.frame)
        btns.pack()

        tk.Button(btns, text="Generate Barcode", bg="#4CAF50", fg="white",
                  width=16, height=2, command=self.generate_barcode).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(btns, text="Refresh", bg="#9E9E9E", fg="white",
                  width=16, height=2, command=self.refresh).grid(row=0, column=1, padx=5)

        tk.Button(btns, text="Download", bg="#2196F3", fg="white",
                  width=16, height=2, command=self.download).grid(row=1, column=0, padx=5)

        tk.Button(btns, text="Print", bg="#FF5722", fg="white",
                  width=16, height=2, command=self.print_barcode).grid(row=1, column=1, padx=5)

    def generate_barcode(self):
        data = self.entry.get().strip()
        if not data:
            messagebox.showwarning("Warning", "Enter text")
            return
        code = Code128(data, writer=ImageWriter())
        filename = code.save("temp_barcode")
        self.barcode_img = Image.open(filename)
        img = ImageTk.PhotoImage(self.barcode_img.resize((260, 140)))
        self.label.config(image=img)
        self.label.image = img

    def download(self):
        if not self.barcode_img:
            return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            self.barcode_img.save(path)

    def print_barcode(self):
        if not self.barcode_img:
            return
        self.barcode_img.save("temp_barcode_print.png")
        os.startfile("temp_barcode_print.png", "print")

    def refresh(self):
        self.entry.delete(0, tk.END)
        self.label.config(image="")
