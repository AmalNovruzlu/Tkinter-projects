import tkinter as tk
import qrcode
from PIL import Image,ImageTk

def generate_qr():
    txt=entry1.get()
    if txt:
        result_label.config(text="QR Code Generated!")
        img=qrcode.make(txt)
        img.save("my_qr.png")
        
        qr_img=Image.open("my_qr.png")
        qr_img=qr_img.resize((200,200))
        img_tk=ImageTk.PhotoImage(qr_img)
        qr_label.config(image=img_tk)
        qr_label.image=img_tk
    else:       
        result_label.config(text="Please enter a text")

root=tk.Tk()
root.title("QR Code Generator")

label1=tk.Label(root, text="Enter text or URL: ")
label1.pack(pady=5)

entry1=tk.Entry(root)
entry1.pack(pady=5)

button1=tk.Button(root, text="Generate The QR Code: ",command=generate_qr)
button1.pack(pady=5)

result_label=tk.Label(root, text="")
result_label.pack(pady=5)

qr_label=tk.Label(root)
qr_label.pack(pady=5)

root.mainloop()
