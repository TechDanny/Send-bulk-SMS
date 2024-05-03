import tkinter as tk
from tkinter import filedialog, messagebox
import africastalking
import csv
from PIL import Image, ImageTk
from dotenv import load_dotenv
import os

load_dotenv() # Get environment variable from .env file

# This function will send sms using API
def send_sms(username, message, numbers):
    response = sms.send(message, numbers)
    print(response)  # for debugging purpose

# This function will upload csv file
def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            contacts = [row[0] for row in reader] #This I assumed the phone numbers are on the first column
            messagebox.showinfo("Success", "CSV file uploaded successfully.")
            global uploaded_contacts
            uploaded_contacts = contacts
            return contacts
    else:
        messagebox.showerror("Error", "Please select a CSV file.")
        return None

# This function will handle sending bulk sms
def send_bulk_sms():
    username = api_username_entry.get()
    message = message_entry.get("1.0", "end-1c")
    contacts = uploaded_contacts
    if not username or not message or contacts is None:
        messagebox.showerror("Error", "Please fill in all fields and upload a CSV file.")
    else:
        send_sms(username, message, contacts)
        messagebox.showinfo("Success", "SMS sent successfully.")

# set GUI
root = tk.Tk()
root.title("Bulk SMS Sender")
root.geometry("500x300")

# Logo image
img = Image.open("./images/sms.png")
img = img.resize((50, 50))
icon = ImageTk.PhotoImage(img)
root.iconphoto(False, icon)

# background color
root.config(bg="#f0f0f0")

# Setup Africa's Talking API
africastalking_username = os.getenv("AFRICASTALKING_USERNAME")
africastalking_api_key = os.getenv("AFRICASTALKING_API_KEY")

africastalking.initialize(africastalking_username, africastalking_api_key)
sms = africastalking.SMS

api_username_label = tk.Label(root, text="API Username:", bg="#f0f0f0", font=("Helvetica", 12))
api_username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

api_username_entry = tk.Entry(root)
api_username_entry.grid(row=0, column=1, padx=10, pady=5)

message_label = tk.Label(root, text="Message:", bg="#f0f0f0", font=("Helvetica", 12))
message_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

message_entry = tk.Text(root, height=4, width=40)
message_entry.grid(row=1, column=1, padx=10, pady=5)

upload_button = tk.Button(root, text="Upload CSV", command=upload_file, bg="#4caf50", fg="white", font=("Helvetica", 12))
upload_button.grid(row=2, column=0, padx=10, pady=5)

send_button = tk.Button(root, text="Send SMS", command=send_bulk_sms, bg="#2196f3", fg="white", font=("Helvetica", 12))
send_button.grid(row=2, column=1, padx=10, pady=5)

uploaded_contacts = None

root.mainloop()
