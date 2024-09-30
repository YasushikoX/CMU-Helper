import time
import tkinter as tk
from tkinter import messagebox, filedialog
import pyautogui
import keyboard

def count_tabs_and_spaces(line):
    tab_count = line.count('\t')
    space_count = line.count('    ')
    return tab_count + space_count

def type_text(text, interval):
    if keyboard.is_pressed('esc'):
        print("Program aborted.")
        status_var.set("Program aborted.")
        status_bar.config(bg="red")
        return
    
    lines = text.split('\n')
    previous_tabs = 0
    for line in lines:
        stripped_line = line.lstrip('\t').lstrip(' ')
        current_tabs = count_tabs_and_spaces(line)
        tab_difference = previous_tabs - current_tabs
        for _ in range(tab_difference):
            pyautogui.press('backspace')
        
        pyautogui.typewrite(stripped_line, interval=interval)
        pyautogui.press('enter')
        
        previous_tabs = current_tabs

def start_typing():
    text_to_type = text_entry.get("1.0", tk.END).strip()
    if not text_to_type:
        messagebox.showwarning("Input Error", "Restart the program and enter text to type.")
        return
    try:
        interval = float(0)
        start_delay = float(start_delay_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for interval and start delay.")
        return
    
    status_var.set("Typing will start in {} seconds...".format(start_delay))
    status_bar.config(bg="yellow")
    root.update()
    time.sleep(start_delay)
    
    status_var.set("Typing in progress...")
    status_bar.config(bg="green")
    root.update()
    
    type_text(text_to_type, interval)
    
    status_var.set("Typing completed.")
    status_bar.config(bg="blue")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()
            text_entry.delete("1.0", tk.END)
            text_entry.insert(tk.END, file_content)

#!!GUI
root = tk.Tk()
root.title("Cheater")
root.geometry("800x600")  # Set initial size of the window
root.resizable(True, True)

tk.Label(root, text="Select what to do").pack(pady=10)

open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.pack()

tk.Label(root, text="Or").pack(pady=10)
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10, expand=True, fill='both')

tk.Label(root, text="Interval before starting (seconds):").pack(pady=5)
start_delay_entry = tk.Entry(root)
start_delay_entry.insert(0, "5")
start_delay_entry.pack(pady=5)

tk.Button(root, text="Start Typing", command=start_typing).pack(pady=10)

status_var = tk.StringVar()
status_var.set("Ready")
status_bar = tk.Label(root, textvariable=status_var, bd=0, relief=tk.SUNKEN, anchor=tk.CENTER)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
status_bar.config(bg="green")

root.mainloop()