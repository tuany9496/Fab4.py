import tkinter

window = tkinter.Tk()
entry = tkinter.Entry(window)

def encrypt():
    encrypt_label = tkinter.Label(window, text="Please enter the message you'd like to encrypt", font=('Helvetica', 14))
    encrypt_label.pack()
    entry = tkinter.Entry(window)
    entry.pack()
    encrypt_confirm = tkinter.Button(window, text="Confirm")
    encrypt_confirm.pack()
    back_button = tkinter.Button(window, text="Back", command=back)
    back_button.pack()
    encrypt_button.destroy()
    title_header.destroy() 
    title_label.destroy()
    heading_label.destroy()

def back():
    title_header = tkinter.Label(window, text="ENCRYPTION/DECRYPTION", font=('Helvetica', 16))
    title_header.pack()
    title_label = tkinter.Label(window, text="Welcome to this encryption and decryption program")
    title_label.pack()
    heading_label = tkinter.Label(window, text="When you are ready, press a button to continue")
    heading_label.pack()
    encrypt_button = tkinter.Button(window, text="Encrypt", command=encrypt)
    encrypt_button.pack()
    encrypt_label.destroy()
    entry.destroy()
    encrypt_confirm.destroy()
    back_button.destroy()

title_header = tkinter.Label(window, text="ENCRYPTION/DECRYPTION", font=('Helvetica', 16))
title_header.pack()

title_label = tkinter.Label(window, text="Welcome to this encryption and decryption program")
title_label.pack()

heading_label = tkinter.Label(window, text="When you are ready, press a button to continue")
heading_label.pack()

encrypt_button = tkinter.Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()

encrypt_label = tkinter.Label(window, text="Please enter the message you'd like to encrypt", font=('Helvetica', 14))

entry = tkinter.Entry(window)

encrypt_confirm = tkinter.Button(window, text="Confirm")

back_button = tkinter.Button(window, text="Back", command=back)

window.mainloop()