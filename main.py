import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Add the paths to your images
pic1 = "bear-love.gif"
pic2 = "bear-love.gif"
pic3 = "bear-kiss-bear-kisses.gif"

def ask_name():
    name = name_entry.get().strip()
    if name.isalpha():
        photo1_label.pack_forget()
        name_label.pack_forget()
        name_entry.pack_forget()
        name_button.pack_forget()
        photo_label.pack(pady=8)  # Show the photo above the question
        question_label.config(text=f"{name}, Do You Love Me?❤️")
        question_label.pack(pady=7)  # Show the question label
        yes_button.pack()
        no_button.pack()
    else:
        messagebox.showerror("Invalid Input!", "Hey! babe enter your name😘.")

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Love Confession ❤")

    # Load and display the third image in the popup
    photo3 = load_and_resize_image(pic3)
    photo3_label = tk.Label(popup, image=photo3, background='mistyrose')
    photo3_label.image = photo3  # Keep a reference to avoid garbage collection
    photo3_label.pack(pady=10)  # Pack the image at the top of the popup

    label = tk.Label(popup, font=('calibri', 15, 'bold'), background='mistyrose', foreground='red',
                     text="I knew it! You love me too! 😍 \nTake my Insta ID: mahmudulhasanzb")
    label.pack(padx=20, pady=20)

def move_button(event):
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    margin = 50
    x = random.randint(margin, window_width - margin)
    y = random.randint(margin, window_height - margin)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.title("Instagram: @mahmudulhasanzb")
root.geometry("800x400")
root.config(background='lavenderblush')

def load_and_resize_image(image_path):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((150, 95), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

# Load and display the first image
photo1 = load_and_resize_image(pic1)
photo1_label = tk.Label(root, image=photo1, background='lavenderblush')
photo1_label.pack(pady=8)

# Load and display the second image
photo2 = load_and_resize_image(pic2)
photo_label = tk.Label(root, image=photo2, background='lavenderblush')

# Name input section
name_label = tk.Label(root, font=('calibri', 15, 'bold'), background='lavenderblush', foreground='deeppink',text="Enter your name:")
name_label.pack(pady=4)

name_entry = tk.Entry(root, font=('calibri', 15), background='white', foreground='deeppink')
name_entry.pack(pady=11)

name_button = tk.Button(root, font=('calibri', 15, 'bold'), background='lightpink', foreground='deeppink', text="Submit", command=ask_name)
name_button.pack(pady=6)

question_label = tk.Label(root, font=('calibri', 20, 'bold'), background='deeppink', foreground='white')

yes_button = tk.Button(root, font=('calibri', 15, 'bold'), background='lightpink', foreground='deeppink', text="Yes", command=show_popup)
no_button = tk.Button(root, font=('calibri', 15 , 'bold'), background='lightpink', foreground='deeppink', text="No")
no_button.bind("<Enter>", move_button)

root.mainloop()