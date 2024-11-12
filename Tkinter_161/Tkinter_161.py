import tkinter as tk #mengimpor pustaka tkinter untuk digunakan dalam GUI
from tkinter import messagebox #mengimpor modul messagebox dari pustaka tkinter"

def hasil_prediksi():
    for entry in nilai_entries:
        if entry.get().strip() == "":
            hasil_label.config(text="Harap isi semua nilai mata pelajaran.", fg="red")
            return #memeriksa input kosong
    try:
        for entry in nilai_entries:
            nilai = int(entry.get())
            if not (0 <= nilai <=100):
                messagebox.showinfo("Ingpo maszeh", "Nilai harus antara 0 dan 100.") #memastikan input bernilai antara 0-100
                return
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi") #Jika semua input valid, label hasil_label akan menampilkan teks "Prediksi Prodi: Teknologi Informasi".
    except ValueError as ve:
            messagebox.showerror("Input Error", "Pastikan semua input adalah angka") #Jika semua input valid, label hasil_label akan menampilkan teks "Prediksi Prodi: Teknologi Informasi".
            return
    # Fungsi untuk menghasilkan tulisan saat button hasil prediksi ditekan
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi", fg="black")

# Membuat window utama
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan")

# Menambahkan label judul
judul_label = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

nilai_entries = [] #fungsi untuk memasukkan nilai

for i in range(10):
    label = tk.Label(window, text=f"Nilai Mata Pelajaran {i+1} :")
    label.grid(row=i+1, column=0, padx=1, pady=5, sticky="w")
    entry = tk.Entry(window)
    entry.grid(row=i+1, column=1, padx=1, pady=5)
    nilai_entries.append(entry) #memberi 10 baris input nilai




# Menambahkan button untuk memprediksi prodi pilihan
prediksi_button = tk.Button(window, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Menambahkan label untuk  menampilkan hasil prediksi
hasil_label = tk.Label(window, text="", font=("Arial", 14))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
window.mainloop()
