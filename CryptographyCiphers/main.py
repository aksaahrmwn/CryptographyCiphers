# main.py

import tkinter as tk
from tkinter import filedialog, messagebox
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from playfair_cipher import playfair_encrypt, playfair_decrypt
from hill_cipher import hill_encrypt, hill_decrypt

# Fungsi untuk memilih file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            plaintext_entry.delete(1.0, tk.END)
            plaintext_entry.insert(tk.END, file.read())

# Fungsi enkripsi
def encrypt_message(cipher_type):
    plaintext = plaintext_entry.get(1.0, tk.END).strip()
    key = key_entry.get()

    if not plaintext or not key:
        messagebox.showerror("Error", "Pesan dan kunci tidak boleh kosong!")
        return

    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus memiliki minimal 12 karakter!")
        return

    if cipher_type == 'vigenere':
        encrypted_message = vigenere_encrypt(plaintext, key)
    elif cipher_type == 'playfair':
        encrypted_message = playfair_encrypt(plaintext, key)
    elif cipher_type == 'hill':
        encrypted_message = hill_encrypt(plaintext, key)
    else:
        encrypted_message = ""

    result_entry.delete(1.0, tk.END)
    result_entry.insert(tk.END, encrypted_message)

# Fungsi dekripsi
def decrypt_message(cipher_type):
    ciphertext = plaintext_entry.get(1.0, tk.END).strip()
    key = key_entry.get()

    if not ciphertext or not key:
        messagebox.showerror("Error", "Pesan dan kunci tidak boleh kosong!")
        return

    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus memiliki minimal 12 karakter!")
        return

    if cipher_type == 'vigenere':
        decrypted_message = vigenere_decrypt(ciphertext, key)
    elif cipher_type == 'playfair':
        decrypted_message = playfair_decrypt(ciphertext, key)
    elif cipher_type == 'hill':
        decrypted_message = hill_decrypt(ciphertext, key)
    else:
        decrypted_message = ""

    result_entry.delete(1.0, tk.END)
    result_entry.insert(tk.END, decrypted_message)

# Setup GUI
root = tk.Tk()
root.title("Cryptography Ciphers - Enkripsi & Dekripsi")
root.geometry("600x500")

# Label dan input untuk pesan
plaintext_label = tk.Label(root, text="Pesan:")
plaintext_label.pack()

plaintext_entry = tk.Text(root, height=5, width=50)
plaintext_entry.pack()

# Tombol untuk memilih file
file_button = tk.Button(root, text="Pilih File", command=select_file)
file_button.pack()

# Label dan input untuk kunci
key_label = tk.Label(root, text="Kunci (minimal 12 karakter):")
key_label.pack()

key_entry = tk.Entry(root, width=50)
key_entry.pack()

# Tombol untuk enkripsi dan dekripsi Vigenere
encrypt_vigenere_button = tk.Button(root, text="Enkripsi (Vigenere)", command=lambda: encrypt_message('vigenere'))
encrypt_vigenere_button.pack(pady=5)

decrypt_vigenere_button = tk.Button(root, text="Dekripsi (Vigenere)", command=lambda: decrypt_message('vigenere'))
decrypt_vigenere_button.pack(pady=5)

# Tombol untuk enkripsi dan dekripsi Playfair
encrypt_playfair_button = tk.Button(root, text="Enkripsi (Playfair)", command=lambda: encrypt_message('playfair'))
encrypt_playfair_button.pack(pady=5)

decrypt_playfair_button = tk.Button(root, text="Dekripsi (Playfair)", command=lambda: decrypt_message('playfair'))
decrypt_playfair_button.pack(pady=5)

# Tombol untuk enkripsi dan dekripsi Hill
encrypt_hill_button = tk.Button(root, text="Enkripsi (Hill)", command=lambda: encrypt_message('hill'))
encrypt_hill_button.pack(pady=5)

decrypt_hill_button = tk.Button(root, text="Dekripsi (Hill)", command=lambda: decrypt_message('hill'))
decrypt_hill_button.pack(pady=5)

# Hasil enkripsi/dekripsi
result_label = tk.Label(root, text="Hasil:")
result_label.pack()

result_entry = tk.Text(root, height=5, width=50)
result_entry.pack()

# Jalankan GUI
root.mainloop()