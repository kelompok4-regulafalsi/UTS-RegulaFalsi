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
        
        #input_frame = tk.Frame(root)
        
        input_frame.pack(pady=10)
        
        # Input fungsi
        tk.Label(input_frame, text="Fungsi f(x):", font=self.font_style).grid(row=0, column=0, sticky="w", pady=5)
        self.fungsi_entry = tk.Entry(input_frame, width=30, font=self.font_style)
        self.fungsi_entry.grid(row=0, column=1, padx=10, pady=5)
        self.fungsi_entry.insert(0, "")
        
        # Input batas atas
        tk.Label(input_frame, text="Batas atas (a):", font=self.font_style).grid(row=1, column=0, sticky="w", pady=5)
        self.a_entry = tk.Entry(input_frame, width=15, font=self.font_style)
        self.a_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        self.a_entry.insert(0, "")
        
        #input batas bawah
        tk.Label(input_frame, text="Batas bawah (b):", font=self.font_style).grid(row=2, column=0, sticky="w", pady=5)
        self.b_entry = tk.Entry(input_frame, width=15, font=self.font_style)
        self.b_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)
        self.b_entry.insert(0, "")
        
        # Input toleransi error
        tk.Label(input_frame, text="Toleransi error:", font=self.font_style).grid(row=3, column=0, sticky="w", pady=5)
        self.toleransi_entry = tk.Entry(input_frame, width=15, font=self.font_style)
        self.toleransi_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)
        self.toleransi_entry.insert(0, "")
        
        #input iterasi maksimum
        tk.Label(input_frame, text="Max iterasi:", font=self.font_style).grid(row=4, column=0, sticky="w", pady=5)
        self.iterasi_entry = tk.Entry(input_frame, width=15, font=self.font_style)
        self.iterasi_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)
        self.iterasi_entry.insert(0, "")
        
        # Tombol
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # tombol hitung dan reset 
        tk.Button(button_frame, text="HITUNG", command=self.hitung, 
                 bg="lightblue", font=self.font_style, width=10).pack(side="left", padx=5)
        tk.Button(button_frame, text="RESET", command=self.reset, 
                 bg="lightcoral", font=self.font_style, width=10).pack(side="left", padx=5)
        

