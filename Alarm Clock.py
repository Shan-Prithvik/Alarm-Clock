import tkinter as tk
import tkinter.messagebox as messagebox
import time
import winsound
from PIL import Image, ImageTk  # Import Pillow modules
import os

def set_alarm():
    alarm_time = time_entry.get()
    alarm_message = message_entry.get()
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == alarm_time:
            winsound.Beep(500, 1000)  # Beep at 500 Hz for 1 second
            show_message_popup(alarm_message)
            break

def show_message_popup(message):
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Alarm", message)
    root.deiconify()  # Show the main window again

def reset_alarm():
    time_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Alarm Clock")


time_label = tk.Label(root, text="Enter alarm time (HH:MM):", bg="lightgray")
time_label.pack(pady=10)

time_entry = tk.Entry(root)
time_entry.pack()

message_label = tk.Label(root, text="Enter alarm message:", bg="lightgray")
message_label.pack(pady=10)

message_entry = tk.Entry(root)
message_entry.pack()

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_alarm)
reset_button.pack(pady=5)

root.mainloop()
