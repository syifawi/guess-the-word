import random
import tkinter as tk
from tkinter import messagebox

buah = ["apel", "jeruk", "mangga", "pisang", "anggur", "kiwi", "semangka", 
        "nangka", "durian", "salak", "melon", "manggis", "strawberry", 
        "cerry", "alpukat", "jambu", "belimbing", "blueberry", "aprikot"]

def acak_huruf(kata):
    kata_acak = list(kata)
    random.shuffle(kata_acak)
    return ''.join(kata_acak)

class TebakKataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Tebak Acak Kata")
        self.root.configure(bg='#ADD8E6')  # Warna background utama

        # Header
        self.header = tk.Label(root, text="GAME TEBAK ACAK KATA", font=("Helvetica", 20, "bold"), 
                               fg="white", bg="#4682B4")
        self.header.pack(pady=20)

        # Label Pertanyaan
        self.teka_teki_label = tk.Label(root, text="Tebak buah apa ini:", font=("Helvetica", 16, "italic"), 
                                        fg="#2E8B57", bg='#ADD8E6')
        self.teka_teki_label.pack(pady=10)

        # Display Kata Acak
        self.teka_teki = tk.StringVar()
        self.teka_teki_display = tk.Label(root, textvariable=self.teka_teki, font=("Helvetica", 18, "bold"), 
                                          fg="#8B0000", bg='#ADD8E6')
        self.teka_teki_display.pack(pady=10)

        # Input Jawaban
        self.jawaban_entry = tk.Entry(root, font=("Helvetica", 16), fg="#00008B", bg="#FAFAD2")
        self.jawaban_entry.pack(pady=10)

        # Tombol Cek Jawaban
        self.cek_button = tk.Button(root, text="Cek Jawaban", font=("Helvetica", 14), bg="#32CD32", fg="white", 
                                    activebackground="#228B22", activeforeground="white", command=self.cek_jawaban)
        self.cek_button.pack(pady=20)

        # Memulai permainan pertama kali
        self.main_game()

    def main_game(self):
        indeks = random.randint(0, len(buah) - 1)
        self.kata_asli = buah[indeks]
        self.teka_teki.set(acak_huruf(self.kata_asli))

    def cek_jawaban(self):
        jawaban = self.jawaban_entry.get().lower()
        if jawaban == self.kata_asli:
            messagebox.showinfo("Hasil", "SELAMAT JAWABAN ANDA BENAR")
        else:
            messagebox.showerror("Hasil", f"JAWABAN ANDA SALAH, YANG BENAR: {self.kata_asli}")
        self.jawaban_entry.delete(0, tk.END)
        self.main_game()

if __name__ == "__main__":
    root = tk.Tk()
    app = TebakKataApp(root)
    root.mainloop()

