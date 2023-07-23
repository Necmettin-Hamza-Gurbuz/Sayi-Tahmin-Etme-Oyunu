import time
import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    global deneme_hakki, yanlis_tahminler

    try:
        tahmin = int(entry_guess.get())

        if not 1 <= tahmin <= 100:
            messagebox.showwarning("Hatalı Giriş", "Lütfen 1 ile 100 arasında bir sayı giriniz.")
            return

        if tahmin > rastgele:
            feedback = "Bu yanlış: -"
        elif tahmin < rastgele:
            feedback = "Bu yanlış: +"
        else:
            feedback = "Tebrikler!! Sayıyı tutmuştum: " + str(rastgele)
            btn_guess.config(state=tk.DISABLED)

        yanlis_tahminler.append(str(tahmin))
        deneme_hakki -= 1

        if deneme_hakki == 0:
            feedback = "Maalesef hakkın doldu. Doğru sayı: " + str(rastgele)
            btn_guess.config(state=tk.DISABLED)

        lbl_feedback.config(text=feedback)
        lbl_attempts.config(text="Kalan Deneme Hakkı: " + str(deneme_hakki))

        if yanlis_tahminler:
            lbl_wrong_guesses.config(text="Yanlış Tahminler: " + ", ".join(yanlis_tahminler))
        
    except ValueError:
        messagebox.showwarning("Hatalı Giriş", "Lütfen geçerli bir sayı giriniz.")

def start_game():
    global rastgele, deneme_hakki, yanlis_tahminler

    liste = list(range(1, 101))
    rastgele = random.choice(liste)
    deneme_hakki = int(entry_attempts.get())
    yanlis_tahminler = []

    lbl_attempts.config(text="Kalan Deneme Hakkı: " + str(deneme_hakki))
    lbl_wrong_guesses.config(text="")
    lbl_feedback.config(text="")
    btn_guess.config(state=tk.NORMAL)

def create_game_window():
    global entry_guess, entry_attempts, lbl_attempts, lbl_feedback, lbl_wrong_guesses, btn_guess

    window = tk.Tk()
    window.title("Sayı Tahmin Oyunu")

    frame = tk.Frame(window)
    frame.pack(pady=10)

    lbl_welcome = tk.Label(frame, text="Merhaba! Bugün seninle bir oyun oynayacağız.", font=("Arial", 12))
    lbl_welcome.pack()

    lbl_instruction = tk.Label(frame, text="Ben 1'den 100'e kadar bir sayı tutacağım ve sen tahmin etmeye çalışacaksın.", font=("Arial", 12))
    lbl_instruction.pack()

    lbl_hint = tk.Label(frame, text="Eğer sana '+' dersem bil ki sayı daha yüksek, eğer sana '-' dersem bil ki sayı daha düşük.", font=("Arial", 12))
    lbl_hint.pack()

    lbl_attempts_prompt = tk.Label(frame, text="Kaç deneme hakkı istersin?:", font=("Arial", 12))
    lbl_attempts_prompt.pack()

    entry_attempts = tk.Entry(frame, font=("Arial", 12))
    entry_attempts.pack()

    btn_start = tk.Button(frame, text="Oyuna Başla", font=("Arial", 12), command=start_game)
    btn_start.pack()

    lbl_attempts = tk.Label(frame, text="Kalan Deneme Hakkı:", font=("Arial", 12))
    lbl_attempts.pack()

    entry_guess = tk.Entry(frame, font=("Arial", 12))
    entry_guess.pack()

    btn_guess = tk.Button(frame, text="Tahmin Et", font=("Arial", 12), command=check_guess, state=tk.DISABLED)
    btn_guess.pack()

    lbl_feedback = tk.Label(frame, text="", font=("Arial", 12))
    lbl_feedback.pack()

    lbl_wrong_guesses = tk.Label(frame, text="", font=("Arial", 12))
    lbl_wrong_guesses.pack()

    window.mainloop()

create_game_window()
