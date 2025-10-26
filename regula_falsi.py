import tkinter as tk
from tkinter import ttk, messagebox
import math
import re

class KalkulatorRegulaFalsi:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Regula Falsi")
        self.root.geometry("800x550")

        #teks entry
        self.bg_color = "#FFF0F5"            # Soft pink muda (latar utama)
        self.frame_color = "#E6F0FA"         # Biru pastel lembut (frame input & hasil)
        self.button_color = "#87CEFA"        # LightSkyBlue (tombol hitung)
        self.button_reset_color = "#FFB6C1"  # LightPink (tombol reset)
        self.text_bg = "#FDFEFE"             # Putih lembut untuk hasil iterasi
        self.text_fg = "#1C2833"             # Abu tua (teks hasil iterasi)
        self.highlight_color = "#5DADE2"     # Biru medium (judul & highlight)
        self.result_fg = "#2E8B57"           # Hijau medium (hasil akhir)
        self.warning_fg = "#E67E22"          # Orange lembut (peringatan)
        
       
        # Background utama
        root.configure(bg=self.bg_color)

                
        # Configure font
        self.font_style = ("Times New Roman", 10)
        self.font_bold = ("Times New Roman", 11, "bold")
        self.font_title = ("Times New Roman", 14, "bold")
        self.font_result = ("Times New Roman", 9)
        
        # Judul
        title_label = tk.Label(root, text="KALKULATOR METODE REGULA FALSI", 
                              font=self.font_title,
                              bg = self.bg_color, #warna latar belakang judul
                              fg = self.highlight_color) # warna teks judul (biru tua)
        title_label.pack(pady=10)
        
        # Frame input
        input_frame = tk.Frame(root, bg=self.frame_color, bd=2, relief="ridge")

