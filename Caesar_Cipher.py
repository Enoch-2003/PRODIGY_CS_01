import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter message:").grid(row=0, column=0, padx=10, pady=10)
        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Enter shift value:").grid(row=1, column=0, padx=10, pady=10)
        self.shift_entry = tk.Entry(self.root, width=10)
        self.shift_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.encrypt_button = tk.Button(self.root, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.grid(row=2, column=0, padx=10, pady=10)

        self.decrypt_button = tk.Button(self.root, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.grid(row=3, column=0, padx=10, pady=10)

        self.result_text = tk.Text(self.root, height=4, width=50)
        self.result_text.grid(row=3, column=1, padx=10, pady=10)

    def encrypt_message(self):
        try:
            shift = int(self.shift_entry.get())
            message = self.message_entry.get()
            encrypted_message = encrypt(message, shift)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, encrypted_message)
        except ValueError:
            messagebox.showerror("Input error", "Please enter a valid shift value.")

    def decrypt_message(self):
        try:
            shift = int(self.shift_entry.get())
            message = self.message_entry.get()
            decrypted_message = decrypt(message, shift)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, decrypted_message)
        except ValueError:
            messagebox.showerror("Input error", "Please enter a valid shift value.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()