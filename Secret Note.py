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

def save_encrypt_button_click():
    global password
    file_name = note_name_entry.get()
    content = password
    key = key_entry.get()
    with open(file_name, "a") as file:
        file.write(content)
    messagebox.showinfo("Transaction successful", f"The file named {file_name} was created!")

save_button = Button(text="Save & Secret",command=save_encrypt_button_click)
save_button.pack()

def decrypt_button_click():
    encrypted_text = note.get(1.0,END)  #User İnput
    try:
        decrypted_text = base64.b64decode(encrypted_text).decode("utf-8")  # Base64
        messagebox.showinfo(f"Çözülmüş Metin:{decrypted_text}")
    except:
        messagebox.showerror("Hata", "Geçersiz şifrelenmiş metin!")

decrypt_button = Button(text="Decrypt",command=decrypt_button_click)
decrypt_button.pack()

def encrypt_text():#b and pw_2
    a = note.get(1.0, END)
    pw = base64.b64encode(a.encode("utf-8")).decode("utf-8")  # Base64 şifreleme
    return pw
password= encrypt_text()


window.mainloop()