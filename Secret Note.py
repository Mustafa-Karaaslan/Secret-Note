from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import base64

#window
window = Tk()
window.title("Secret Note")
window.minsize(350,500)
window.config(padx=30,pady=30)

#font
font_1=("Ariel",20,"italic")


#image
img = ImageTk.PhotoImage(Image.open("Secret.png"))
picture = Label(image = img,font=('Ariel', 1, "italic"))
picture.pack(fill = "both", expand = "yes")


note_name_label = Label(text="Enter note name:", font=font_1)
note_name_label.pack()

note_name_entry = Entry()
note_name_entry.pack()

note_label = Label(text="Enter secret note:",font=font_1)
note_label.pack()

note = Text()
note.config(height=15,width=40)
note.pack()

key_label = Label(text="Enter key:",font=font_1)
key_label.pack()

key_entry = Entry()
key_entry.pack()

def save_encrypt_click():
    file_name = note_name_entry.get()
    content = note.get(1.0,END)
    key = key_entry.get()
    with open(file_name, "a") as file:
        file.write(content)
    messagebox.showinfo("Transaction successful", f"The file named {file_name} was created!")

save_button = Button(text="Save & Secret",command=save_encrypt_click)
save_button.pack()

def decrypt_click():
    pass
decrypt_button = Button(text="Decrypt",command=decrypt_click)
decrypt_button.pack()



window.mainloop()