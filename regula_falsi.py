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
        
        # Hasil
        hasil_frame = tk.Frame(root)
        hasil_frame.pack(pady=10, fill="both", expand=True)
        
        tk.Label(hasil_frame, text="Hasil Iterasi:", font=self.font_bold).pack(anchor="w")
        
        # Text area & Scrollbar
        self.hasil_text = tk.Text(hasil_frame, height=15, width=95, font=("Courier New", 10), bg=self.text_bg, fg=self.text_fg)#.font_result)
        scrollbar = tk.Scrollbar(hasil_frame, command=self.hasil_text.yview)
        self.hasil_text.configure(yscrollcommand=scrollbar.set)
        
        self.hasil_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Label hasil akhir
        self.hasil_akhir = tk.Label(root, text="Akar: Belum dihitung", 
                                   font=self.font_bold, fg="red")
        self.hasil_akhir.pack(pady=5)
    
    # fungsi konversi string ke fungsi python
    def konversi_fungsi_ke_python(self, func_str):
        """Konversi fungsi matematika ke format Python"""
        func_str = func_str.replace("^", "**")
        func_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', func_str)
        func_str = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', func_str)
        func_str = re.sub(r'(\))([a-zA-Z0-9])', r'\1*\2', func_str)
        func_str = re.sub(r'([a-zA-Z0-9])(\()', r'\1*\2', func_str)
        return func_str

    # Hitung fungsi dengan aman
    def f(self, x):
        """Menghitung nilai fungsi dengan keamanan"""
        try:
            fungsi_python = self.konversi_fungsi_ke_python(self.fungsi_entry.get())
            safe_dict = {
                'x': x, 'math': math, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'log': math.log, 'log10': math.log10, 'exp': math.exp, 'sqrt': math.sqrt,
                'pi': math.pi, 'e': math.e
            }
            result = eval(fungsi_python, {"__builtins__": {}}, safe_dict)
            return result
        except:
            return None
    
    # Fungsi hitung(),Proses Utama Metode Regula Falsi
    def hitung(self):
        """Menghitung akar dengan metode Regula Falsi"""
        try:
            # Validasi input tidak kosong
            if not self.fungsi_entry.get().strip():
                messagebox.showerror("Error", "Fungsi f(x) harus diisi!")
                return
            if not self.a_entry.get().strip():
                messagebox.showerror("Error", "Batas atas (a) harus diisi!")
                return
            if not self.b_entry.get().strip():
                messagebox.showerror("Error", "Batas bawah (b) harus diisi!")
                return
            if not self.toleransi_entry.get().strip():
                messagebox.showerror("Error", "Toleransi error harus diisi!")
                return
            if not self.iterasi_entry.get().strip():
                messagebox.showerror("Error", "Max iterasi harus diisi!")
                return
            
            # Ambil input - SUDAH DIBALIK
            a = float(self.a_entry.get())  # a = batas atas
            b = float(self.b_entry.get())  # b = batas bawah
            
            # Validasi: a harus > b (karena a batas atas, b batas bawah)
            if a <= b:
                messagebox.showerror("Error", "Batas atas (a) harus lebih besar dari batas bawah (b)!")
                return
            
            toleransi = float(self.toleransi_entry.get())
            max_iter = int(self.iterasi_entry.get())
            
            if toleransi <= 0:
                messagebox.showerror("Error", "Toleransi harus lebih besar dari 0!")
                return
            if max_iter <= 0:
                messagebox.showerror("Error", "Max iterasi harus lebih besar dari 0!")
                return
            
            # Validasi fungsi
            if self.f(a) is None or self.f(b) is None:
                messagebox.showerror("Error", "Fungsi tidak valid! Periksa format fungsi.")
                return
            
            # Validasi interval
            fa = self.f(a)
            fb = self.f(b)
            if fa * fb > 0:
                messagebox.showerror("Error", f"f(a) dan f(b) harus berbeda tanda!\nf({a}) = {fa:.4f}, f({b}) = {fb:.4f}")
                return
            
            # Bersihkan hasil sebelumnya
            self.hasil_text.delete(1.0, tk.END)
    
