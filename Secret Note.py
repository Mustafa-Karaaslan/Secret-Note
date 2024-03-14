from tkinter import *
from PIL import ImageTk, Image
import os

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

def save_click():
    pass

save_button = Button(text="Save & Secret",command=save_click)
save_button.pack()

def decrypt_click():
    pass

decrypt_button = Button(text="decrypt",command=decrypt_click)





window.mainloop()