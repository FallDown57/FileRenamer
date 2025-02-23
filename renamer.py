import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import time
from PIL import Image, ImageTk

METAMASK_ADDRESS = "0xe87cB10d373Ce2d1114487d916D9600537c7bd3C"

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def rename_files(folder_path, new_name, progress_bar, window):
    count = 1
    total_items = len(os.listdir(folder_path))
    progress_bar["maximum"] = total_items
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        file_ext = os.path.splitext(item)[1] if os.path.isfile(item_path) else ""
        new_filename = f"{new_name}{count}{file_ext}"
        new_path = os.path.join(folder_path, new_filename)
        os.rename(item_path, new_path)
        count += 1
        progress_bar["value"] = count - 1
        window.update_idletasks()
        time.sleep(0.05)
    return f"Done! Renamed {count-1} items to {new_name}1, {new_name}2, etc."

def start_renaming():
    folder_path = folder_entry.get()
    new_name = name_entry.get()
    if not folder_path or not os.path.exists(folder_path):
        messagebox.showerror("Oops", "Bruh, pick a real folder!", icon="warning")
        return
    if not new_name:
        messagebox.showerror("Oops", "Bruh, type a name!", icon="warning")
        return
    loading_window = tk.Toplevel()
    loading_window.title("Renaming...")
    loading_window.geometry("350x150")
    loading_window.configure(bg="#2e2e2e")
    tk.Label(loading_window, text="Hold up, renaming your stuff...", fg="white", bg="#2e2e2e", font=("Arial", 12, "bold")).pack(pady=10)
    progress_bar = ttk.Progressbar(loading_window, length=250, mode="determinate", style="Custom.Horizontal.TProgressbar")
    progress_bar.pack(pady=10)
    loading_window.transient(window)
    loading_window.grab_set()
    def run():
        result = rename_files(folder_path, new_name, progress_bar, loading_window)
        loading_window.destroy()
        messagebox.showinfo("Success", result, icon="info")
    threading.Thread(target=run, daemon=True).start()

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

def copy_address():
    window.clipboard_clear()
    window.clipboard_append(METAMASK_ADDRESS)
    messagebox.showinfo("Copied", "Address copied to clipboard! Paste it in your wallet to tip me!")

window = tk.Tk()
window.title("File Renamer by Bro")
window.geometry("450x400")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("default")
style.configure("Custom.Horizontal.TProgressbar", troughcolor="#1e1e1e", background="#00ff00", thickness=20)

try:
    logo_path = resource_path("assets/logo.png")
    logo = Image.open(logo_path)
    logo = logo.resize((60, 60), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo)
    tk.Label(window, image=logo_photo, bg="#1e1e1e").pack(pady=10)
except Exception as e:
    tk.Label(window, text=f"Logo broke, bro! {str(e)}", fg="white", bg="#1e1e1e").pack(pady=10)

tk.Label(window, text="Pick your folder:", fg="white", bg="#1e1e1e", font=("Arial", 10, "bold")).pack(pady=5)
folder_entry = tk.Entry(window, width=40, bg="#333333", fg="white", insertbackground="white")
folder_entry.pack()
tk.Button(window, text="Browse", command=browse_folder, bg="#555555", fg="white", relief="flat").pack(pady=5)

tk.Label(window, text="What you wanna call ‘em?", fg="white", bg="#1e1e1e", font=("Arial", 10, "bold")).pack(pady=5)
name_entry = tk.Entry(window, width=40, bg="#333333", fg="white", insertbackground="white")
name_entry.pack()

rename_btn = tk.Button(window, text="Rename ‘Em!", command=start_renaming, bg="#00cc00", fg="white", font=("Arial", 12, "bold"), relief="flat")
rename_btn.pack(pady=20)

tk.Label(window, text="Look, I’m not saying you should do it, but… you know /:", fg="white", bg="#1e1e1e", font=("Arial", 9)).pack(pady=5)
tip_btn = tk.Button(window, text=f"ETH: {METAMASK_ADDRESS}", command=copy_address, bg="#00cc00", fg="white", font=("Arial", 8, "bold"), relief="flat", wraplength=400, justify="center")
tip_btn.pack(pady=5)

tk.Label(window, text="v1.0 - Built with love by Bro", fg="#666666", bg="#1e1e1e", font=("Arial", 8)).pack(side="bottom", pady=5)

window.mainloop()